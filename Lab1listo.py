#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:12:45 2021

@author: FelipeJr
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import random
print("")
print("INTRODUCCION")
print("")
print("Para jugar, se le pedira las coordenadas de manera (X,Y)")
print("en donde usted debera ingresar cada variable.")
print("Por ejemplo, si desea ingresar la coordenada (0,1) se debe escribir como")
print("X = 0")
print("Y = 1")

cant_cartas = int(input("¿Con cuantas cartas desea jugar? "))

cartas1 = list(range(1, cant_cartas+1))
cartas2 = list(range(1, cant_cartas+1))

random.shuffle(cartas1)
random.shuffle(cartas2)

a = 0
n = 1
jugador1 = 0
jugador2 = 0
contador_final = 0


coordenadas0 = []
coordenadas1 = []


while contador_final < cant_cartas:
      
    while a < cant_cartas:
        
        coordenadas0.append((a,1))
        coordenadas1.append((a,0))
        a+= 1
    
    
    print("--------------------------------")
    print(coordenadas0)
    print(coordenadas1)
    print("")
    print("ingrese la coordenada que desea elegir. Se representará como (X, Y)")
    print("")
    print("ahora es el turno del jugador", n)
    
#    print("Esta es la respuesta")   
#    print(cartas1)
#    print(cartas2)
    
    x = int(input("X = "))
    y = int(input("Y = "))
    print("")
    
    valor1 = cartas1[x]
    valor2 = cartas2[x]
    
    
    if x > cant_cartas or x < 0:
        print("ingrese un numero valido para X")
        
    if y > 1 or y < 0:
        print("ingrese un numero valido para Y")    
    
    
    if y == 1:
        print("la carta obtenida es ", valor1)
        jugada1 = valor1
    
    if y == 0:
        print("la carta obtenida es ", valor2)
        jugada1 = valor2
    
    
    print("")
    print("ingrese la coordenada para su segunda carta ")
    x1 = int(input("X = "))
    y1 = int(input("Y = "))
    print("")
    
    
    valor3 = cartas1[x1]
    valor4 = cartas2[x1]
    
    
    if x1 > cant_cartas or x1 < 0:
        print("ingrese un numero valido para X")
        
    if y1 > 1 or y1 < 0:
        print("ingrese un numero valido para Y")    
    
    if y1 == 1:
        print("la carta obtenida es ", valor3)
        jugada2 = valor3
        
    if y1 == 0:
        print("la carta obtenida es ", valor4)
        jugada2 = valor4
        
    print("")
    
    if jugada1 != jugada2 and n == 2:
        n = 1
    
    elif jugada1 != jugada2 and n == 1:
        n = 2

    if jugada1 == jugada2:
        
        if n == 1:
            jugador1 += 1
        if n == 2:
            jugador2 += 1
            
        print("El jugador", n ,"ha ganado 1 punto.")
        print("")
        print("Resultado por el momento:")
        print("Jugador 1 =", jugador1)
        print("Jugador 2 =", jugador2)
        
        contador_final += 1
        
        if y == 1:
            coordenadas0.remove((x, 1))
            coordenadas0.insert(x, " ")
            
        if y == 0:
            coordenadas0.remove((x, 0))
            coordenadas0.insert(x, " ")
            
        if y1 == 1:
            coordenadas1.remove((x1, 1))
            coordenadas1.insert(x1, " ")
        if y1 == 0:
            coordenadas1.remove((x1, 0))
            coordenadas1.insert(x1, " ")
        

print("El juego ha acabado.")
    
    