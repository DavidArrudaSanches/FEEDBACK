from hashlib import sha256
import mysql.connector
from data.conexao import Conexao
from flask import session
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


    def validar_login(login, senha):
        
        senha=sha256(senha.encode()).hexdigest()

        conn = Conexao.criar_conexao()


        cursor = conn.cursor(dictionary=True)


        sql = "SELECT nome, login, senha FROM tb_usuarios WHERE login = %s AND senha = %s"


        valores = (login, senha)


        cursor.execute(sql, valores)


        resultado = cursor.fetchone()


        cursor.close()
        conn.close()


        if resultado:
            session['usuario'] = resultado['login']
            session['nome_usuario'] = resultado['nome']
            return True
        else:
            return False

