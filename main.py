from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models

app = FastAPI()

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

# Dependencia para usar la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Motor Delivery AI está activo 🚀"}

@app.post("/create-service")
def create_service(
    client_name: str,
    client_phone: str,
    origin: str,
    destination: str,
    db: Session = Depends(get_db)
):
    new_service = models.Service(
        client_name=client_name,
        client_phone=client_phone,
        origin=origin,
        destination=destination,
        status="pending",
        fare=0.0
    )

    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return {
        "message": "Servicio creado",
        "service_id": new_service.id
    }
