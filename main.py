from fastapi import FastAPI  

app = FastAPI()  

@app.get("/info")
def get_info():
    return {
        "name": "FastAPI Microservice",
        "version": "1.0",
        "author": "Nicol valeria Ocampo Bernal",
        "language": "Python",
        "framework": "FastAPI"
    }

