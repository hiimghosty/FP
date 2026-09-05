import random

#temperaturas de febrero

tempFeb=[]
cantdeDias=29

for i in range(cantdeDias):
    temperatura = random.randint(15,30)
    tempFeb.append(temperatura)


print(tempFeb)
print("La mayor temperatura es : ")
print(max(tempFeb))
print("y ocurre en el dia nro: ")
print(tempFeb.index(max(tempFeb)) + 1)


