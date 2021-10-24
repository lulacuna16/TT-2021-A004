# ** Descargar sqlite tools y agregar la carpeta a las variables de entorno
# -- Convertir sql a sqlite
#     sqlite3 <baseDatosNueva.bd> -init <baseDatosVieja>
#     Ejemplo: (sqlite3 senas.db -init bd.sql)

from DataBase import DataBase
import os

path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/senas.db"
bd = DataBase(path)

bd.crearConexion()

# Pruebas generales
table = bd.leer('SELECT * FROM usuarios')
bd.imprimirTabla(table)

bd.actualizar('UPDATE usuarios SET nombre="User1" WHERE id_usuario=1')
table = bd.leer('SELECT * FROM usuarios')
bd.imprimirTabla(table)

bd.insertar('INSERT INTO usuarios (nombre,progreso_pnt,senas_completadas) VALUES ("Usuario Prueba",0,0)')
table = bd.leer('SELECT * FROM usuarios')
bd.imprimirTabla(table)



bd.borrar('DELETE FROM usuarios WHERE id_usuario=5')
table = bd.leer('SELECT * FROM usuarios')
bd.imprimirTabla(table)


# Prueba JOIN progresos
# bd.borrar('DELETE FROM progresos')
table = bd.leer('SELECT * FROM progresos')
bd.imprimirTabla(table)

bd.insertar('INSERT INTO progresos(id_usuario,id_sena) VALUES (1,3)')
bd.insertar('INSERT INTO progresos(id_usuario,id_sena) VALUES (1,2)')
bd.insertar('INSERT INTO progresos(id_usuario,id_sena) VALUES (1,6)')
bd.insertar('INSERT INTO progresos(id_usuario,id_sena) VALUES (2,34)')
bd.insertar('INSERT INTO progresos(id_usuario,id_sena) VALUES (2,32)')
bd.insertar('INSERT INTO progresos(id_usuario,id_sena) VALUES (3,24)')
bd.insertar('INSERT INTO progresos(id_usuario,id_sena) VALUES (3,77)')
bd.insertar('INSERT INTO progresos(id_usuario,id_sena) VALUES (3,46)')
bd.insertar('INSERT INTO progresos(id_usuario,id_sena) VALUES (3,67)')
table = bd.leer('SELECT * FROM progresos')
bd.imprimirTabla(table)

queryJOIN = '''
    SELECT
        u.nombre AS Usuario,
        s.nombre_sena AS Seña,
        c.nombre_cat AS Categoria
        FROM usuarios u
        INNER JOIN progresos p
            ON u.id_usuario = p.id_usuario
        INNER JOIN senas s
            ON p.id_sena = s.id_sena
        INNER JOIN categorias c
            ON s.id_categoria = c.id_categoria;
'''

table = bd.leer(queryJOIN)
bd.imprimirTabla(table)


bd.cerrarConexion()