from operator import mod


n = int(input("Dame el valor del numerador "))
m = int(input("Dame el valor del denominador "))
c = n/m
r = n % m

print("La division de ", n, "entre", m, " da un cociente de ", c, " y un resto de ", r)