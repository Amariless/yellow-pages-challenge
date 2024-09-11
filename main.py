#Diccionario
from data import people

#Listar usuarios

print("Todos los usuarios son: ", list(people))

#Agregar usuario y numero

people[input()]

#Modificar usuario existente

#Eliminar usuario

#Salir

#Menu

while True:
    print("1. Listar usuarios: ")
    print("2. Añadir un usuario: ")
    print("3. Modificar usuario existente: ")
    print("4. Eliminar usuario existente: ")
    print("5. Salir")

    user_input = int(input())

    if user_input == 1:
        print ("Holiii")
    elif user_input == 2:
        print("Chao malparid")
    elif user_input == 3:
        break
    else:
        break