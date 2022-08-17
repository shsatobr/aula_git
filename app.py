from flask import Flask, render_template
from datetime import datetime
app = Flask("hello")

posts = [
    {
        "title": "Meu primeiro posts",
        "body": "Esse post é o primeiro do blog",
        "author": "Danilo de souza Miguel",
        "created": datetime(2022,8,17)
    },
    {
        "title": "Meu segundo posts",
        "body": "Esse post é o segundo do blog",
        "author": "Raiane Caroline",
        "created": datetime(2022,8,17)
    },
    {
        "title": "Meu terceiro posts",
        "body": "Esse post é o terceiro do blog",
        "author": "Jezimiel Marcondes",
        "created": datetime(2022,8,17)
    },
]

@app.route("/")
def index():
    return render_template("index.html",posts=posts)

# def usuario():
#     usuario = [1, "Danilo de Souza", "Professor"]
#     alunos  = ["Andre Guedes", "Lucas Santos", "Alicia Duarte", "Raiane Caroline"]
#     return render_template("index.html", usuario = usuario, alunos=alunos)

# @app.route("/contato")
# def contato():
#     nomeAula = "Aula Python para Web"
#     return render_template("index.html", nome = nomeAula, usuario = usuario)