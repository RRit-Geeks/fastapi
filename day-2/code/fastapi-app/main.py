from fastapi import FastAPI
app = FastAPI()

@app.get("/say-hello")
def say_hello():
    return "Hi! I am your first FastAPI Application"