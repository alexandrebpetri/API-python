
# 📚 Books API (CRUD) - Flask

This is a simple REST API developed in Python using Flask. It allows you to **retrieve**, **create**, **update**, and **delete** books from an in-memory list.

This project was created as a learning exercise, following the tutorial video: [Como CRIAR uma API com PYTHON [DO ZERO]](https://www.youtube.com/watch?v=FBLAV1SbJFk).

---

## 🚀 How to Run the Project

### Prerequisites:

- Python 3.x installed
- Flask installed (if not installed, run: `pip install flask`)

### Steps:

1. Save the API code in a file named `app.py`.

2. Run the server:

```bash
python app.py
```

3. The Flask server will start at:

```
http://localhost:5000
```

---

## 🛠️ Available Endpoints

### 🔍 Get all books

- **Method:** GET  
- **URL:** `/livros`

**Example Response:**
```json
[
  {
    "id": 1,
    "titulo": "O Diário de um Banana",
    "autor": "Jeff Kinney"
  },
  ...
]
```

---

### 🔍 Get book by ID

- **Method:** GET  
- **URL:** `/livros/<id>`

**Example:**
```
GET /livros/2
```

**Response:**
```json
{
  "id": 2,
  "titulo": "Harry Potter e a Pedra Filosofal",
  "autor": "J. K. Rowling"
}
```

---

### ➕ Create a new book

- **Method:** POST  
- **URL:** `/livros`  
- **Request Body (JSON):**
```json
{
  "id": 4,
  "titulo": "New Book",
  "autor": "Example Author"
}
```

**Response:** Updated list of books.

---

### ✏️ Update an existing book

- **Method:** PUT  
- **URL:** `/livros/<id>`  
- **Request Body (JSON):**
```json
{
  "titulo": "Updated Title",
  "autor": "Updated Author"
}
```

**Response:** Updated book.

---

### 🗑️ Delete a book

- **Method:** DELETE  
- **URL:** `/livros/<id>`

**Response:** List of books after deletion.

---

## ✅ Important Notes:

- This API **does not use a database**. Data is stored in a simple Python list in memory.
- If the server restarts, the book list will reset to its original state defined at the start of the code.

---

## 🎯 Project Purpose

This project was created for educational purposes to learn the basics of creating REST APIs using Python and Flask.

---

## 📖 Learning Sources:

- Tutorial video: [https://www.youtube.com/watch?v=FBLAV1SbJFk](https://www.youtube.com/watch?v=FBLAV1SbJFk)
- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

---
