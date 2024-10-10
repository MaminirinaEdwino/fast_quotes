from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def teste_function():
    return {"msg" : "api ok"}