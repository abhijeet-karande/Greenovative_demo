
from package.models.emp_model import Emp
from sqlalchemy.orm import Session
import redis
import json
class empService():
    def __init__(self) :
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0,password='abc')


    def add_emp(self,db:Session,request):

        if db.query(Emp).filter(Emp.id == request.id).first():
            return f"employe with {request.id} already exists"
        emp = Emp(
             id=request.id,
             name=request.name,
             city=request.city,
             salary=request.salary
             )
        db.add(emp)
        db.commit()
        db.refresh(emp)
        self.redis_client.set(f"user:{emp.id}", json.dumps(self._user_to_dict(emp)))

        return f"Info of employee {request.id} is added"
        
    def read_emp(self,db:Session,request):
        cached_user = self.redis_client.get(f"user:{request.id}")
        if cached_user:
            emp = json.loads(cached_user)
            info=f"employee info= id={emp['id']} ,name={emp['name']} ,city={emp['city']} ,salary={emp['salary']}"
            return info 
        
        emp=db.query(Emp).filter(Emp.id==request.id).first()
        if not emp:
            return f"Info of employee {request.id} is not found"
        info=f"id={emp.id} ,name={emp.name} ,city={emp.city} ,salary={emp.salary}"
        return info  
    
    def update_emp(self,db:Session,request):
        emp=db.query(Emp).filter(Emp.id==request.id).first()
        if not emp:
            return f"Info of employee {request.id} is not found"
        emp.name=request.name
        emp.city=request.city
        emp.salary=request.salary
        db.commit()
        self.redis_client.set(f"employee: {emp.id}",json.dumps(self._user_to_dict(emp)))
        return f"Info of employee {request.id} is updated"
    
    def delete_emp(self,db:Session,request):
        emp=db.query(Emp).filter(Emp.id==request.id).first()
        if not emp:
            return f"Info of employee {request.id} is not found"
        db.delete(emp)
        db.commit()
        self.redis_client.delete(f"employee with id{emp.id} is deleted ")
        return f"Info of employee {request.id} is deleted"
    
    def _user_to_dict(self, emp):
        return {
            "id": emp.id,
            "name": emp.name,
            "city": emp.city,
            "salary": emp.salary,
        
        }