#Adivina el numero
import random


def run():
    numero_aleatorio=random.randint(1,100)
    numero_elegido=int(input('Elige un numero del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido< numero_aleatorio:
            print('Elija un numero mayor')
        else:
            print('Elija un numero menor')
        numero_elegido=int(input('Elija otro numero: '))    
    print('ganaste!')


if __name__=='__main__':
    run()