from flask import Flask, render_template, form, request
import datetime
import mysql.connector

app= Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template ("index.html")

app.route("/post/mensagem", methods=["POST"])
def post_mensagem():

    usuario= request.form.get("nome_user")
    mensagem = request.form.get("mensagem")
    data_hora= datetime.datetime.today()

    conexao= mysql.connector.connect(   host="localhost",
                                        port=3306,
                                        user = "root",
                                        password = "root",
                                        database = "db_feedback"
                                    )

    cursor = conexao.cursor()

    sql = """INSERT INTO tb_comentarios 
                    (nome, data_hora, comentario)
                VALUES
                    (%s, $s, $s)"""

    valores = (usuario, data_hora, mensagem)

    cursor.execute(sql,valores)


    conexao.commit()

    cursor.close()
    conexao.close()

app.run(debug=True)