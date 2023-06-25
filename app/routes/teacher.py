from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas.teacher import TeacherSchema, RequestTeacher, Response
from controllers.teacher import get_teacher, get_teacher_by_id, create_teacher, remove_teacher, update_teacher

teacher = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@teacher.post("/create")
async def create_teacher_service(request: RequestTeacher, db: Session = Depends(get_db)):
    create_teacher(db, teacher=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Teacher created successfully").dict(exclude_none=True)


@teacher.get("/")
async def get_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _teachers = get_teacher(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_teachers)


@teacher.get("/{id}")
async def get_by_id(id=id, db: Session = Depends(get_db)):
    _teacher = get_teacher_by_id(db, id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_teacher)


@teacher.patch("/update")
async def update(request: RequestTeacher, db: Session = Depends(get_db)):
    _teacher = update_teacher(db, 
                              teacher_id=request.parameter.id,
                              name=request.parameter.name, 
                              subject=request.parameter.subject, 
                              email=request.parameter.email)
    return Response(status="Ok", code="200", message="Success update data", result=_teacher)


@teacher.delete("/delete")
async def delete(request: RequestTeacher,  db: Session = Depends(get_db)):
    remove_teacher(db, teacher_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
