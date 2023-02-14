import colorama
def mostrar_laberinto(titulo,laberinto):
    for fila in laberinto:
        for celda in fila :
            if celda==" " :
                print (colorama.Back.RED +colorama.fore.BLACK + 'X ',end= " ")
            elif celda == "X" :
                print (colorama.Back.BLACK +colorama.fore.BLACK + 'X ',end=" " )
            elif celda =="E":
                print (colorama.Back.GREEN +colorama.Fore.GREEN + 'E',end=" ")
            elif celda =="S":
                print (colorama.Back.YELLOW +colorama.fore.YELLOW + 'S',end=" ")
            elif celda ==".":
                print (colorama.Back.RED +colorama.fore.BLACK + '.',end=" ")
