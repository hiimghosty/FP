import random

#temperaturas de febrero

tempFeb=[]
cantdeDias=29

for i in range(cantdeDias):
    temperatura = random.randint(15,30)
    tempFeb.append(temperatura)

print(tempFeb)

suma=0
dias=0
for i in range(20,27): #estamos recorriendo de los dias 21 al 27
    suma += tempFeb[i]
    dias += 1
    print(tempFeb[i])


print('promedio')
promedioTemp=suma/dias

print(promedioTemp)





