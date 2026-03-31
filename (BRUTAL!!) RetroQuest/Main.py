import random; import sys; import tkinter as tk; import copy;
from Combat import combat
from Characters_Data import allcharacters
import Globals
from ColorText import rainbow
from Event_Generator import gerador_de_eventos
# from Commands import callboss
# from Bosses_Data import bossesact1
# from Commands import input_player

print(rainbow("Welcome to retroquest! if want to stop the game, type [EXIT]"))

#characters
def character_choice():
    while True:
     print("Choose your character!")
     for i, char in enumerate(allcharacters):
            print(f"[{i+1}] - {char.name}")

     #escolha
     choice=input(">  ")

     if choice.isdigit():
         charpos=int(choice)-1
         if 0<=charpos<len(allcharacters):
             return allcharacters[charpos]
             
     else:
        print("Sorry, that's ins't a valid choice")

player = character_choice()

print(f"Congrats! You chose, the {player.name}!")
    
filadeeventos=[]

while len(filadeeventos) < 2:
        filadeeventos.append(gerador_de_eventos(player))

while True:
    if Globals.bosscall == "called":
        Globals.bosscall = "notcalled"
        filadeeventos.clear()
        filadeeventos.append(gerador_de_eventos(player))

    evento = filadeeventos.pop(0)  # pega o atual

    tipo, oqé = evento

    if tipo == 1:
        oqé.trigger(player)

    elif tipo == 2:
        combat(player, oqé)

    elif tipo == 3:
        oqé.trigger(player)

    elif tipo == 4:
        oqé.trigger(player)

    elif tipo == 123:
        oqé(player)

    elif tipo == 67:
        combat(player, oqé)

    filadeeventos.append(gerador_de_eventos(player))

