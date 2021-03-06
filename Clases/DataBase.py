import sqlite3

class DataBase:

    def __init__(self, bd_path):
        self.__bd_path = bd_path

    def crearConexion(self):
        self.__conexion = sqlite3.connect(self.__bd_path)
        self.__cursor = self.__conexion.cursor()

    def cerrarConexion(self):
        self.__conexion.close()

    def leer(self,query):
        try:
            return self.__cursor.execute(query)
        except Exception as error:
            print("Error al leer")
            print(error)

    def actualizar(self,query):
        try:
            self.__cursor.execute(query)
            self.__conexion.commit()
        except Exception as error:
            print("Error al actualizar")
            print(error)

    def insertar(self,query):
        try:
            self.__cursor.execute(query)
            self.__conexion.commit()
        except Exception as error:
            print("Error al insertar")
            print(error)

    def borrar(self,query):
        try:
            self.__cursor.execute(query)
            self.__conexion.commit()
        except Exception as error:
            print("Error al borrar")
            print(error)

    def imprimirTabla(self,table):
        print("(",end="")
        for columnName in table.description:
            print(columnName[0], end=",")
        print(")")
        for row in table:
            print(row)