# server.py
from concurrent import futures
import grpc
import proto_pb2
import proto_pb2_grpc
from proto_pb2_grpc import ClocksServerServicer

class ClockSyncServicer(proto_pb2_grpc.ClocksServer):
    def RequestTimeDiff(self, request, context):
        # Lógica para retornar o tempo atual do servidor
        return proto_pb2.TimeDiffResponse(diff=123456789)

    def RequestTimeAjust(self, request, context):
        # Lógica para ajustar o tempo do servidor com base no tempo recebido do cliente
        return proto_pb2.TimeAjustResponse(status=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_pb2_grpc.add_ClocksServerServicer_to_server(ClockSyncServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
