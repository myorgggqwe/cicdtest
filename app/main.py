from fastapi import FastAPI

app = FastAPI()

b = 4


@app.get("/")
def read_root():
    return {"message": "bbb"}
