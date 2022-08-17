from flask import Flask, render_template

app = Flask("hello")

@app.route("/")
def usuario():
    usuario = [1, "Danilo de Souza", "Professor"]
    alunos  = ["Andre Guedes", "Lucas Santos", "Alicia Duarte", "Raiane Caroline"]
    return render_template("index.html", usuario = usuario, alunos=alunos)

@app.route("/contato")
def contato():
    nomeAula = "Aula Python para Web"
    return render_template("index.html", nome = nomeAula, usuario = usuario)