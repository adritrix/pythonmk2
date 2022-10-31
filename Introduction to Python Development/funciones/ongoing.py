def hello_world():
    print("hello_world pepe")

hello_world()


def hello_world_nombre(name="adrian"):
    print(f"hello_world {name}")

hello_world_nombre("pedro")

def hello_world_nombre_retorno(name="adrian", surname="navarro"):
    # return (f"hello_world pepe {name}")
    halt = (f"hello_world pepe {name} {surname}")
    return halt

print(hello_world_nombre_retorno("alvaro", "losa"))
print(hello_world_nombre_retorno(surname="gonzalez" ,name="pedro" ))
# print(hello_world_nombre_retorno("cano",name="alejando"))