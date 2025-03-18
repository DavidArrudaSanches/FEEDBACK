from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.control_mensagem import Mensagem
app= Flask(__name__)

@app.route("/")
def pagina_principal():
    mensagem = Mensagem.recuperar_mensagens()
   
    return render_template ("index.html", mensagem=mensagem)

@app.route("/post/mensagem", methods=["POST"])
def post_mensagem():

    usuario= request.form.get("nome_user")
    mensagem = request.form.get("comentario")
    
    Mensagem.cadastrar_mensagem(usuario,mensagem)

    return redirect("/")

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/")

@app.route("/put/mensagem/adicionar/curtida/<codigo>")
def adicionar_curtida(codigo):
    return redirect("/") 



app.run(debug=True)