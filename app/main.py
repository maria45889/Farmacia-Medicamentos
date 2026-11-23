# app/main.py
from fastapi import FastAPI

app = FastAPI(title="API de Medicamnetos", version="1.0.0")


@app.get("/")
def raiz() -> dict:
    return {"api": "medicamentos", "nombre": "Cate"}
