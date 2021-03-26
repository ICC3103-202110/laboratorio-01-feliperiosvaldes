
from numpy import random

print("")
print("¡Bienvenido al juego MEMORICE!")
print("")
print("INTRODUCCION")
print("")
print("Para jugar, se le pedira las coordenadas de manera (X,Y)")
print("en donde usted debera ingresar cada variable.")
print("Por ejemplo, si desea ingresar la coordenada (0,1) se debe escribir como")
print("X = 0")
print("Y = 1")
print("")
print("En la linea de codigo numero 52 se encuentra el valor de las cartas para el memorice")

amount_of_cards = int(input("¿Con cuantos pares de cartas desea jugar? "))

cards1 = list(range(1, amount_of_cards+1))
cards2 = list(range(1, amount_of_cards+1))

random.shuffle(cards1)
random.shuffle(cards2)

a = 0
n = 1
player1 = 0
player2 = 0
final_counter = 0


coordinates0 = []
coordinates1 = []


while final_counter < amount_of_cards:
      
    while a < amount_of_cards:
        
        coordinates0.append((a,1))
        coordinates1.append((a,0))
        a+= 1
      
    print("--------------------------------")
    print(coordinates0)
    print(coordinates1)
    print("")
    print("ingrese la coordenada que desea elegir. Se representará como (X, Y)")
    print("")
    print("ahora es el turno del jugador", n)
    
    print("Esta es la respuesta")   
    print(cards1)
    print(cards2)
    
    x = int(input("X = "))
    y = int(input("Y = "))
    print("")
    
    value1 = cards1[x]
    value2 = cards2[x]
    
    
    if x > amount_of_cards or x < 0:
        print("ingrese un numero valido para X")
        
    if y > 1 or y < 0:
        print("ingrese un numero valido para Y")    
    
    
    if y == 1:
        print("la carta obtenida es ", value1)
        move1 = value1
    
    if y == 0:
        print("la carta obtenida es ", value2)
        move1 = value2
    
    
    print("")
    print("ingrese la coordenada para su segunda carta ")
    x1 = int(input("X = "))
    y1 = int(input("Y = "))
    print("")
    
    
    value3 = cards1[x1]
    value4 = cards2[x1]
    
    
    if x1 > amount_of_cards or x1 < 0:
        print("ingrese un numero valido para X")
        
    if y1 > 1 or y1 < 0:
        print("ingrese un numero valido para Y")    
    
    if y1 == 1:
        print("la carta obtenida es ", value3)
        move2 = value3
        
    if y1 == 0:
        print("la carta obtenida es ", value4)
        move2 = value4
        
    print("")
    
    if move1 != move2 and n == 2:
        n = 1
    
    elif move1 != move2 and n == 1:
        n = 2

    if move1 == move2:
        
        if n == 1:
            player1 += 1
        if n == 2:
            player2 += 1
            
        print("El jugador", n ,"ha ganado 1 punto.")
        print("")
        print("Resultado por el momento:")
        print("Jugador 1 =", player1)
        print("Jugador 2 =", player2)
        
        final_counter += 1
        
        if y == 1:
            coordinates0.remove((x, 1))
            coordinates0.insert(x, " ")
            
        if y == 0:
            coordinates0.remove((x, 0))
            coordinates0.insert(x, " ")
            
        if y1 == 1:
            coordinates1.remove((x1, 1))
            coordinates1.insert(x1, " ")
            
        if y1 == 0:
            coordinates1.remove((x1, 0))
            coordinates1.insert(x1, " ")
        
print("")

if player1 == player2:
    print("Hubo un empate.")

if player1 < player2:
    print("¡Ha ganado el jugador 2, felicitaciones!")

if player1 > player2:
    print("¡Ha ganado el jugador 1, felicitaciones!")

print("")
print("El juego ha acabado.")
































    
    