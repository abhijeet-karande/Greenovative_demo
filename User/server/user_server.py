from concurrent import futures
import grpc
from package.proto import user_pb2_grpc
from package.proto import emp_pb2_grpc
from controller.user_controller import UserController
from controller.emp_controller import empController
from package.db.connections import init_db

def serve():
    init_db()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserController(), server)
    emp_pb2_grpc.add_EmployeesServiceServicer_to_server(empController(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("server is running...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


