from colorama import init,Back,Fore




#Generar laberinto
def generar_laberinto(tamaño,muros ):
    array = []

    for X in range(0,tamaño):
        array.append([]) 
        for Y in range(0,tamaño):
            if (str(X) + "," +str(Y)) in muros:
                
                array[X].append("X")
            else:
                array[X].append(" ")
    
    return array
  






#Mostrar laberinto
def printear_laberinto(laberinto):
    init()
    for fila in laberinto:
        print('\t')
        for celda in fila :
            if celda==" " :
                print (Back.GREEN + Fore.BLACK+ '  '+Fore.RESET + Back.RESET,end= " ")
            elif celda == "X" :
                print (Back.RED +Fore.BLACK + 'X '+ Fore.RESET + Back.RESET,end=" " )
            elif celda =="E":
                print (Back.GREEN +Fore.GREEN + 'E '+ Fore.RESET + Back.RESET,end=" ")
            elif celda =="S":
                print (Back.YELLOW +Fore.YELLOW + 'S '+ Fore.RESET + Back.RESET,end=" ")
            elif celda ==".":
                print (Back.RED +Fore.BLACK + '. '+ Fore.RESET + Back.RESET,end=" ")