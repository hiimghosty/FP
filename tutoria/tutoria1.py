# validar que el numero sea multiplo de 3
import random
def validar():
  N=10
  while((N%3!=0)):
    N=int(input('Introducir un numero multiplo de 3: '))

  return N

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


def listaFinal(nroBinario,listaContador):
  posicionBinario=1
  posicionLista=0
  listaPedida=[]
  for elemento in nroBinario:
    if ((posicionBinario-1)%3==0):
      listaPedida.append(listaContador[posicionLista])
      posicionLista=posicionLista+1
    else:
      listaPedida.append(elemento)


    posicionBinario=posicionBinario+1

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