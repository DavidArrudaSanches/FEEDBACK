from hashlib import sha256
import mysql.connector
from data.conexao import Conexao
class Usuario:
    
    def cadastrar(login, senha, nome):

        senha=sha256(senha.encode()).hexdigest()
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
    def login(login,senha):

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """SELECT * FROM tb_usuarios
                    WHERE login = %s
                    and binary senha = %s"""

        valores = (login,senha)

        cursor.execute(sql)

        resultado = cursor.fetchone

