from flask import Flask #Biblioteca
from flask import render_template
from flask import request

app = Flask(__name__) #Carregamento

@app.route("/") #Rota
def index(): #Função
    return "<h1>Olá<br>Mundo!</h1>"

@app.route("/aluno/<nome>")
def aluno(nome):
    return render_template("formulario.html")

@app.route("/envio", methods=["POST"])
def envioForms():
    nombre = request.form["nome"]
    senha = request.form["senha"]
    if senha == "123":
        return render_template("aluno.html", n=nombre)
    else:
        return "DEU ERRADO, SEU CUZÃO!"
