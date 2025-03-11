import datetime
import mysql.connector
from data.conexao import Conexao

class Mensagem:
    def cadastrar_mensagem(usuario,mensagem):
        data_hora= datetime.datetime.today()

        conex = Conexao.criar_conexao()

        cursor = conex.cursor()

        sql = """INSERT INTO tb_comentarios 
                        (nome, data_hora, comentario)
                    VALUES
                        (%s, %s, %s)"""

        valores = (usuario, data_hora, mensagem)

        cursor.execute(sql,valores)


        conex.commit()

        cursor.close()
        conex.close()
        
    def recuperar_mensagens():
        conexao=Conexao.criar_conexao()

        cursor= conexao.cursor(dictionary=True)

        sql="""Select nome as usuario,
                comentario as mensagem, data_hora from tb_comentarios"""
        
        cursor.execute(sql)

        resultado=cursor.fetchall()
        
        conexao.close()

        return resultado
    
    