#Roger Bajona
#4 ESO Científic
opcio=0
caracter='d'
es_num=0
text='texte'

#aquestes funcions són per protegir el programa, que no ens entrin caracters que no siguin numèrics
'''
def funcio_numero(caracter):    #retorna 1 si el caracter és un numero i 0 si no és un numero
    num=0
    try:
        num= int(caracter)
        return 1
    except ValueError:
        print()
        print("Valor no vàlid. Entra un número. Torna-ho a provar.")
        print()
        return 0

def ret_numero(text): # retorna un numero
    es_num_func=0                      
    while es_num_func==0:      #Mentre's no sigui un num, no soortim del while
        caracter=input(text)#demano les mesures
        es_num_func=funcio_numero(caracter)  #si funcio_numero() retorna un 1 és que caracter es un numero i sortim del while
    return int(caracter) #retornem el numero


#Mostro el menú i les opcions que hi ha.
while opcio != 4 :       #mentre's el número sigui diferent a 4 segir mostrant.
    es_num=0
    '''
    while es_num==0: #Mentre's no sigui un num, no soortim del while
        print("=======================================")
        print("Menú d'opcions")
        print("=======================================")
        print("1. Hipotenusa d'un trinagle rectangle")
        print("2. Perímetre d'un trapezi")
        print("3. Arrel quadrada d'un nombre")
        print("4. Sortir programa")
        caracter=input("Entra una opció: ")
        es_num=funcio_numero(caracter)
       
    opcio = int(caracter)
    #print("   opcio=",opcio)

    import math
    if opcio == 1:
        catet_1=ret_numero("Entra el nombre en centímetres d'un catet del triangle:")
        catet_2=ret_numero("Entra el nombre en centímetres de l'altre catet del triangle:")
        suma_de_catets_al_quadrat=catet_1**2 + catet_2**2   #elevo les dos variables a 2 i les sumo.  
        arrel_quadrada= math.sqrt(suma_de_catets_al_quadrat)             #agafo el número que m'ha donat l'operació anterior i li aplico l'arrel cuadrada.
        print()
        print("La hipotenusa d'aquest triangle rectangle en centímetres és:", arrel_quadrada)
        print()

    elif opcio == 2:
        primer_costat=ret_numero("Escriu el nombre del primer costat en cm:")
        segon_costat=ret_numero("Escriu el nombre del segon costat:")                 #demano la longitud dels costats i els sumo
        terçer_costat =ret_numero("Escriu el nombre del terçer costat:")
        quart_costat=ret_numero("Escriu el nombre del quart costar:")
        perimetre_del_trapezi = primer_costat+segon_costat+terçer_costat+quart_costat
        print()
        print("El perímetre del trapezi és:",perimetre_del_trapezi,"cm")
        print()

    elif opcio ==3:
        nombre_escollit=ret_numero("Escriu el nombre que se li aplicarà una arrel quadrada:")
        arrel_quadrada2 = nombre_escollit**(1/2)                                #aplico l'arrel quadrada elevant a 1/2
        print()
        print("Aquesta és l'arrel quadrada de",nombre_escollit,"-->",arrel_quadrada2)
        print()
       
    elif opcio ==4:
        print()
        print("Gràcies per fer servir aquest programa!") #aquest eles es refereix al núm. 4
        print()
        break
    else:#aqui faig que si posen un altre número digui que és uncorrecte i torni a sortir el menú d'opcions
        print()
        print("-- Opció no correta-- Torna-ho a provar...")
        print()
