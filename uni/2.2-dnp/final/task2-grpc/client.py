import grpc
import calculator_pb2
import calculator_pb2_grpc

SERVER_ADDR = '127.0.0.1:8081'


if __name__ == '__main__':
    with grpc.insecure_channel(SERVER_ADDR) as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        response = stub.Add(calculator_pb2.AddRequest(a=10, b=2))
        print(f"Add(10, 2) = {response.result}")

        response = stub.Subtract(calculator_pb2.SubtractRequest(a=10, b=2))
        print(f"Subtract(10, 2) = {response.result}")

        response = stub.Multiply(calculator_pb2.MultiplyRequest(a=10, b=2))
        print(f"Multiply(10, 2) = {response.result}")

        response = stub.Divide(calculator_pb2.DivideRequest(a=10, b=2))
        print(f"Divide(10, 2) = {response.result}")

        response = stub.Divide(calculator_pb2.DivideRequest(a=10, b=0))
        print(f"Divide(10, 0) = {response.result}")
