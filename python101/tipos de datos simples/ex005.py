#Por defecto los valores introducidos por terminal son de tipo string
###horas = input("Cuantas horas trabajas a la semana ? ")
#En este punto desconozco el parse. Uso el constructor de tipo entero o float para que se comporten como numeros operables
horas = int(input("Cuantas horas trabajas a la semana ? "))

precioPorHora = int(input("Cuanto cobras por hora? "))
salarioSemanal = horas * precioPorHora
# print(salarioSemanal)
# print("El salario semanal seria de ",salarioSemanal,"€")
# El metodo print no te convierte los enteros a cadena al concatener por lo que es necesario convertir manualmente la variable numeria a cadena o usar coma
print("El salario semanal seria de ",salarioSemanal,"€ y el mensual de "+ str(salarioSemanal*4) +"€")