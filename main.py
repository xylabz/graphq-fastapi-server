from fastapi import FastAPI
from graphene import ObjectType, String, Schema

class User(ObjectType):
    name = String()
    email = String()

class Query(ObjectType):
    me = User(name="John Doe", email="john.doe@example.com")

schema = Schema(query=Query)

app = FastAPI()

@app.get('/')
async def graphql(query: str):
    result = schema.execute(query)
    return {'data': result.data}

@app.get('/status')
async def status():
    return {'status': 'Ok'}