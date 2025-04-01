import mysql.connector
from data.conexao import Conexao

class Usuario:
    
    def cadastrar(login, senha, nome):

        conex = Conexao.criar_conexao()

        cursor = conex.cursor()

        sql = """INSERT INTO tb_usuarios 
                        (login, senha, nome)
                    VALUES
                        (%s, %s, %s)"""

        valores = (login, senha, nome)

        cursor.execute(sql,valores)


        conex.commit()

        cursor.close()
        conex.close()