#Roger Bajona

opcio = 0

#Mostro el menú i les opcions que hi ha.
while opcio != 4 :       #mentre's el número sigui diferent a 4 segir mostrant.
    print("=======================================")
    print("Menú d'opcions")
    print("=======================================")
    print("1. Hipotenusa d'un trinagle rectangle")
    print("2. Perímetre d'un trapezi")
    print("3. Arrel quadrada d'un nombre")
    print("4. Sortir programa")
    opcio =int(input("Entra una opció: "))
   


    import math
    if opcio == 1:
        catet_1 = int(input("Entra el nombre en centímetres d'un catet del triangle:")) #demano les mesures
        catet_2 = int(input("Entra el nombre de l'altre catet:"))
        suma_de_catets_al_quadrat=catet_1**2 + catet_2**2   #elevo les dos variables a 2 i les sumo.  
        arrel_quadrada= math.sqrt(suma_de_catets_al_quadrat)             #agafo el número que m'ha donat l'operació anterior i li aplico l'arrel cuadrada.
        print()
        print("La hipotenusa d'aquest triangle rectangle en centímetres és:", arrel_quadrada)
        print()

    elif opcio == 2:
        primer_costat = int(input("Escriu el nombre del primer costat en cm:"))
        segon_costat = int(input("Escriu el nombre del segon costat:"))
        terçer_costat = int(input("Escriu el nombre del terçer costat:"))
        quart_costat = int(input("Escriu el nombre del quart costar:"))
        perimetre_del_trapezi = primer_costat+segon_costat+terçer_costat+quart_costat
        print()
        print("El perímetre del trapezi és:",perimetre_del_trapezi,"cm")
        print()

    elif opcio ==3:
        nombre_escollit = int(input("Escriu el nombre que se li aplicarà una arrel quadrada:"))
        arrel_quadrada2 = nombre_escollit**(1/2)
        print()
        print("Aquesta és l'arrel quadrada de",nombre_escollit,"-->",arrel_quadrada2)
        print()
       
    elif opcio>4 or opcio<1:
        print("-Opció Incorrecta-")
        print()
       
    else:
        print("Gràcies per fer servir aquest programa!")
        break
