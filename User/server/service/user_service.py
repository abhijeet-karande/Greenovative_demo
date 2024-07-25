from package.models.user_model import User
from sqlalchemy.orm import Session
from package.proto import user_pb2
import redis
import json
class UserService:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0,password='abc')


    def create_user(self,db:Session, request):
        if db.query(User).filter(User.id == request.id).first():
            return "", f"User with id {request.id} already exists."

        user = User(
            id=request.id,
            name=request.name,
            address=request.address,
            salary=request.salary,
            login_id=request.login_id,
            password=request.password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        self.redis_client.set(f"user:{user.id}", json.dumps(self._user_to_dict(user)))
        return f"User {request.name} created successfully.", ""
    
    def read_user(self, db: Session, request):
        cached_user = self.redis_client.get(f"user:{request.id}")
        if cached_user:
            user = json.loads(cached_user)
            user_details = f"User details: id={user['id']}, name={user['name']}, address={user['address']}, salary={user['salary']}, login_id={user['login_id']}"
            return user_details, ""
        
        user = db.query(User).filter(User.id == request.id).first()
        if not user:
            return "", f"User with id {request.id} not found."
        
        self.redis_client.set(f"user:{user.id}", json.dumps(self._user_to_dict(user)))
        user_details = f"User details: id={user.id}, name={user.name}, address={user.address}, salary={user.salary}, login_id={user.login_id}"
        return user_details, ""

    def update_user(self, db: Session, request):
        user = db.query(User).filter(User.id == request.id).first()
        if not user:
            return "", f"User with id {request.id} not found."
        
        user.name = request.name
        user.address = request.address
        user.salary = request.salary
        user.login_id = request.login_id
        user.password = request.password
        db.commit()
        self.redis_client.set(f"user:{user.id}", json.dumps(self._user_to_dict(user)))
        return f"User {request.name} updated successfully.", ""

    def delete_user(self, db: Session, request):
        user = db.query(User).filter(User.id == request.id).first()
        if not user:
            return "", f"User with id {request.id} not found."
        
        db.delete(user)
        db.commit()
        self.redis_client.delete(f"user:{user.id}")
        return f"User with id {request.id} deleted successfully.", ""
    
    def readAll_user(self,db:Session,request):
        users = db.query(User).all()
        return users
    
    def _user_to_dict(self, user):
        return {
            "id": user.id,
            "name": user.name,
            "address": user.address,
            "salary": user.salary,
            "login_id": user.login_id,
            "password": user.password
        }