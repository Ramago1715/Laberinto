from MetodosLaberinto import *
from colorama import Back,Fore

muro = ["1,0","1,1","1,2","2,2","2,3","3,3","3,2","4,2"]

tamaño = int(input("De cuanto quieres que sea el laberinto (n X n ) "))
laberinto = generar_laberinto(tamaño,muro)
printear_laberinto(laberinto)
print(Fore.RESET + Back.RESET)