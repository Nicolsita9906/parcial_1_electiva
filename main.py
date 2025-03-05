from fastapi import FastAPI  

app = FastAPI()  
@app.get("/")
def read_root():
    return {"message": "Hola, FastAPI está funcionando"}
   

@app.get("/info")
def get_info():
    return {
        "name": "FastAPI Microservice",
        "version": "1.0",
        "author": "Nicol valeria Ocampo Bernal",
        "language": "Python",
        "framework": "FastAPI"
    }

