def run():
#    for i in range(100):
#       if i%2!=0:
#            continue
#        print(i)


    texto = input('Escriba un texto: ')
    for letra in texto:
        if letra=='a':
            break
        print(letra)


if __name__=='__main__':
    run()
