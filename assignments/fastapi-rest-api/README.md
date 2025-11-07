# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will learn how to build RESTful APIs using FastAPI, a modern and fast Python web framework. You'll create a simple API to manage a collection of books, implementing CRUD (Create, Read, Update, Delete) operations and learning about HTTP methods, status codes, and API design principles.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a basic FastAPI application with a root endpoint that returns a welcome message. Learn how to run the FastAPI development server and explore the automatic interactive API documentation.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a root endpoint (`/`) that returns a welcome message
- Run successfully using `uvicorn` server
- Display automatic API documentation at `/docs`


### 🛠️ Implement Book Management Endpoints

#### Description
Create a complete REST API for managing a book collection. Implement endpoints to create, read, update, and delete books. Each book should have an ID, title, author, year of publication, and genre.

#### Requirements
Completed program should:

- Define a Book model using Pydantic with fields: id, title, author, year, and genre
- Implement GET `/books` endpoint to retrieve all books
- Implement GET `/books/{book_id}` endpoint to retrieve a specific book
- Implement POST `/books` endpoint to add a new book
- Implement PUT `/books/{book_id}` endpoint to update an existing book
- Implement DELETE `/books/{book_id}` endpoint to remove a book
- Use appropriate HTTP status codes (200, 201, 404, etc.)
- Handle errors gracefully (e.g., book not found)
- Store books in memory using a Python list or dictionary


### 🛠️ Add Query Parameters and Filtering

#### Description
Enhance your API by adding the ability to filter books using query parameters. Allow users to search for books by author or genre.

#### Requirements
Completed program should:

- Add optional query parameters to the GET `/books` endpoint
- Filter books by author when `author` parameter is provided
- Filter books by genre when `genre` parameter is provided
- Support filtering by both parameters simultaneously
- Return an empty list if no books match the criteria
- Test filtering using the interactive API documentation
