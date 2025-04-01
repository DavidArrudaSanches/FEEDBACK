from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.control_mensagem import Mensagem
from model.control_usuario import Usuario

app= Flask(__name__)

@app.route("/pagina-mensg")
def pagina_principal():
    mensagem = Mensagem.recuperar_mensagens()
   
    return render_template ("index.html", mensagem=mensagem)

@app.route("/post/mensagem", methods=["POST"])
def post_mensagem():

    usuario= request.form.get("nome_user")
    mensagem = request.form.get("comentario")
    
    Mensagem.cadastrar_mensagem(usuario,mensagem)

    return redirect("/pagina-mensg")

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/pagina-mensg")

@app.route("/put/mensagem/adicionar/curtida/<codigo>")
def adicionar_curtida(codigo):
    Mensagem.like_mensg(codigo)
    return redirect("/pagina-mensg") 

@app.route("/put/mensagem/remover/curtida/<codigo>")
def remover_curtida(codigo):
    Mensagem.unlike_mensg(codigo)
    return redirect("/pagina-mensg")


@app.route("/")
def pagina_cadastro():
    return render_template("paginainicial.html")

@app.route("/cadastro", methods=["POST"])
def cadastro_user():
    login= request.form.get("login_user")
    nome = request.form.get("name_user")
    senha= request.form.get("senha")

    Usuario.cadastrar(login,senha,nome)

    return redirect("/pagina-mensg")


app.run(debug=True)