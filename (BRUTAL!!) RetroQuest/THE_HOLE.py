import Globals
from Kimera import kimera
from Kimeras_Data import allkimeras, allthekimerasforbreed
from ColorText import *

def THE_HOLE():
    print("Welcome to the THE HOLE!")
    input_player_in_the_hole()
    # print("TYPE [ 1 ] TO START A NEW RUN WITH A PRINCESS!")
    # print("TYPE [ 2 ] TO SEE ONE OF YOUR KIMERAS!")
    # print("TYPE [ 3 ] TO SEE YOUR HISTORY OF EXPEDITIONS!")
    # print("TYPE [ 4 ] TO BREED TWO OF YOUR SUITORS")
    # print("TYPE [ 5 ] TO BREED A PRINCESS!")
    # print("TYPE [ 6 ] TO SEE ALL YOUR PRINCESSES!")
# def show_kimeras_for_breed()
#     for number, kimerainlist  in enumerate(allthekimerasforbreed):
#         print((f"[{number+1}] - {kimerainlist.name}"))

def print_status(chosen):
    print(f"NAME: {chosen.name}")
    # print(f": {}")
    # print(f": {}")
def full_name_with_nickname(chose):
    full_name_nickname = f"{chose.name} {chose.nickname} {chose.surname}"
    return full_name_nickname

def Breeding_Command():

    if Globals.breeding == True:
        print("You are breeding already, restarting the process...\n")
        Globals.breeding = False
        return
    
    Globals.breeding = True

    print("Please, choose 2 kimeras to procreate!")
    for number, kimerainlist  in enumerate(allthekimerasforbreed):
        print((f"[{number+1}] - {kimerainlist.name}"))

    while Globals.gamerunning==2:
        print("Choose the first kimera!")

        choice_for_breed = input_player_in_the_hole()

        if choice_for_breed.isdigit():
            index_kimera = int(choice_for_breed) - 1
            if 0<=index_kimera<len(allthekimerasforbreed):
                kimeraescolhida01 = allthekimerasforbreed[index_kimera]
                print(f"You choose {kimeraescolhida01.name} to be procreate!")

                kimeras_restantes = []
                for k in allthekimerasforbreed:
                    if k != kimeraescolhida01:
                        kimeras_restantes.append(k)
                         
                for number02, kimerainlist02  in enumerate(kimeras_restantes):
                    print((f"[{number02+1}] - {kimerainlist02.name}"))
                print(f"Chose other kimera!")

                choice_for_breed02 = input_player_in_the_hole()
                if choice_for_breed02.isdigit():
                        index_kimera02 = int(choice_for_breed02) - 1
                        if 0<= index_kimera02 <len(kimeras_restantes):
                            kimeraescolhida02 = kimeras_restantes[index_kimera02]
                            print(f"You choose {kimeraescolhida02.name} to be procreate!")
                            baby = kimera.breeding(kimeraescolhida01, kimeraescolhida02)
                            print(f"{kimeraescolhida01.name} and {kimeraescolhida02.name} made a beatiful baby! and named as ( {full_name_with_nickname(baby)} )")
                            allthekimerasforbreed.append(baby)
                            Globals.breeding = False

                            return
            

                        else:
                            print("Type a valid number.")
                            Globals.breeding = False
                            break  
                else:
                    print("Type a valid number.") 
                    Globals.breeding = False
                    break
                            
            else:
                print("Type a valid number.")
                Globals.breeding = False
                break
        else:
            print("Type a valid number.")
            Globals.breeding = False
            break

actions = {
    "breed": Breeding_Command
}

def input_player_in_the_hole():
    while Globals.gamerunning==2:
        comm = input("> ")
        if comm in actions:
            actions[comm]()
            continue
        else:
            return comm

