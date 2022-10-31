# print('hola')
my_file = open('xmen.txt', 'w+')
my_file.write("Bestia\n")
my_file.write("Lovezno\n")
my_file.writelines([
    "Ciclope\n",
    "Bishop\n",
    "Rondador nocturno",
])

my_file.close()

my_file = open('xmen.txt', 'r')

print(my_file.read())
print("#################")
print(my_file.read())
print("#################")

my_file.seek(0)
# my_file.seek(10)
print(my_file.read())
my_file.close()



#___Si queremos que el fichero se cierre automaticamente se propene esto 

with open('hermandad.txt', 'w+') as my_file:
    my_file.write("Ezio\n")
    my_file.write("Altair\n")
    my_file.writelines([
        "Conor\n",
        "Bayel\n",
        "Claudia",
    ])
