# FastAPI REST API - Starter Code
# This starter code provides the basic structure for building a REST API with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create FastAPI app instance
app = FastAPI(title="Book Management API", version="1.0.0")

# Define the Book model using Pydantic
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    genre: str

# In-memory storage for books (using a list)
books = [
    Book(id=1, title="To Kill a Mockingbird", author="Harper Lee", year=1960, genre="Fiction"),
    Book(id=2, title="1984", author="George Orwell", year=1949, genre="Science Fiction"),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925, genre="Fiction"),
]

# TODO: Implement the root endpoint
# This should return a welcome message
@app.get("/")
def root():
    pass
    # Your code here


# TODO: Implement GET /books endpoint
# This should return all books (or filtered books based on query parameters)
# Add optional query parameters for filtering by author and/or genre


# TODO: Implement GET /books/{book_id} endpoint
# This should return a specific book by ID
# Raise HTTPException with status_code=404 if book is not found


# TODO: Implement POST /books endpoint
# This should add a new book to the collection
# Make sure to generate a unique ID for the new book


# TODO: Implement PUT /books/{book_id} endpoint
# This should update an existing book
# Raise HTTPException with status_code=404 if book is not found


# TODO: Implement DELETE /books/{book_id} endpoint
# This should remove a book from the collection
# Raise HTTPException with status_code=404 if book is not found


# To run this application, use the following command in your terminal:
# uvicorn starter-code:app --reload
#
# Then visit:
# - http://localhost:8000 for the API
# - http://localhost:8000/docs for interactive API documentation
