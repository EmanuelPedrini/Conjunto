from pgterminal import print, input, tick
import Globals
import random; import sys; import tkinter as tk; import copy;
from Combat import combat
from Kimeras_Data import princesses, allkimeras
from Event_Generator import gerador_de_eventos
from THE_HOLE import THE_HOLE
from Tutorial import tutorial, full_name_with_nickname
from Kimeras_Data import actualize_princesses
from Globals import looktheirteeths
from Globals import banned_from_twitter
# from Commands import callboss
# from Bosses_Data import bossesact1
# from Commands import input_player

def run_expedition():
    actualize_princesses(allkimeras)
    (print("Welcome to KIMERAHALLA! if want to go back to THE HOLE, type [EXIT]"))

#kimeras
    def kimera_choice():
        while Globals.gamerunning==1:
            tick()
            print("Choose your kimera!")
            for i, char in enumerate(princesses):
                print(f"[{i+1}] - { full_name_with_nickname(char) }")

     #escolha
            choice=input(">  ")

            if choice.isdigit():
                charpos=int(choice)-1
                if 0 <= charpos <len(princesses):
                    actonrun = princesses[charpos]
                    banned_from_twitter(actonrun)
                    return actonrun
                
            elif choice == "lookteeths" or choice == "lk":
                lookedteeths = input("Who you wanna see closely?\n> ")
                if lookedteeths.isdigit():
                    lkth=int(lookedteeths)-1
                    if 0<= lkth <len(princesses):
                        looktheirteeths(princesses[lkth])
                        continue
                continue

                
            elif choice == "EXIT":
                Globals.gamerunning = 2
                print("Welcome Back to THE HOLE!")

            else:
                print("Sorry, that's ins't a valid choice")
                continue

    player = kimera_choice()

    if player is None:
        return


    print(f"Congrats! You chosed {full_name_with_nickname(player)}!")
    player.acthp = player.total_max_hp

    filadeeventos=[]
    while len(filadeeventos) < 2:
        filadeeventos.append(gerador_de_eventos(player))

    while Globals.gamerunning==1:
        tick()
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