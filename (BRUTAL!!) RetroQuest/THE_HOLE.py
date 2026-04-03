import Globals
from ColorText import *

def rdiniti():
    from Kimera import kimera
    from Kimeras_Data import allkimeras
    for k in range(5):
        rd = kimera.random("Queen")
        rd.age += 50
        allkimeras.append(rd)
def show_list(listaesc):
    for numb, kimera  in enumerate(listaesc):   
                print((f"[{numb+1}] - {kimera.name} ( {kimera.status} )"))

def big_ass_print(choice, listap):
            while True:
                if choice.isdigit():
                        index = int(choice) - 1
                        if 0<= index <len(listap):
                            escolha = listap[index]
                            return escolha
                        else:
                            print("Out of the actual options")
                            break
                else:
                    print("Type the number of your choice")
                    break            

def lookingsmaching(theone):
    sumallstats = int(theone.base_strg + theone.base_dex + theone.base_vit +theone.base_intel + theone.base_cha + theone.base_luck)

    skpt = len(theone.skills)

    pspt = len(theone.passives)

    mtpt = len(theone.mutations)

    ptprtt = (skpt * 11) + (pspt * 20) + (mtpt * 5)

    hdpt = (ptprtt / (ptprtt + 12))

    points = int((sumallstats * 100) * hdpt) 

    return points
        
def look_teeths_again_Command():
    from Globals import looktheirteeths
    from Kimeras_Data import allkimeras
    print("Choose a Kimera to analize!")
    show_list(allkimeras)
    cxp = input("> ")
    alisada = big_ass_print(cxp, allkimeras)
    if alisada == None:
         return
    looktheirteeths(alisada)

def look_best_Command():
    # from Globals import looktheirteeths
    from Kimeras_Data import allkimeras
    print("Choose a Kimera to analize!")
    show_list(allkimeras)
    chcc = input("> ")
    alisada = big_ass_print(chcc, allkimeras)
    if alisada == None:
        return
    analise_da_alisada = lookingsmaching(alisada)
    print(f"Using a points scale {full_name_with_nickname(alisada)} received the score of {analise_da_alisada}.")

def Points_list():
     from Kimeras_Data import allkimeras
     for n, k in enumerate(allkimeras):
          print(f"[{n+1}] - {full_name_with_nickname(k)} / ( SCORE: {lookingsmaching(k)} )")

    

def THE_HOLE():
    rdiniti()
    from Kimeras_Data import allkimeras, actualize_breed, actualize_princesses
    actualize_breed(allkimeras)
    actualize_princesses(allkimeras)

    print("Type your action!")
    print("Type [start] to start a NEW RUN with a princess!")
    print("Type [breed] to start breeding 2 KIMERAS!")
    print("Type [sleep] to end the day")

    input_player_in_the_hole()

def end_day():
    from Kimeras_Data import allkimeras, allthekimerasforbreed, princesses, actualize_breed, actualize_princesses

    print(f"you finished the Day [ TOTAL DAYS: {Globals.day} ]")

    for i in allkimeras:
            i.age += 1
            i.exhausted = False

    Globals.day += 1

    actualize_breed(allkimeras)
    actualize_princesses(allkimeras)
        
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

    while Globals.gamerunning == 2:
        print("Please, choose 2 kimeras to procreate!")
        for number, kimerainlist  in enumerate(allthekimerasforbreed):
            if kimerainlist.exhausted == True:
                print((f"[{number+1}] - {kimerainlist.name} ( {kimerainlist.status} ) ( EXHAUSTED )"))
            else:    
                print((f"[{number+1}] - {kimerainlist.name} ( {kimerainlist.status} ) ( DISPONIBLE )"))
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
                    if kimerainlist02.exhausted == True:
                        print((f"[{number02+1}] - {kimerainlist02.name} ( {kimerainlist02.status} ) ( EXHAUSTED )"))
                    else: 
                        print((f"[{number02+1}] - {kimerainlist02.name} ( {kimerainlist02.status} ) ( DISPONIBLE )"))

                print(f"Chose other kimera!")

                choice_for_breed02 = input_player_in_the_hole()
                if choice_for_breed02.isdigit():
                        index_kimera02 = int(choice_for_breed02) - 1
                        if 0<= index_kimera02 <len(kimeras_restantes):
                            kimeraescolhida02 = kimeras_restantes[index_kimera02]
                            if kimeraescolhida02.exhausted == True:
                                print("This kimera can't breed today anymore")
                                continue
                            else:
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
    "lookteeths": look_teeths_again_Command,
    "lookpoints": look_best_Command,
    "thebests": Points_list,
}

def input_player_in_the_hole():
    while Globals.gamerunning==2:
        comm = input("> ")
        if comm in actions:
            actions[comm]()
            continue
        else:
            return comm

