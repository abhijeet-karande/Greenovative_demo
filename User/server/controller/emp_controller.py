from package.proto import emp_pb2,emp_pb2_grpc
from service.emp_service import empService
from package.db.connections import SessionLocal
import grpc

class empController(emp_pb2_grpc.EmployeesServiceServicer):
    def __init__(self) :
        self.service= empService()

    def AddEmp(self, request, context):
        db=SessionLocal()
        result=self.service.add_emp(db,request)
        return emp_pb2.AddResponse(result=result)
    
    def ReadEmp(self, request, context):
        db=SessionLocal()
        result=self.service.read_emp(db,request)
        return emp_pb2.ReadResponse(result=result)
    
    def UpdateEmp(self, request, context):
        db=SessionLocal()
        result=self.service.update_emp(db,request)
        return emp_pb2.UpdateResponse(result=result)
    
    def DeleteEmp(self, request, context):
        db=SessionLocal()
        result=self.service.delete_emp(db,request)
        return emp_pb2.DeleteResponse(result=result)
