from sqlalchemy.orm import Session
from app import models, schemas
import uuid

def create_student(db: Session, student: schemas.StudentIn):
    db_student = models.Student(id=str(uuid.uuid4()), **student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_all_students(db: Session):
    return db.query(models.Student).all()

def get_student(db: Session, student_id: str):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def update_student(db: Session, student_id: str, student: schemas.StudentUpdate):
    db_student = get_student(db, student_id)
    if not db_student:
        return None

    # Only update fields if they are provided
    if student.name is not None:
        db_student.name = student.name
    if student.email is not None:
        db_student.email = student.email
    if student.status is not None:
        db_student.status = student.status

    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: str):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
