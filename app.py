from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    
    {
        "id": 1,
        "titulo": "O Diário de um Banana",
        "autor": "Jeff Kinney",
    },

    {
        "id": 2,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J. K. Rowling",
    },

    {
        "id": 3,
        "titulo": "Jurassic Park",
        "autor": "Michael Crichton",
    },
]

#consulta todos os livros

app.route('/livros')

def obter_livros():
    return jsonify(livros)

#consulta um livro pelo id
#Editar
#Deletar
app.run(port=5000, host='localhost', debug=True)