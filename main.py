from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.auth import hash_password, verify_password, create_access_token
from auth.dependencies import get_current_user

import models, schemas, crud
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print("In the users api")
    return crud.create_user(db, user)

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed = hash_password(user.password)

    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed,
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User created"}

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"user_id": db_user.id})

    return {"access_token": token}

@app.post("/products")
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return crud.create_product(db, product)
@app.post("/products")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@app.post("/cart/{user_id}/add")
def add_to_cart(user_id: int, item: schemas.CartItemCreate, db: Session = Depends(get_db)):
    return crud.add_to_cart(db, user_id, item)


@app.post("/checkout/{user_id}")
def checkout(user_id: int, db: Session = Depends(get_db)):
    return crud.checkout_cart(db, user_id)
