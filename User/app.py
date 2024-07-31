
from flask import Flask, request, jsonify
import grpc
import requests
from functools import wraps
from server.package.proto import user_pb2_grpc,user_pb2,emp_pb2,emp_pb2_grpc
app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        login_data = {
            "logid": request.headers.get("Logid"),
            "Password": request.headers.get("Password")
        }
        response = requests.post("http://127.0.0.1:5000/login", json=login_data)
        if response.status_code == 200:
            return f(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized"}), 401
    return decorated_function

@app.route('/login',methods=['POST'])
def login():
    data = request.json
    logid=data['logid'],
    Password=data['Password']
    if logid == 'valid_logid' and Password == 'valid_password':
        return jsonify('passkey:root12'), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
    

@app.route('/user',methods=['POST'])
@login_required
def create():
    data = request.json
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        
        response = stub.CreateUser(request= user_pb2.CreateUserRequest(id=data['id'], name=data['name'], address=data['address'], salary=data['salary'], login_id=data['login_id'], password=data['password']))
    # print(data)
    return jsonify({"result":response.result}),200

@app.route('/user/<int:uid>',methods=['GET'])
@login_required
def read(uid):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        response = stub.ReadUser(request = user_pb2.ReadUserRequest(id=uid))
        if response.result:
            return jsonify({
                "result":response.result
            }),200
    return jsonify("id not found"),404

@app.route('/user/<int:uid>',methods=['PUT'])
@login_required
def update(uid):
    data = request.json
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        response = stub.UpdateUser(request = user_pb2.UpdateUserRequest(id=uid, name=data['name'], address=data['address'], salary=data['salary'], login_id=data['login_id'], password=data['password']))
    
    return jsonify({"result":response.result}),200

@app.route('/user/<int:uid>',methods=['DELETE'])
@login_required
def delete(uid):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        response = stub.DeleteUser(request  = user_pb2.DeleteUserRequest(id=uid))
    return jsonify({"result":response.result}),200 





@app.route('/emp',methods=['POST'])
@login_required
def create_emp():
    data = request.json
    with grpc.insecure_channel('localhost:50051') as channel:
        stub=emp_pb2_grpc.EmployeesServiceStub(channel)
        response=stub.AddEmp(request =emp_pb2.AddRequest(id=data['id'],name=data['name'],city=data['city'],salary=data['salary']))
    return jsonify({"result":response.result}),200

@app.route('/emp/<int:eid>',methods=['GET'])
@login_required
def read_emp(eid):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub=emp_pb2_grpc.EmployeesServiceStub(channel)
        response=stub.ReadEmp(request =emp_pb2.ReadRequest(id=eid))
        if response.result:
            return jsonify({
                "result":response.result
            }),200
    return jsonify("id not found")

@app.route('/emp/<int:eid>',methods=['PUT'])
@login_required
def update_emp(eid):
    data = request.json
    with grpc.insecure_channel('localhost:50051') as channel:
        stub=emp_pb2_grpc.EmployeesServiceStub(channel)
        response=stub.UpdateEmp(request =emp_pb2.UpdateRequest(id=eid,name=data['name'],city=data['city'],salary=data['salary']))
    return jsonify({"result":response.result}),200

@app.route('/emp/<int:eid>',methods=['DELETE'])
@login_required
def delete_emp(eid):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub=emp_pb2_grpc.EmployeesServiceStub(channel)
        response=stub.DeleteEmp(request =emp_pb2.DeleteRequest(id=eid)) 
    return jsonify({"result":response.result}),200


if __name__ =="__main__":
    app.run(debug=True)