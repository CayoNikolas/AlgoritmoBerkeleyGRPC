# client.py
import grpc
import proto_pb2
import proto_pb2_grpc

def request_time():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = proto_pb2_grpc.ClocksServerStub(channel)
        response = stub.RequestTimeDiff(proto_pb2.TimeDiffRequest())
        print(f"Tempo do servidor: {response.diff}")

def adjust_time():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = proto_pb2_grpc.ClocksServerStub(channel)
        # Lógica para calcular a diferença e ajustar o tempo
        response = stub.RequestTimeAjust(proto_pb2.TimeAjustRequest())
        if response.status:
            print("Tempo ajustado com sucesso!")

if __name__ == '__main__':
    request_time()
    adjust_time()
