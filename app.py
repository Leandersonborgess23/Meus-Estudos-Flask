from flask import Flask #Biblioteca

app = Flask(__name__) #Carregamento

@app.route("/") #Rota
def index(): #Função
    return "<h1>Olá<br>Mundo!</h1>"

@app.route("/aluno/<nome>")
def aluno(nome):
    return f"<h1>Meu nome é {nome}</h1>"