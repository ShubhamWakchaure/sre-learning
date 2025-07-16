print("✅ students.py router loaded")

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db import get_db
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/students",
    tags=["students"]
)

@router.post("/", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentIn, db: Session = Depends(get_db)):
    logger.info('Creatng the student.')
    return crud.create_student(db, student)

@router.get("/", response_model=list[schemas.StudentOut])
def get_all_students(db: Session = Depends(get_db)):
    logger.info('Fetchng all students.')
    return crud.get_all_students(db)

@router.get("/{student_id}", response_model=schemas.StudentOut)
def get_student(student_id: str, db: Session = Depends(get_db)):
    logger.info('Going to get the students details')
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=schemas.StudentOut)
def update_student(student_id: str, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, student)

@router.delete("/{student_id}")
def delete_student(student_id: str, db: Session = Depends(get_db)):
    logger.info('Going to delete the student.')
    crud.delete_student(db, student_id)
    return {"message": "Student deleted"}
