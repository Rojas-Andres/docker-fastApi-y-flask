from fastapi import FastAPI 
import uvicorn

app = FastAPI()

@app.get('/')
def hello():
    return {"respuesta":"hola mundo"}

@app.get('/frutas')
def frutas():
    return {"respuesta":["pera","manzana"]}
