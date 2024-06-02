from fastapi import FastAPI, Depends, HTTPException
import models
from sqlalchemy.orm import Session
from sqlalchemy import desc
from database import SessionLocal, engine, Base, get_db
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated, ClassVar, List
from schemas import input

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["http://localhost:*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_dependency = Annotated[Session, Depends(get_db())]
