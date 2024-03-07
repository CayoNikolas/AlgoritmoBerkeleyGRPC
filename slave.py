# server.py
from concurrent import futures
import grpc
import proto_pb2
import proto_pb2_grpc
from proto_pb2_grpc import ClocksServerServicer
import random
import threading
import sys


time = random.randint(1,52)
class ClockSyncServicer(proto_pb2_grpc.ClocksServer):
    def RequestTimeDiff(self, request, context):
        diff = time - request.time
        return proto_pb2.TimeDiffResponse(diff=diff)

    def RequestTimeAjust(self, request, context):
        global time
        time +=request.ajust
        print("Hora atual: "+str(time))
        return proto_pb2.TimeAjustResponse(status=True)

def serve(port:str):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    proto_pb2_grpc.add_ClocksServerServicer_to_server(ClockSyncServicer(), server)
    server.add_insecure_port('[::]:'+port)
    server.start()
    print("Servidor rodando na porta: "+port)
    print("Hora atual: "+str(time))
    server.wait_for_termination()

if __name__ == '__main__':
    args = sys.argv[1:]   
    serve(args[0])
