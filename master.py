# client.py
import grpc
import proto_pb2
import proto_pb2_grpc
import random

ports = ["50051", "50052", "50053"]
my_port = "50051"
time = random.randint(1,52)
times = []
ajust = 0
def request_time():
    for port in ports:
        if(port == my_port):
            times.append(0)
            continue
        with grpc.insecure_channel('localhost:'+port) as channel:
            stub = proto_pb2_grpc.ClocksServerStub(channel)
            response = stub.RequestTimeDiff(proto_pb2.TimeDiffRequest(time=time))
            times.append(response.diff)
            print(f"Diferença de Tempo para o servidor: {response.diff}")

def adjust_time():
    global time
    ajust = (sum(times)) // len(times)
    old_time = time
    time += ajust
    for index, port in enumerate(ports):
        if(port == my_port):
            print("Hora atual: "+str(time))
            continue
        new_ajust = time - (old_time+times[index])
        with grpc.insecure_channel('localhost:'+port) as channel:
            stub = proto_pb2_grpc.ClocksServerStub(channel)
            response = stub.RequestTimeAjust(proto_pb2.TimeAjustRequest(ajust=new_ajust))
            if response.status:
                print("Tempo ajustado com sucesso!")

if __name__ == '__main__':
    print("Hora do servidor: "+str(time))
    request_time()
    adjust_time()
