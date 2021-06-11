# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones!') 

# imprimir_mensaje()

def opciones(mensaje):
    print('Hola')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opcion (1,2,3): '))
if opcion ==1:
    opciones('Elegiste la opcion 1')
elif opcion==2:
    opciones('Elegiste la opcion 2')
elif opcion==3:
    opciones('Elegiste la opcion 3')
else:
    print('Elige una opcion correcta')        