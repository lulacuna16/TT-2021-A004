from Usuario import Usuario
import os

path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/senas.db"
# print(path)

usuario = Usuario()
usuario.setBD(path)

usuario.obtenerUsuarioBDId(1)
print(usuario)

usuario.nombre = "User 1"
usuario.porcentaje = 0.0
usuario.totalSenas = 0
usuario.actualizarUsuarioBDId(1)
usuario.obtenerUsuarioBDId(1)
print(usuario)