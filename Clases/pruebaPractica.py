from Practica import Practica

p = Practica()
p.setBD("senas.db")
p.id_categoria = 5

p.crearPreguntas()
preguntas = p.preguntas
print("---")
for pregunta in preguntas:
    print(pregunta)

for i in range(p.MAXPREGUNTAS):
    res = input(str(i)+": ")
    p.agregarRespuesta(int(res))

print(p.verResultado())