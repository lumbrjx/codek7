package api

import (
	"context"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strconv"

	"github.com/google/uuid"
	"github.com/lumbrjx/codek7/gateway/pkg/utils"
	"github.com/segmentio/kafka-go"
)

func (a API) UploadFile(w http.ResponseWriter, r *http.Request) {
	err := r.ParseMultipartForm(0)
	if err != nil {
		http.Error(w, `{"status":"error","message":"Failed to parse form"}`, http.StatusBadRequest)
		return
	}
	userID, ok := utils.GetUserID(r.Context())
	if !ok {
		http.Error(w, "User ID not found in context", http.StatusUnauthorized)
		return
	}
	title := r.FormValue("title")
	description := r.FormValue("description")

	if title == "" || userID == "" || description == "" {
		http.Error(w, `{"status":"error","message":"Missing required fields: title, user_id, or description"}`, http.StatusBadRequest)
		return
	}

	// Get the file from form
	file, handler, err := r.FormFile("file")
	if err != nil {
		http.Error(w, `{"status":"error","message":"File not found in request"}`, http.StatusBadRequest)
		return
	}
	defer file.Close()

	fmt.Printf("Receiving file: %s\n", handler.Filename)

	// Save file to temp location
	tmpFile, err := os.CreateTemp("", "upload-*.mp4")
	if err != nil {
		http.Error(w, `{"status":"error","message":"Failed to create temp file"}`, http.StatusInternalServerError)
		return
	}
	defer tmpFile.Close()

	_, err = io.Copy(tmpFile, file)
	if err != nil {
		http.Error(w, `{"status":"error","message":"Failed to save file"}`, http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusAccepted)
	w.Write([]byte(`{"status":"success","message":"File received and processing started"}`))

	// Start async processing
	go processFile(a.Producer, tmpFile.Name(), userID, title, description)
}

func processFile(producer *kafka.Writer, filePath string, userID, title, description string) {
	defer os.Remove(filePath)

	videoID := uuid.New().String()
	sem := make(chan struct{}, 40)
	chunkBuf := make([]byte, 32*1024)

	f, err := os.Open(filePath)
	if err != nil {
		log.Printf("❌ Failed to open file: %v", err)
		return
	}
	defer f.Close()

	var chunks [][]byte

	for {
		n, err := f.Read(chunkBuf)
		if err != nil && err != io.EOF {
			log.Printf("❌ Error reading chunk: %v", err)
			return
		}
		if n == 0 {
			break
		}

		chunk := make([]byte, n)
		copy(chunk, chunkBuf[:n])
		chunks = append(chunks, chunk)
	}

	totalChunks := len(chunks)
	fmt.Printf("📦 Total chunks: %d\n", totalChunks)

	for i, chunk := range chunks {
		sem <- struct{}{}
		go func(idx int, data []byte) {
			defer func() { <-sem }()
			produceChunk(producer, videoID, int32(idx), int32(totalChunks), data, filePath, userID, title, description)
		}(i, chunk)
	}

	// Wait for all goroutines to finish
	for i := 0; i < cap(sem); i++ {
		sem <- struct{}{}
	}
}

func produceChunk(producer *kafka.Writer, videoID string, index int32, totalChunks int32, chunk []byte, filepath string, userID, title, description string) {
	msg := kafka.Message{
		Key:   []byte(videoID),
		Value: chunk,
		Headers: []kafka.Header{
			{Key: "chunk_index", Value: []byte(strconv.Itoa(int(index)))},
			{Key: "total_chunks", Value: []byte(strconv.Itoa(int(totalChunks)))},
			{Key: "file_path", Value: []byte(filepath)},
			{Key: "user_id", Value: []byte(userID)},
			{Key: "title", Value: []byte(title)},
			{Key: "description", Value: []byte(description)},
		},
	}

	err := producer.WriteMessages(context.Background(), msg)
	if err != nil {
		fmt.Printf("❌ Failed to send chunk %d: %v\n", index, err)
	} else {
		fmt.Printf("✅ Sent chunk %d/%d to Kafka\n", index+1, totalChunks)
	}
}
