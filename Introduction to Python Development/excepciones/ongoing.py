# my_file = open('recipes.txt', 'x')
# my_file.write('Meatballs\n')
# my_file.close()


#Si ejecutamos el codigo de arriba por segunda vez, nos saltara 
# Un error de que el archivo ya exite 
from fileinput import filename
import sys

file_name = 'recipes.txt'
try:
    my_file = open('recipes.txt', 'x')
    # my_file.write(b'Meatballs\n')
    my_file.write('Meatballs\n')
    my_file.close()
except FileExistsError as err:
    print(f"The {file_name} allredy exists.")
    # sys.exit(1)
except:
    print(f"Unable to wite to the file")
    # sys.exit(1)
else: 
    print(f"Wrote to {file_name}")
finally:
    print("Execution completed")