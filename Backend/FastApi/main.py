from fastapi import FastAPI #https://fastapi.tiangolo.com/

app = FastAPI()

@app.get("/")
async def root():
        return "Hola FastApi"
