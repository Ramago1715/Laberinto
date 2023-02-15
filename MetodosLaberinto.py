from colorama import init,Back,Fore




#Generar laberinto
def generar_laberinto(tamaño):
    array = []
    for x in tamaño:
        print()
        for y in tamañol: 
            array.append([x,y])
    print(array)  
    return array
  






#Mostrar laberinto
def printear_laberinto(laberinto):
    init()
    for fila in laberinto:
        print('\t')
        for celda in fila :
            if celda==" " :
                print (Back.RED +Fore.BLACK + 'X ',end= " ")
            elif celda == "X" :
                print (Back.BLACK +Fore.BLACK + 'X ',end=" " )
            elif celda =="E":
                print (Back.GREEN +Fore.GREEN + 'E ',end=" ")
            elif celda =="S":
                print (Back.YELLOW +Fore.YELLOW + 'S ',end=" ")
            elif celda ==".":
                print (Back.RED +Fore.BLACK + '. ',end=" ")
            
