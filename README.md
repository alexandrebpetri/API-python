
#  Books API (CRUD) - Flask

This is a simple REST API developed in Python using Flask. It allows you to **create**, **read**, **update**, and **delete** books from an in-memory list.

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

# (🌍 PT-br) API de Livros (CRUD) - Flask

Esta é uma API REST simples desenvolvida em Python usando Flask. Ela permite  **criar**, **ler**, **atualizar** e **excluir** livros de uma lista na memória.

Este projeto foi criado como um exercício de aprendizado, seguindo o vídeo tutorial: [Como CRIAR uma API com PYTHON [DO ZERO]](https://www.youtube.com/watch?v=FBLAV1SbJFk).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos:

- Python 3.x instalado
- Flask instalado (se não estiver instalado, execute: `pip install flask`)

### Passos:

1. Salve o código da API em um arquivo chamado `app.py`.

2. Execute o servidor:

```bash
python app.py
```

3. O servidor Flask iniciará em:

```
http://localhost:5000
```

---

## 🛠️ Endpoints disponíveis

### 🔍 Obter todos os livros

- **Método:** GET
- **URL:** `/livros`

**Exemplo de resposta:**
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

### 🔍 Obter livro por ID

- **Método:** GET
- **URL:** `/livros/<id>`

**Exemplo:**
```
GET /livros/2
```

**Resposta:**
```json
{
"id": 2,
"titulo": "Harry Potter e a Pedra Filosofal",
"autor": "J. K. Rowling"
}
```

---

### ➕ Criar um novo livro

- **Método:** POST
- **URL:** `/livros`
- **Corpo de Requisição (JSON):**
```json
{
"id": 4,
"titulo": "Novo Livro",
"autor": "Exemplo de Autor"
}
```

**Resposta:** Lista de livros atualizada.

---

### ✏️ Atualizar um livro existente

- **Método:** PUT
- **URL:** `/livros/<id>`
- **Corpo de Requisição (JSON):**
```json
{
"titulo": "Título Atualizado",
"autor": "Autor Atualizado"
}
```

**Resposta:** Livro atualizado.

---

### 🗑️ Excluir um livro

- **Método:** DELETE
- **URL:** `/livros/<id>`

**Resposta:** Lista de livros após a exclusão.

---

## ✅ Observações Importantes:

- Esta API **não utiliza um banco de dados**. Os dados são armazenados em uma lista simples do Python na memória.
- Se o servidor for reiniciado, a lista de livros retornará ao seu estado original definido no início do código.

---

## 🎯 Objetivo do Projeto

Este projeto foi criado com fins educacionais para aprender os conceitos básicos da criação de APIs REST usando Python e Flask.

---

## 📖 Fontes de Aprendizado:

- Vídeo tutorial: [https://www.youtube.com/watch?v=FBLAV1SbJFk](https://www.youtube.com/watch?v=FBLAV1SbJFk)
- Documentação do Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

---