#TODOS LOS IMPORTS
from MetodosLaberinto import *
from colorama import Back,Fore
import time 

#DECLARACION DE VARIABLES
camino: list[str] = []
entrada: str = "0,0"
monigote: str = entrada
muro: list[str] = ["1,0","1,1","1,2","2,2","2,4","4,2"]
salida:str = "4,4"
salir:bool = False
tamaño: int = int(input("De cuanto quieres que sea el laberinto (n X n ) "))


laberinto,exterior = generar_laberinto(tamaño,muro,entrada,salida,camino)
printear_laberinto(laberinto)
movimiento_laberinto(salida,muro,tamaño,entrada,exterior,monigote,camino)
