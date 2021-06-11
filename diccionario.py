def run():
    poblacion_paises={
        'Argentina':444684,
        'Brasil':21144558856,
        'colombia':355555
    }
    
    
    for pais, poblacion in poblacion_paises.items():
        print(pais+' tiene '+str(poblacion)+ ' habitantes')

if __name__== '__main__':
    run()