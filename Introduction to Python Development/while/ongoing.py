from ast import While
from random import Random, random
from random import seed
seed()
validador=round((10*random()))

while True:
    validador=round((1000*random()))
    print(validador)
    if validador > 500:
        break

print("El validador: ", validador, "es mayor que 500")


