from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas.book import BookSchema, RequestBook, Response
from controllers.book import get_book, get_book_by_id, create_book, remove_book, update_book

book = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@book.post("/create")
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    create_book(db, book=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully").dict(exclude_none=True)

@book.get("/")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _books = get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_books)

@book.get("/{id}")
async def get_by_id(id=id, db: Session = Depends(get_db)):
    _book = get_book_by_id(db, id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_book)

@book.patch("/update")
async def update(request: RequestBook, db: Session = Depends(get_db)):
    _book = update_book(db, book_id=request.parameter.id,
                             title=request.parameter.title, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Success update data", result=_book)

@book.delete("/delete")
async def delete(request: RequestBook,  db: Session = Depends(get_db)):
    remove_book(db, book_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)