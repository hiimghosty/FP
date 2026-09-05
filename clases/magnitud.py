import random
import math

def magnitud(B):
    suma= 0 
    for x in B:
        suma = suma + x**2

    resultado = math.sqrt(suma)
    return resultado


   



C=[20,30,40]
magnitud(C)


print( "La magnitud del vector es: ")
print(magnitud(C))


# random.randint(15,30)