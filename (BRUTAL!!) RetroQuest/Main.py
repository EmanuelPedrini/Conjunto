import Globals
import random; import sys; import tkinter as tk; import copy;
from Combat import combat
from Kimeras_Data import allkimeras
from ColorText import rainbow
from Event_Generator import gerador_de_eventos
from THE_HOLE import THE_HOLE
from Tutorial import tutorial

# from Commands import callboss
# from Bosses_Data import bossesact1
# from Commands import input_player

def run_expedition():
    (print("Welcome to retroquest! if want to stop the game, type [EXIT]"))
#kimeras
    def kimera_choice():
        while Globals.gamerunning==1:
            print("Choose your kimera!")
            for i, char in enumerate(allkimeras):
                print(f"[{i+1}] - {char.name}")

     #escolha
            choice=input(">  ")

            if choice.isdigit():
                charpos=int(choice)-1
                if 0<=charpos<len(allkimeras):
                    return allkimeras[charpos]
            else:
                print("Sorry, that's ins't a valid choice")

    player = kimera_choice()
    print(f"Congrats! You chose, the {player.name}!")

    player.acthp = player.total_max_hp

    filadeeventos=[]
    while len(filadeeventos) < 2:
        filadeeventos.append(gerador_de_eventos(player))

    while Globals.gamerunning==1:
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
    return("ended_run")

while True:
    if Globals.gamerunning == 0:
        tutorial()

    elif Globals.gamerunning==1:
        run_expedition()
        
    if Globals.gamerunning==2:
        THE_HOLE()