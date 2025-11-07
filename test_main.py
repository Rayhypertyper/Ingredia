from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World - Test App"}

@app.get("/health")
def health():
    return {"status": "healthy"}