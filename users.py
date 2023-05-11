from fastapi import FastAPI
from pydantic import BaseModel

#inciar el servidor con:  uvicorn users:app --reload 
# iniciar navegador con:  http://127.0.0.1:8000/users


app=FastAPI()

class User(BaseModel):
    id:int
    name:str
    surname:str
    email:str
    age:int


users_list = [User(id=1,name="Rodrigo",surname="Marin",email="rm@gmail.com",age=45),
              User(id=2,name="Gustavo",surname="Londoño",email="gl@gmail.com",age=28),
              User(id=3,name="Roberto",surname="Restrepo",email="rr@gmail.com",age=50)]


@app.get("/usersjson")
async def usersjson():
    return [{"name":"Roberto", "surname":"Restrepo","email":"rr@gmail.com", "age":35},
            {"name":"Rodrigo", "surname":"Marin","email":"rm@gmail.com", "age":45},
            {"name":"Gustavo", "surname":"Londoño","email":"gl@gmail.com","age":15}
        ]
    
@app.get("/users")
async def users():
    return users_list
    #return User(name="Rodrigo",surname="Marin",email="rm@gmail.com",age=45)
    
@app.get("/user/{id}")
async def user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    return list(users)[0] @app.get("/user/{id}")
async def user(id:int):
    return users_list    
