N= int(input('ingresar nu numero multiplo de 3'))
ListaBinaria = []

# carga de lista

for i in range(N):
    ListaBinaria.append(int(input('introducir elemento ')))

print(ListaBinaria)

def crearLista(lista):
    contadorUnos=0
    contadorPos=0
    listaDeContadores=[]
    for x in lista:
        contadorPos += 1
        if x==1:
            contadorUnos+= 1
        if (contadorPos%3==0):
            contadorPos = 0
            listaDeContadores.append(contadorUnos)
            contadorUnos=0


    print(listaDeContadores)


crearLista(ListaBinaria)




