from .DataBase import DataBase

class Progreso:

    def __init__(self):
        self.__id_progreso = 0
        self.__id_usuario = 0
        self.__id_sena = 0

    #getters
    @property
    def id_progreso(self):
        return self.__id_progreso
    @property
    def id_usuario(self):
        return self.__id_usuario
    @property
    def id_sena(self):
        return self.__id_sena

    #setters
    @id_progreso.setter
    def id_progreso(self,id_prog):
        self.__id_progreso = id_prog
    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self.__id_usuario = id_usuario
    @id_sena.setter
    def id_sena(self,id_sena):
        self.__id_sena = id_sena

    def __str__(self):
        return "{id_progreso" + str(self.__id_progreso) + ", id_usuario: " + str(self.__id_usuario) + ", id_sena: " + str(self.__id_sena) + "}"

    def setBD(self, path):
        self.__path = path

    def insertarProgreso(self):
        try:
            bd = DataBase(self.__path)
            bd.crearConexion()
            bd.insertar(f'INSERT INTO progresos (id_usuario,id_sena) VALUES ({self.__id_usuario},{self.id_sena})')
            bd.cerrarConexion()
        except Exception as e:
            print(e)

    def senasCorrectasCategoria(self, id_usuario, id_categoria):
        queryJOIN = f'''
            SELECT
                s.nombre_sena
                FROM usuarios u
                INNER JOIN progresos p
                    ON u.id_usuario = {id_usuario}
                    AND u.id_usuario = p.id_usuario
                INNER JOIN senas s
                    ON p.id_sena = s.id_sena
                INNER JOIN categorias c
                    ON s.id_categoria = c.id_categoria
                    AND c.id_categoria = {id_categoria};
            '''
        correctas = []
        try:
            bd = DataBase(self.__path)
            bd.crearConexion()
            table = bd.leer(queryJOIN)
            for row in table:
                correctas.append(str(row[0]))
            bd.cerrarConexion()
            return correctas
        except Exception as e:
            print(e)

    def progresoCategoria(self, id_usuario, id_categoria):
        queryJOIN = f'''
            SELECT
                count(s.nombre_sena)
                FROM usuarios u
                INNER JOIN progresos p
                    ON u.id_usuario = {id_usuario}
                    AND u.id_usuario = p.id_usuario
                INNER JOIN senas s
                    ON p.id_sena = s.id_sena
                INNER JOIN categorias c
                    ON s.id_categoria = c.id_categoria
                    AND c.id_categoria = {id_categoria};
            '''
        try:
            bd = DataBase(self.__path)
            bd.crearConexion()
            row = bd.leer(queryJOIN)
            senasCorrectas = float(row.fetchone()[0])
            row = bd.leer(f'SELECT COUNT(*) FROM senas WHERE id_categoria = {id_categoria}')
            totalSenas = float(row.fetchone()[0])
            porcentaje = (senasCorrectas * 100) / totalSenas
            bd.cerrarConexion()
            return porcentaje
        except Exception as e:
            print(e)