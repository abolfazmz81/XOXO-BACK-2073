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


@app.post("/scores")
async def update_score(json: List[input], db: Session = Depends(get_db)):
    user1 = json[0]
    user2 = json[1]
    dt1 = db.query(models.Scores).filter(models.Scores.name == json[0].name).first()
    dt2 = db.query(models.Scores).filter(models.Scores.name == user2.name).first()
    if not dt1:
        if json[0].status == "WIN":
            db_user1 = models.Scores(score=1, name=user1.name)
        else:
            db_user1 = models.Scores(score=-1, name=user1.name)
        db.add(db_user1)
        db.commit()
        db.refresh(db_user1)
    else:
        if json[0].status == "WIN":
            dt1.score = dt1.score + 1
            db.commit()
            db.refresh(dt1)
        else:
            dt1.score = dt1.score - 1
            db.commit()
            db.refresh(dt1)

    if not dt2:
        if json[1].status == "Win":
            db_user2 = models.Scores(score=1, name=user2.name)
        else:
            db_user2 = models.Scores(score=-1, name=user2.name)
        db.add(db_user2)
        db.commit()
        db.refresh(db_user2)
    else:
        if json[1].status == "Win":
            dt2.score = dt2.score + 1
            db.commit()
            db.refresh(dt2)
        else:
            dt2.score = dt2.score - 1
            db.commit()
            db.refresh(dt2)
    return "ok"
