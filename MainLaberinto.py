#TODOS LOS IMPORTS
from MetodosLaberinto import *
from colorama import Back,Fore
import time 

#DECLARACION DE VARIABLES
movimiento = []
camino: list[str] = []
entrada: str = "0,0"
monigote: str = entrada
muro: list[str] = ["1,1","0,1","2,2","3,2","1,3","4,4"]
salida:str = "0,3"
salir:bool = False
tamaño: int = int(input("De cuanto quieres que sea el laberinto (n X n ) "))


laberinto,exterior = generar_laberinto(tamaño,muro,entrada,salida,camino)
printear_laberinto(laberinto)
movimiento_laberinto(salida,muro,tamaño,entrada,exterior,monigote,camino,movimiento)
