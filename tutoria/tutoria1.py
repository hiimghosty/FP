# validar que el numero sea multiplo de 3
import random
def validar():
  N=10
  while((N%3!=0)):
    N=int(input('Introducir un numero multiplo de 3: '))

  return N

def listaDeContadoresDeUno(nroBinario):
    contador = 0
    posicionBinario = 1
    listaContador = []
    for elemento in nroBinario:
        if elemento == 1:
            contador = contador + 1
        if posicionBinario % 3 == 0:
            listaContador.append(contador)
            contador = 0
        posicionBinario = posicionBinario + 1
    return listaContador


def listaFinal(nroBinario, listaContador):
    posicionBinario = 1
    posicionLista = 0
    listaPedida = []
    for elemento in nroBinario:
        listaPedida.append(elemento)
        if posicionBinario % 3 == 0:
            listaPedida.append(listaContador[posicionLista])
            posicionLista = posicionLista + 1
        posicionBinario = posicionBinario + 1
    return listaPedida



#N = validar()
N= 9
nroBinario=[]

for i in range(0,N):
  #print("Insertar el elemento:" )
  #x=input()
  x=random.randint(0,1)
  nroBinario.append(x)



print(nroBinario)

listaContadorUnos=listaDeContadoresDeUno(nroBinario)
print(listaContadorUnos)
print(listaFinal(nroBinario,listaContadorUnos))