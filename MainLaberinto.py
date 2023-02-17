from MetodosLaberinto import *
from colorama import Back,Fore

muro = ["1,0","1,1","1,2","2,2","2,3","3,3","3,2","4,2"]
entrada = ("0,0")
salida = ("4,4")

tamaño = int(input("De cuanto quieres que sea el laberinto (n X n ) "))
laberinto = generar_laberinto(tamaño,muro,entrada,salida)
printear_laberinto(laberinto)
