from DataBase import DataBase
import os

path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/senas.db"
bd = DataBase(path)

bd.crearConexion()


bd.borrar('DELETE FROM progresos')
table = bd.leer('SELECT * FROM usuarios')
bd.imprimirTabla(table)


queryAbecedario = "INSERT INTO progresos (id_usuario,id_sena) VALUES"
queryAbecedario += "(1,1),"    # a
queryAbecedario += "(1,2),"    # b
queryAbecedario += "(1,3),"    # c
queryAbecedario += "(1,4),"    # d
queryAbecedario += "(1,5),"    # e
queryAbecedario += "(1,6),"    # f
queryAbecedario += "(1,7),"    # g
queryAbecedario += "(1,8),"    # h
#queryAbecedario += "(1,9),"    # i
queryAbecedario += "(1,10),"   # j
queryAbecedario += "(1,11),"   # k
queryAbecedario += "(1,12),"   # l
queryAbecedario += "(1,13),"   # m
queryAbecedario += "(1,14),"   # n
queryAbecedario += "(1,15),"   # ñ
queryAbecedario += "(1,16),"   # o
queryAbecedario += "(1,17),"   # p
#queryAbecedario += "(1,18),"   # q
queryAbecedario += "(1,19),"   # r
queryAbecedario += "(1,20),"   # s
queryAbecedario += "(1,21),"   # t
queryAbecedario += "(1,22),"   # u
#queryAbecedario += "(1,23),"   # v
queryAbecedario += "(1,24),"   # w
queryAbecedario += "(1,25),"   # x
queryAbecedario += "(1,26),"   # y
queryAbecedario += "(1,27);"   # z

print(queryAbecedario)

queryNumeros = "INSERT INTO progresos (id_usuario,id_sena) VALUES"
#queryNumeros += "(1,28)," # 1
#queryNumeros += "(1,29)," # 2
#queryNumeros += "(1,30)," # 3
#queryNumeros += "(1,31)," # 4
#queryNumeros += "(1,32)," # 5
#queryNumeros += "(1,33)," # 6
#queryNumeros += "(1,34)," # 7
#queryNumeros += "(1,35)," # 8
queryNumeros += "(1,36)," # 9
queryNumeros += "(1,37)," # 10
queryNumeros += "(1,38)," # 20
queryNumeros += "(1,39)," # 30
queryNumeros += "(1,40)," # 40
queryNumeros += "(1,41)," # 50
queryNumeros += "(1,42)," # 60
queryNumeros += "(1,43)," # 70
queryNumeros += "(1,44)," # 80
queryNumeros += "(1,45)," # 90
queryNumeros += "(1,46);" # 100

queryCuerpo = "INSERT INTO progresos (id_usuario,id_sena) VALUES"
queryCuerpo += "(1,47)," # boca
queryCuerpo += "(1,48)," # brazo
queryCuerpo += "(1,49)," # codo
queryCuerpo += "(1,50)," # cuello
#queryCuerpo += "(1,51)," # diente
queryCuerpo += "(1,52)," # espalda
queryCuerpo += "(1,53)," # estómago
#queryCuerpo += "(1,54)," # hombro
queryCuerpo += "(1,55)," # lengua
queryCuerpo += "(1,56)," # mano
#queryCuerpo += "(1,57)," # muñeca
queryCuerpo += "(1,58)," # nariz
queryCuerpo += "(1,59)," # ojo
queryCuerpo += "(1,60)," # oreja
queryCuerpo += "(1,61)," # pelo
queryCuerpo += "(1,62)," # pulgar
queryCuerpo += "(1,63);" # uña

queryDias = "INSERT INTO progresos (id_usuario,id_sena) VALUES"
#queryDias += "(1,64)," # lunes
queryDias += "(1,65)," # martes
queryDias += "(1,66)," # miercoles
queryDias += "(1,67)," # jueves
queryDias += "(1,68)," # viernes
queryDias += "(1,69)," # sabado
queryDias += "(1,70);" # domingo

queryColores = "INSERT INTO progresos (id_usuario,id_sena) VALUES"
queryColores += "(1,71)," # amarillo
queryColores += "(1,72)," # azul
queryColores += "(1,73)," # rojo
queryColores += "(1,74)," # verde
queryColores += "(1,75)," # rosa
queryColores += "(1,76)," # cafe
#queryColores += "(1,77)," # morado
queryColores += "(1,78)," # naranja
queryColores += "(1,79)," # gris
queryColores += "(1,80)," # blanco
queryColores += "(1,81);" # negro

bd.insertar(queryAbecedario)
bd.insertar(queryNumeros)
bd.insertar(queryCuerpo)
bd.insertar(queryDias)
bd.insertar(queryColores)

# table = bd.leer('SELECT * FROM progresos')
# bd.imprimirTabla(table)

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