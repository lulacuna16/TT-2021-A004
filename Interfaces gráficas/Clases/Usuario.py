import json

class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre

    # getters
    @property
    def nombre(self):
        return self.__nombre

    # setters
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return '{ "nombre": "'+ self.__nombre +'"}'

    # Mapear la clase a diccionario
    def __toDict(self):
        dic = {}
        dic['nombre'] = self.__nombre
        return dic

    def __setUsuario(self,dic):
        self.__nombre = dic["nombre"]

    # Guardar un nuevo usuario en .json
    def guardar(self,archivo):
        f = open(archivo, 'r')
        original = f.read()
        f.close()
        original = json.loads(original)
        original.append(self.__toDict())
        f = open(archivo, 'w')
        toJson = json.dumps(original, indent=4)
        f.write(toJson)
        f.close()

    # Obtener [] usuarios desde .json
    def obtenerUsuarios(self,archivo):
        f = open(archivo, 'r')
        usuarios = f.read()
        f.close()
        usuarios = json.loads(usuarios)
        return usuarios

    # Obtener usuario por nombre desde .json
    # def obtenerUsuario(self,archivo,nombre):
    #     f = open(archivo, 'r')
    #     usuarios = f.read()
    #     f.close()
    #     usuarios = json.loads(usuarios)
    #     for usuario in usuarios:
    #         if usuario["nombre"] == nombre:
    #             return usuario
    #     return "No encontro usuario"

    # Obtener usuario por indice desde .json
    def obtenerUsuarioIndex(self,archivo,index):
        f = open(archivo, 'r')
        usuarios = f.read()
        f.close()
        usuarios = json.loads(usuarios)
        if index >= 0  and index < len(usuarios):
            self.__setUsuario(usuarios[index])
        return "No encontro usuario"

    # def actualizarUsuario(self, archivo, nombre_o, nombre_n):
    #     f = open(archivo, 'r')
    #     usuarios = f.read()
    #     f.close()
    #     usuarios = json.loads(usuarios)
    #     for usuario in usuarios:
    #         if usuario["nombre"] == nombre_o:
    #             usuario["nombre"] = nombre_n
    #             f = open(archivo, 'w')
    #             toJson = json.dumps(usuarios, indent=4)
    #             f.write(toJson)
    #             f.close()
    #             return True
    #     return False

    def actualizarUsuarioIndex(self, archivo, index, nombre_n):
        f = open(archivo, 'r')
        usuarios = f.read()
        f.close()
        usuarios = json.loads(usuarios)
        if index >= 0  and index < len(usuarios):
            usuarios[index]["nombre"] = nombre_n
            f = open(archivo, 'w')
            toJson = json.dumps(usuarios, indent=4)
            f.write(toJson)
            f.close()
            return True
        return False
