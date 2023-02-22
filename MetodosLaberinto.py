from colorama import init,Back,Fore
import time



#Generar laberinto
def generar_laberinto(tamaño:int,muros:list[str],entrada:str,salida:str,camino:list[str])->list[str]:
    array = []
    muro = []
    #recorro segun el tamaño que me diga el usuario para generar los tamaños exteriores invisibles para que el monigote no se salga del laberinto
    # detectando que es un muro 
    for numero in range(0,tamaño):
        muro.append(str(-1)+","+str(numero))
        muro.append(str(tamaño)+","+str(numero))
    for numero in range(0,tamaño):
        muro.append(str(numero)+","+str(-1))
        muro.append(str(numero)+","+str(tamaño))
    #Creo dos fors que me iteren (El primer for que recorre cada fila es la X)
    for X in range(0,tamaño):
        #Creo la primera fila
        array.append([]) 
        # Este for recorre cada posicion de cada array que es la Y)
        for Y in range(0,tamaño):
            #Si en la posicion actual esta en las cordenadas que hemos asigando que estan los muros,el camino, la salida o la entrada
            #Le pones un caracter o otro para usarlo en el colorama
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
def printear_laberinto(laberinto:list[str]):
    init()
    #Recorremos cada linia(Haciendo el \t para que se vea en cuadrado y no seguido)
    for fila in laberinto:
        print('\t')
        #Recorro posicion por posicion de los arrays y comprobando el caracter que hemos introducido antes lo pintamos de un color o otro
        for celda in fila :
            if celda==" " :
                print (Back.LIGHTBLACK_EX + '  '+Fore.RESET + Back.RESET,end= " ")
            elif celda == "X" :
                print (Back.RED +'  '+ Fore.RESET + Back.RESET,end=" " )
            elif celda =="E": 
                print (Back.YELLOW +'  '+ Fore.RESET + Back.RESET,end=" ")
            elif celda =="S":
                print (Back.WHITE +'  '+ Fore.RESET + Back.RESET,end=" ")
            elif celda ==".":
                print (Back.CYAN +Fore.BLACK + '. '+ Fore.RESET + Back.RESET,end=" ")

def movimiento_laberinto(salida:str,muro:list[str],tamaño:int,entrada:str,exterior:list[str],monigote:str,camino:list[str]):
    salir = False
    X:int = 0
    Y:int = 0
    #Meto todo el programa en un bucle que hasta que monigote no llegue a la meta
    #No sale del bucle
    print("\n")
    while salir == False:
        atascado = True
        if monigote == salida:
            salir = True
        #Ir a la derecha, comrpueba si la posicion de la derecha hay muro o camino y si no se mueve
        elif str(X)+","+str(Y+1) not in muro and str(X)+","+str(Y+1) not in camino and str(X)+","+str(Y+1) not in exterior:
            #En el caso de cumplirse aumento el valor de la Y, agrego la posicion a camino
            #Y modifico la posicion del monigote a la ultima posicion del camino, es decir a la acutal
            Y = Y+1
            camino.append(str(X)+","+str(Y))
            monigote = camino[-1]
            #Le meto a la funcion los nuevos datos del laberinto y lo printeo
            laberinto,exterior = generar_laberinto(tamaño,muro,entrada,salida,camino)
            printear_laberinto(laberinto)
            time.sleep(1)
            #Atascado es = false, para que declarar que ha hecho un movimiento
            atascado = False
            print("\n")
        #Ir abajo
        elif str(X+1)+","+str(Y) not in muro and str(X+1)+","+str(Y) not in camino and str(X+1)+","+str(Y) not in exterior:
            #En el caso de cumplirse aumento el valor de la X, agrego la posicion a camino
            #Y modifico la posicion del monigote a la ultima posicion del camino, es decir a la acutal
            X = X+1
            camino.append(str(X)+","+str(Y))
            monigote = camino[-1]
            #Le meto a la funcion los nuevos datos del laberinto y lo printeo
            laberinto,exterior = generar_laberinto(tamaño,muro,entrada,salida,camino)
            printear_laberinto(laberinto)
            time.sleep(1)
            #Atascado es = false, para que declarar que ha hecho un movimiento
            atascado = False
            print("\n")
        #Ir a la Izquierda
        elif str(X)+","+str(Y-1) not in muro and str(X)+","+str(Y-1) not in camino and str(X)+","+str(Y-1) not in exterior:
            Y = Y-1
            camino.append(str(X)+","+str(Y))
            monigote = camino[-1]
            laberinto,exterior = generar_laberinto(tamaño,muro,entrada,salida,camino)
            printear_laberinto(laberinto)
            time.sleep(1)
            atascado = False
            print("\n")
        #IR arriba
        elif str(X-1)+","+str(Y) not in muro and str(X-1)+","+str(Y) not in camino and str(X-1)+","+str(Y) not in exterior:
            X = X-1
            camino.append(str(X)+","+str(Y))
            monigote = camino[-1]
            laberinto,exterior = generar_laberinto(tamaño,muro,entrada,salida,camino)
            printear_laberinto(laberinto)
            time.sleep(1)
            atascado = False
            print("\n")
        elif atascado == True:
            #En el caso de que entre en este condicional significa que no ha hecho ningun cambio y quiere decir que se ha quedado atascado
            #Asi que guardo la posicion del monigote como si fuera un muro para que no vuelva a pasar por ahi, pongo el monigote en el inicio otra vez
            #Y restablezco el camino para que vuelva a empezar pero con un muro donde se ha quedado atascado para que no vuelva a pasar
            muro.append(monigote)
            monigote = entrada
            camino = []
            
