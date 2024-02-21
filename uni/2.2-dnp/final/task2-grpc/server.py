from concurrent.futures import ThreadPoolExecutor

import grpc
import calculator_pb2
import calculator_pb2_grpc


SERVER_ADDR = '127.0.0.1:8081'


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.a + request.b

        print(f"Add: {request.a, request.b} = {result}")
        return calculator_pb2.AddResponse(result=result)

    def Subtract(self, request, context):
        result = request.a - request.b

        print(f"Subtract: {request.a, request.b} = {result}")
        return calculator_pb2.SubtractResponse(result=result)

    def Multiply(self, request, context):
        result = request.a * request.b

        print(f"Multiply: {request.a, request.b} = {result}")
        return calculator_pb2.MultiplyResponse(result=result)

    def Divide(self, request, context):
        if request.b == 0:
            result = float('nan')
        else:
            result = request.a / request.b

        print(f"Divide: {request.a, request.b} = {result}")
        return calculator_pb2.DivideResponse(result=result)


if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port(SERVER_ADDR)
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

    server.start()

    print(f"gRPC  is listening on: {SERVER_ADDR}")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)
        print("Shutting down...")

