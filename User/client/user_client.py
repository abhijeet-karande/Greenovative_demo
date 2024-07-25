import grpc
import user_pb2_grpc, user_pb2
import emp_pb2_grpc,emp_pb2

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)

        while True:
            print("1: Create User")
            print("2: Read User")
            print("3: Update User")
            print("4: Delete User")
            print("5: ReadAll User")
            print("6: Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                id = int(input("Enter id: "))
                name = input("Enter name: ")
                address = input("Enter address: ")
                salary = int(input("Enter salary: "))
                login_id = input("Enter login_id: ")
                password = input("Enter password: ")
                request = user_pb2.CreateUserRequest(id=id, name=name, address=address, salary=salary, login_id=login_id, password=password)
                response = stub.CreateUser(request)
            elif choice == "2":
                id = int(input("Enter id: "))
                request = user_pb2.ReadUserRequest(id=id)
                response = stub.ReadUser(request)
            elif choice == "3":
                id = int(input("Enter id: "))
                name = input("Enter name: ")
                address = input("Enter address: ")
                salary = int(input("Enter salary: "))
                login_id = input("Enter login_id: ")
                password = input("Enter password: ")
                request = user_pb2.UpdateUserRequest(id=id, name=name, address=address, salary=salary, login_id=login_id, password=password)
                response = stub.UpdateUser(request)
            elif choice == "4":
                id = int(input("Enter id: "))
                request = user_pb2.DeleteUserRequest(id=id)
                response = stub.DeleteUser(request)
            elif choice == "5":
                request = user_pb2.ReadAllRequest()
                response = stub.ReadAll(request)
                for user in response.users:
                    print(f"User ID: {user.id}, Name: {user.name}, Address: {user.address}, Salary: {user.salary}, Login ID: {user.login_id}")   
            elif choice == "6":
                break
            else:
                print("Invalid choice!")
                continue

            print(f"Result: {response.result}")
            if response.error:
                print(f"Error: {response.error}")


        stub=emp_pb2_grpc.EmployeesServiceStub(channel)

        while True:
            print("1 :Add Employee")
            print("2 :Read Employee")
            print("3 :Update Employee")
            print("4 :Delete Employee")
            print("5 :Exit")
            choise = input("choose the operation :")

            if choise =="1":
                id=int(input("Enter id:"))
                name=input("Enter name:")
                city=input("Enter city:")
                salary=int(input("Enter salary:"))

                request=emp_pb2.AddRequest(id=id,name=name,city=city,salary=salary)
                response=stub.AddEmp(request)

            elif choise=="2":
                id=int(input("enter id:"))
                
                request=emp_pb2.ReadRequest(id=id)
                response=stub.ReadEmp(request)

            elif choise=="3":
                id=int(input("enter id:"))
                name=input("Enter name:")
                city=input("Enter city:")
                salary=int(input("Enter salary:"))
                request=emp_pb2.UpdateRequest(id=id,name=name,city=city,salary=salary)
                response=stub.UpdateEmp(request) 
            elif choise=="4":
                id=int(input("enter id:"))
                request=emp_pb2.DeleteRequest(id=id)
                response=stub.DeleteEmp(request)  
            elif choise=="5":
                break       
            else:
                print("Invalid choice!")
                continue 
            
            print(f"Result: {response.result}")
        

if __name__ == '__main__':
    run()
