from sqlalchemy import Column, Integer, String, Float
from database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=True)
    client_phone = Column(String, nullable=False)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    status = Column(String, default="pending")
    fare = Column(Float, default=0.0)
