from .DataBase import DataBase
from .Senas import Senas
import random

class Practica:

    def __init__(self):
        self.__id_categoria = -1
        self.__preguntas = []
        self.__solucion = []
        self.__respuestas = []
        self.__MAXPREGUNTAS = 10

    #getters
    @property
    def preguntas(self):
        return self.__preguntas

    @property
    def solucion(self):
        return self.__solucion

    @property
    def respuestas(self):
        return self.__respuestas

    @property
    def id_categoria(self):
        return self.__id_categoria

    @property
    def MAXPREGUNTAS(self):
        return self.__MAXPREGUNTAS

    #setters
    @id_categoria.setter
    def id_categoria(self,id_cat):
        self.__id_categoria = id_cat


    def setBD(self, path):
        self.__path = path

    def agregarRespuesta(self, sena):
        self.__respuestas.append(sena)

    def crearPreguntas(self):
        if self.__id_categoria > -1:
            if self.__id_categoria == 4:
                self.__MAXPREGUNTAS = 7
            #Creando solución
            self.__crearSolucion()
            print(self.__solucion)

            #Creando preguntas
            senas = self.__getSenas()
            totalSenas = len(senas)
            i = 0
            while(i < self.__MAXPREGUNTAS):
                indiceSol = random.randint(0,2)
                j = 0
                pregunta = []
                while (j < 3):
                    indice = random.randint(0, totalSenas-1)
                    sena = senas[indice]
                    if sena.tipo_sena == self.__solucion[i].tipo_sena:                # Verifica si es estática/dinámica
                        if sena.id_sena != self.__solucion[i].id_sena:            # Verifica que no se repita la solucion
                            if j == indiceSol:
                                pregunta.append(self.__solucion[i])
                                j = j + 1
                            else:
                                if not sena in pregunta:                # Verifica que no se repitan opciones
                                    pregunta.append(sena)
                                    j = j + 1
                self.__preguntas.append(pregunta)
                i = i + 1
        else:
            print("Ingrese una categoria primero")

    def __crearSolucion(self):
        senas = self.__getSenas()
        totalSenas = len(senas)
        i = 0
        while(i < self.__MAXPREGUNTAS):
            indice = random.randint(0, totalSenas-1)
            sena = senas[indice]
            if not sena in self.__solucion:
                self.__solucion.append(sena)
                i = i + 1

    def __getSenas(self):
        if self.id_categoria > -1:
            try:
                bd = DataBase(self.__path)
                bd.crearConexion()
                table = bd.leer(f'SELECT id_sena, tipo_sena, nombre_sena FROM senas WHERE id_categoria={self.__id_categoria}')
                senas = []
                for row in table:
                    sena = Senas()
                    sena.setBD(self.__path)
                    sena.id_categoria = self.id_categoria
                    sena.id_sena = row[0]
                    sena.tipo_sena = row[1]
                    sena.nombre_sena = row[2]
                    senas.append(sena)
                bd.cerrarConexion()
                return senas
            except Exception as e:
                print(e)
        else:
            print("Ingrese una categoria primero")

    def verResultado(self):
        buenas = 0
        for i in range(self.__MAXPREGUNTAS):
            if self.__solucion[i].id_sena == self.__respuestas[i].id_sena:
                buenas = buenas + 1
        return buenas
