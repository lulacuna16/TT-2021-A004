from .DataBase import DataBase

class Senas:

    def __init__(self):
        self.__id_sena = 0
        self.__nombre_sena = ""
        self.__tipo_sena = ""
        self.__id_categoria = 0

    #getters
    @property
    def id_sena(self):
        return self.__id_sena
    @property
    def nombre_sena(self):
        return self.__nombre_sena
    @property
    def tipo_sena(self):
        return self.__tipo_sena
    @property
    def id_categoria(self):
        return self.__id_categoria

    #setters
    @id_sena.setter
    def id_sena(self,id_sena):
        self.__id_sena = id_sena
    @nombre_sena.setter
    def nombre_sena(self,nombre):
        self.__nombre_sena = self.removerTildes(nombre)
    @tipo_sena.setter
    def tipo_sena(self,tipoSena):
        self.__tipo_sena = tipoSena
    @id_categoria.setter
    def id_categoria(self,id_cat):
        self.__id_categoria = id_cat

    def __str__(self) -> str:
        return "{id_sena: " + str(self.__id_sena) + ", nombre_sena: " + self.nombre_sena + ", id_categoria: " + str(self.__id_categoria) + "}"

    def __repr__(self):
        return "{" + str(self.__id_sena) + ", " + self.nombre_sena + ", " + str(self.tipo_sena) + ", " + str(self.__id_categoria) + "}"

    def setBD(self, path):
        self.__path = path

    def obtenerIdSenaBD(self):
        try:
            bd = DataBase(self.__path)
            bd.crearConexion()
            table = bd.leer(f'SELECT id_sena, tipo_sena, id_categoria FROM senas WHERE nombre_sena="{self.nombre_sena}"')
            reg = table.fetchone()
            self.__id_sena = int(reg[0])
            self.__tipo_sena = int(reg[1])
            self.__id_categoria = int(reg[2])
            bd.cerrarConexion()
        except Exception as e:
            print(e)

    def removerTildes(self,cadena):
        cadena = str(cadena).replace("á","a")
        cadena = str(cadena).replace("é","e")
        cadena = str(cadena).replace("í","i")
        cadena = str(cadena).replace("ó","o")
        cadena = str(cadena).replace("ú","u")
        return cadena