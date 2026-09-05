
NroDeAlumnos=int(input('insertar numero de alumnos'))
Notas=[]


for i in range(NroDeAlumnos):
    x=int(input('Insertar nota'))
    Notas.append(x)


promedio=sum(Notas)/NroDeAlumnos

cantidadDeInferioresAlPromedio=0

for calificacion in Notas:
    if calificacion < promedio:
        cantidadDeInferioresAlPromedio += 1

print(cantidadDeInferioresAlPromedio)

