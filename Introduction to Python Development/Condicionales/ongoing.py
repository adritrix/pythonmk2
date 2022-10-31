from random import Random, random
from random import seed
seed()
validador=round((10*random()))

print(validador)

segundo_val="si"
# segundo_val="no"

if validador > 5 and segundo_val=="si":
    print("Este numero es mayor que 5")
else:
    print("Este numero NO es mayor que 5")