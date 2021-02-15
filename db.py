import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self): #conexão com o banco de dados
        self.db = mysql.connector.connect(host = "localhost", 
                                            user = "root",
                                            passwd = "manussa1",
                                            database = "companhia_aerea",)
        self.my_cursor = self.db.cursor()


    # métodos referentes a tabela aeroporto
    def mostrar_aeroportos(self):
        self.my_cursor.execute("SELECT * FROM aeroporto")
        linhas = self.my_cursor.fetchall()
        return linhas

    def inserir_aeroporto(self, codigo_aeroporto, nome, cidade, estado):
        self.my_cursor.execute("INSERT INTO aeroporto VALUES (%s, %s, %s, %s)",(codigo_aeroporto, nome, cidade, estado))
        self.db.commit()
        #o API do database pega strings como argumentos e depois converte pro datatype apropriado

    def remover_aeroporto(self, codigo_aeroporto):
        self.my_cursor.execute("DELETE FROM aeroporto WHERE codigo_aeroporto = %s", (codigo_aeroporto,))
        self.db.commit()

    def atualizar_aeroportos(self, codigo_aeroporto, nome, cidade, estado):
        self.my_cursor.execute("UPDATE aeroporto SET nome= %s, cidade= %s, estado= %s WHERE codigo_aeroporto = %s",(nome, cidade, estado, codigo_aeroporto))
        self.db.commit()

    #métodos referentes a próxima tabela
    

    def encerrar_conexao(self): #fecha a conexão com o banco
        self.db.close()










