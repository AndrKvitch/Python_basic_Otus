from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get('/')
def ping():
    data = {"message": "pong"}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)


