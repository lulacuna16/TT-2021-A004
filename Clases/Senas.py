from select import select
from .DataBase import DataBase

class Senas:

    def __init__(self):
        self.__id_sena = 0
        self.__nombre_sena = ""
        self.__id_categoria = 0

    #getters
    @property
    def id_sena(self):
        return self.__id_sena
    @property
    def nombre_sena(self):
        return self.__nombre_sena
    @property
    def id_categoria(self):
        return self.__id_categoria

    #setters
    @id_sena.setter
    def id_sena(self,id_sena):
        self.__id_sena = id_sena
    @nombre_sena.setter
    def nombre_sena(self,nombre):
        self.__nombre_sena = nombre
    @id_categoria.setter
    def id_categoria(self,id_cat):
        self.__id_categoria = id_cat

    def __str__(self) -> str:
        return "{id_sena: " + str(self.__id_sena) + ", nombre_sena: " + self.nombre_sena + ", id_categoria: " + str(self.__id_categoria) + "}"

    def setBD(self, path):
        self.__path = path

    def obtenerIdSenaBD(self):
        try:
            bd = DataBase(self.__path)
            bd.crearConexion()
            table = bd.leer(f'SELECT id_sena, id_categoria FROM senas WHERE nombre_sena="{self.nombre_sena}"')
            reg = table.fetchone()
            self.__id_sena = int(reg[0])
            self.__id_categoria = int(reg[1])
            bd.cerrarConexion()
        except Exception as e:
            print(e)