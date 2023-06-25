from sqlalchemy.orm import Session
from models.teacher import Teacher
from schemas.teacher import TeacherSchema


def get_teacher(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Teacher).offset(skip).limit(limit).all()


def get_teacher_by_id(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()


def create_teacher(db: Session, teacher: TeacherSchema):
    _teacher = Teacher(name=teacher.name,
                       subject=teacher.subject, email=teacher.email)
    db.add(_teacher)
    db.commit()
    db.refresh(_teacher)
    return _teacher


def remove_teacher(db: Session, teacher_id: int):
    _teacher = get_teacher_by_id(db=db, teacher_id=teacher_id)
    db.delete(_teacher)
    db.commit()


def update_teacher(db: Session, teacher_id: int, name: str, subject: str, email: str):
    _teacher = get_teacher_by_id(db=db, teacher_id=teacher_id)
    _teacher.name = name
    _teacher.subject = subject
    _teacher.email = email
    db.commit()
    db.refresh(_teacher)
    return _teacher
