from package.proto import user_pb2_grpc, user_pb2
from service.user_service import UserService
from package.db.connections import SessionLocal
import grpc
class UserController(user_pb2_grpc.UserServiceServicer):
    def __init__(self):
        self.service = UserService()

    def CreateUser(self, request, context):
        db = SessionLocal()
        result, error = self.service.create_user(db,request)
        return user_pb2.UserResponse(result=result, error=error)

    def ReadUser(self, request, context):
        db = SessionLocal()
        result, error = self.service.read_user(db,request)
        return user_pb2.UserResponse(result=result, error=error)

    def UpdateUser(self, request, context):
        db = SessionLocal() 
        result, error = self.service.update_user(db,request)
        return user_pb2.UserResponse(result=result, error=error)

    def DeleteUser(self, request, context):
        db = SessionLocal() 
        result, error = self.service.delete_user(db,request)
        return user_pb2.UserResponse(result=result, error=error)
    
    def ReadAll(self, request, context):
        db = SessionLocal() 
        try:
            users= self.service.readAll_user(db,request)
            users_list = [user_pb2.User(
                    id=user.id,
                    name=user.name,
                    address=user.address,
                    salary=user.salary,
                    login_id=user.login_id,
                    password=user.password
                ) for user in users]
            return user_pb2.ReadAllResponse(users=users_list)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return user_pb2.UsersListResponse(users=[])
        finally:
            db.close()
