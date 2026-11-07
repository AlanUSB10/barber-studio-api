from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inico():
    return {"mensjae": "Bienvenido a Barber Studio API"}