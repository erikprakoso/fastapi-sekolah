from fastapi import FastAPI
from models.book import Book
from routes.book import book
from models.teacher import Teacher
from routes.teacher import teacher
from config import engine

Book.metadata.create_all(bind=engine)
Teacher.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book, prefix="/book", tags=["book"])
app.include_router(teacher, prefix="/teacher", tags=["teacher"])