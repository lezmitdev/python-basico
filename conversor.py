def conversor(tipo_moneda,valor_dolar):
    moneda =int(input('¿Cuánta moneda '+tipo_moneda +" tienes?:"))
    moneda =float(moneda)
    dolares=moneda/ valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print('Tienes $'+ dolares+" dolares")

menu = """ 
Bienvenido al conversor de monedas 

1 - Moneda colombiana
2 - Moneda argentina
3 - Moneda mexicana
4 - Moneda Peruana

Elige una opción: """

opcion =int(input(menu))

if opcion ==1:
    conversor('colombiana',3875)
elif opcion ==2:
    conversor('argentina',65)
elif opcion ==3:
    conversor('mexicana',24)
elif opcion ==4:
    conversor('peruana',3.72)
else:
    print('Ingresa una opción correcta')



