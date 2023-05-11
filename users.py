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
    
@app.get("/users")
async def users():
    return users_list
    #return User(name="Rodrigo",surname="Marin",email="rm@gmail.com",age=45)
    
# iniciar navegador con:  http://127.0.0.1:8000/users

@app.get("/user/{id}")
async def user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]  
    except:
        return {"error":"No se ha encontrado el usuario"}
# iniciar navegador con:  http://127.0.0.1:8000/user/1    


@app.get("/username/")
async def username(name:str):
    users = filter(lambda user: user.name == name, users_list)
    try:
        return list(users)[0]  
    except:
        return {"error":"No se ha encontrado el usuario"}
# iniciar navegador con:  http://127.0.0.1:8000/username/?name=Roberto   
    
@app.get("/user/")
async def user(id:int):
    return search_user(id)
    
    # iniciar navegador con:  http://127.0.0.1:8000/userquery/?id=1
   
    # iniciar navegador con:  http://127.0.0.1:8000/username/?name=roberto   


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]  
    except:
        return {"error":"No se ha encontrado el usuario"}   
    # iniciar navegador con:  http://127.0.0.1:8000/userquery/?id=1
