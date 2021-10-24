from BaseDatos.DataBase import DataBase

class Usuario:

    def __init__(self):
        self.__id = 0
        self.__nombre = ""
        self.__porcentaje = 0.0
        self.__totalSenas = 0

    # getters
    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre
    @property
    def porcentaje(self):
        return self.__porcentaje
    @property
    def totalSenas(self):
        return self.__totalSenas

    # setters
    @id.setter
    def id(self, id):
        self.__id = id
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @porcentaje.setter
    def porcentaje(self, porcentaje):
        self.__porcentaje = porcentaje
    @totalSenas.setter
    def totalSenas(self, totalSenas):
        self.__totalSenas = totalSenas

    def __str__(self):
        return "{id:" + str(self.__id) + ", nombre: " + self.__nombre + ", porcentaje: " + str(self.__porcentaje) + ", total de señas: " + str(self.__totalSenas) + "}"

    def setBD(self, path):
        self.__path = path

    def obtenerUsuarioBDId(self, id):
        try:
            bd = DataBase(self.__path)
            bd.crearConexion()
            table = bd.leer(f'SELECT * FROM usuarios WHERE id_usuario={id}')
            reg = table.fetchone()
            self.__id = reg[0]
            self.__nombre = reg[1]
            self.__porcentaje = float(reg[2])
            self.__totalSenas = reg[3]
            bd.cerrarConexion()
        except Exception as e:
            print("Falta ruta base de datos. - " + e.__str__())

    def actualizarUsuarioBDId(self, id):
        try:
            bd = DataBase(self.__path)
            bd.crearConexion()
            bd.actualizar(f'UPDATE usuarios SET nombre="{self.__nombre}", progreso_pnt={self.__porcentaje}, senas_completadas={self.__totalSenas} WHERE id_usuario="{id}"')
            bd.cerrarConexion()
        except Exception as e:
            print("Falta ruta base de datos. - " + e.__str__())