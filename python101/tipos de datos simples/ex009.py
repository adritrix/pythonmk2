cantidadInvertir=float(input("Que cantidad de € quieres inventir?"))
interesAnual=int(input("Interes?"))
años=int(input("A cuantsos años?"))


total=(cantidadInvertir * (interesAnual / 100 + 1) ** años, 2)

print("Con una cantidad de ", cantidadInvertir," con un interes anual de ", interesAnual, " en ", años, " tendras un total de ", total)