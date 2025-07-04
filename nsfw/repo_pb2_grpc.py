# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import repo_pb2 as repo__pb2

GRPC_GENERATED_VERSION = '1.73.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in repo_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class RepoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/repo.RepoService/CreateUser',
                request_serializer=repo__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=repo__pb2.UserResponse.FromString,
                _registered_method=True)
        self.GetUser = channel.unary_unary(
                '/repo.RepoService/GetUser',
                request_serializer=repo__pb2.GetUserRequest.SerializeToString,
                response_deserializer=repo__pb2.UserResponse.FromString,
                _registered_method=True)
        self.UploadVideo = channel.stream_unary(
                '/repo.RepoService/UploadVideo',
                request_serializer=repo__pb2.UploadVideoRequest.SerializeToString,
                response_deserializer=repo__pb2.VideoMetadataResponse.FromString,
                _registered_method=True)
        self.GetUserVideos = channel.unary_unary(
                '/repo.RepoService/GetUserVideos',
                request_serializer=repo__pb2.GetUserVideosRequest.SerializeToString,
                response_deserializer=repo__pb2.VideoListResponse.FromString,
                _registered_method=True)
        self.GetVideoByID = channel.unary_unary(
                '/repo.RepoService/GetVideoByID',
                request_serializer=repo__pb2.GetVideoRequest.SerializeToString,
                response_deserializer=repo__pb2.VideoMetadataResponse.FromString,
                _registered_method=True)
        self.DownloadVideo = channel.unary_stream(
                '/repo.RepoService/DownloadVideo',
                request_serializer=repo__pb2.DownloadVideoRequest.SerializeToString,
                response_deserializer=repo__pb2.VideoFileResponse.FromString,
                _registered_method=True)


class RepoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """User operations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadVideo(self, request_iterator, context):
        """Video operations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserVideos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVideoByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadVideo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RepoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=repo__pb2.CreateUserRequest.FromString,
                    response_serializer=repo__pb2.UserResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=repo__pb2.GetUserRequest.FromString,
                    response_serializer=repo__pb2.UserResponse.SerializeToString,
            ),
            'UploadVideo': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadVideo,
                    request_deserializer=repo__pb2.UploadVideoRequest.FromString,
                    response_serializer=repo__pb2.VideoMetadataResponse.SerializeToString,
            ),
            'GetUserVideos': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserVideos,
                    request_deserializer=repo__pb2.GetUserVideosRequest.FromString,
                    response_serializer=repo__pb2.VideoListResponse.SerializeToString,
            ),
            'GetVideoByID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVideoByID,
                    request_deserializer=repo__pb2.GetVideoRequest.FromString,
                    response_serializer=repo__pb2.VideoMetadataResponse.SerializeToString,
            ),
            'DownloadVideo': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadVideo,
                    request_deserializer=repo__pb2.DownloadVideoRequest.FromString,
                    response_serializer=repo__pb2.VideoFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'repo.RepoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('repo.RepoService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RepoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/repo.RepoService/CreateUser',
            repo__pb2.CreateUserRequest.SerializeToString,
            repo__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/repo.RepoService/GetUser',
            repo__pb2.GetUserRequest.SerializeToString,
            repo__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UploadVideo(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/repo.RepoService/UploadVideo',
            repo__pb2.UploadVideoRequest.SerializeToString,
            repo__pb2.VideoMetadataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUserVideos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/repo.RepoService/GetUserVideos',
            repo__pb2.GetUserVideosRequest.SerializeToString,
            repo__pb2.VideoListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetVideoByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/repo.RepoService/GetVideoByID',
            repo__pb2.GetVideoRequest.SerializeToString,
            repo__pb2.VideoMetadataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DownloadVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/repo.RepoService/DownloadVideo',
            repo__pb2.DownloadVideoRequest.SerializeToString,
            repo__pb2.VideoFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
