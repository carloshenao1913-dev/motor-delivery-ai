from fastapi import FastAPI, Request
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Motor Delivery AI está activo 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}
