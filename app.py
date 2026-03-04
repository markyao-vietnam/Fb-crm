from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

DATABASE_URL = "sqlite:///./test.db"

Base = declarative_base()

# Database initialization
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy models
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

Base.metadata.create_all(bind=engine)

# Pydantic schemas
class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str

class CustomerUpdate(BaseModel):
    name: str = None
    email: str = None
    phone: str = None

class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str

    class Config:
        orm_mode = True

# FastAPI application
app = FastAPI()

# Dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations
@app.post("/customers/", response_model=Customer)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = Customer(name=customer.name, email=customer.email, phone=customer.phone)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customers/{customer_id}", response_model=Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@app.put("/customers/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    if customer.name:
        db_customer.name = customer.name
    if customer.email:
        db_customer.email = customer.email
    if customer.phone:
        db_customer.phone = customer.phone
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()
    return {"detail": "Customer deleted"}

# Facebook integration endpoints
@app.get("/facebook_integration/track_customer/{customer_id}")
def track_customer(customer_id: int):
    # Placeholder for Facebook API integration logic
    return {"message": "Customer tracking initiated for Facebook", "customer_id": customer_id}
