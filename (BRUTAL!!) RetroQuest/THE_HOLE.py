import Globals
from ColorText import *


def THE_HOLE():
    from Kimeras_Data import allkimeras, actualize_breed, actualize_princesses
    actualize_breed(allkimeras)
    actualize_princesses(allkimeras)

    print("Type your action!")
    print("Type [start] to start a NEW RUN with a princess!")
    print("Type [breed] to start breeding 2 KIMERAS!")
    print("Type [sleep] to end the day")

    input_player_in_the_hole()

def end_day():
    from Kimeras_Data import allkimeras, allthekimerasforbreed, princesses
    print(f"you finished the Day [ TOTAL DAYS: {Globals.day} ]")
    for baba in (allkimeras, allthekimerasforbreed, princesses):
        baba.age += 1
        baba.exhausted = False
        Globals.day += 1
        return

def print_status(chosen):
    print(f"NAME: {chosen.name}")
    # print(f": {}")
    # print(f": {}")
def full_name_with_nickname(chose):
    full_name_nickname = f"{chose.name} {chose.nickname} {chose.surname}"
    return full_name_nickname


def Start_Command():
    Globals.gamerunning = 1

def Breeding_Command():
    from Kimera import kimera
    from Kimeras_Data import allthekimerasforbreed, allkimeras
    if Globals.breeding == True:
        print("You are breeding already, restarting the process...\n")
        Globals.breeding = False
        return
    
    disponiveis = []
    for k in allthekimerasforbreed:
        if k.exhausted != True:
            disponiveis.append(k)

    if len(disponiveis) < 2:
        print("All your kimeras are exhausted or you don't have sufficient disponible kimeras to breed.")
        return
         
    
    Globals.breeding = True

    print("Please, choose 2 kimeras to procreate!")
    for number, kimerainlist  in enumerate(allthekimerasforbreed):
        if kimerainlist.exhausted == True:
            print((f"[{number+1}] - {kimerainlist.name} ( EXHAUSTED )"))
        else:    
            print((f"[{number+1}] - {kimerainlist.name}"))

    while Globals.gamerunning == 2:
        print("Choose the first kimera!")

        choice_for_breed = input_player_in_the_hole()

        if choice_for_breed.isdigit():
            index_kimera = int(choice_for_breed) - 1
            if 0<=index_kimera<len(allthekimerasforbreed):
                kimeraescolhida01 = allthekimerasforbreed[index_kimera]
                if kimeraescolhida01.exhausted == True:
                    print("This kimera can't breed today anymore")
                    continue
                else:
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

                            baby.acthp = baby.total_max_hp
                            allkimeras.append(baby)

                            kimeraescolhida01.exhausted = True
                            kimeraescolhida02.exhausted = True

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
    "breed": Breeding_Command,
    "start": Start_Command,
    "sleep": end_day,
}

def input_player_in_the_hole():
    while Globals.gamerunning==2:
        comm = input("> ")
        if comm in actions:
            actions[comm]()
            continue
        else:
            return comm

