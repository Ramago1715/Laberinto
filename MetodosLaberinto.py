from colorama import init,Back,Fore




#Generar laberinto
def generar_laberinto(tamaño,muros,entrada,salida,camino):
    array = []
    muro = []
    for numero in range(0,tamaño):
        muro.append(str(-1)+","+str(numero))
        muro.append(str(tamaño)+","+str(numero))
    for numero in range(0,tamaño):
        muro.append(str(numero)+","+str(-1))
        muro.append(str(numero)+","+str(tamaño))

    for X in range(0,tamaño):
        array.append([]) 
        for Y in range(0,tamaño):


            if (str(X) + "," +str(Y)) in camino:
                array[X].append(".")
            elif (str(X) + "," +str(Y)) in salida:
                array[X].append("E")
            elif (str(X) + "," +str(Y)) in entrada:
                array[X].append("S")
            elif (str(X) + "," +str(Y)) in muros:
                array[X].append("X")
            else:
                array[X].append(" ")
    return array,muro
  
#Mostrar laberinto
def printear_laberinto(laberinto):
    init()
    for fila in laberinto:
        print('\t')
        for celda in fila :
            if celda==" " :
                print (Back.LIGHTBLACK_EX + Fore.BLACK+ '  '+Fore.RESET + Back.RESET,end= " ")
            elif celda == "X" :
                print (Back.RED +Fore.BLACK + '  '+ Fore.RESET + Back.RESET,end=" " )
            elif celda =="E": 
                print (Back.YELLOW +Fore.YELLOW + '  '+ Fore.RESET + Back.RESET,end=" ")
            elif celda =="S":
                print (Back.WHITE +Fore.YELLOW + '  '+ Fore.RESET + Back.RESET,end=" ")
            elif celda ==".":
                print (Back.CYAN +Fore.BLACK + '. '+ Fore.RESET + Back.RESET,end=" ")