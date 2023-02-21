from MetodosLaberinto import *
from colorama import Back,Fore
import time 

muro = ["1,0","1,1","1,2","2,2","2,4","4,2"]
entrada = ("0,0")
camino = []
salida = ("4,4")
tamaño = int(input("De cuanto quieres que sea el laberinto (n X n ) "))
X = 0
Y = 0
monigote = entrada
# print(monigote)
# Y =+ 1
# monigote = str(X)+","+str(Y)
# print(monigote)


salir = False
laberinto,exterior = generar_laberinto(tamaño,muro,entrada,salida,camino)
printear_laberinto(laberinto)
print("\n")

while salir == False:
    atascado = True
    if monigote == salida:
      salir = True
    #Ir a la derecha
    elif str(X)+","+str(Y+1) not in muro and str(X)+","+str(Y+1) not in camino and str(X)+","+str(Y+1) not in exterior:
       Y = Y+1
       camino.append(str(X)+","+str(Y))
       monigote = camino[-1]
       laberinto,exterior = generar_laberinto(tamaño,muro,entrada,salida,camino)
       printear_laberinto(laberinto)
       time.sleep(1)
       atascado = False
       print("\n")
    #Ir abajo
    elif str(X+1)+","+str(Y) not in muro and str(X+1)+","+str(Y) not in camino and str(X+1)+","+str(Y) not in exterior:
       X = X+1
       camino.append(str(X)+","+str(Y))
       monigote = camino[-1]
       laberinto,exterior = generar_laberinto(tamaño,muro,entrada,salida,camino)
       printear_laberinto(laberinto)
       time.sleep(1)
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
      muro.append(monigote)
      monigote = entrada
      camino = []