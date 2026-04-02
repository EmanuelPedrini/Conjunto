import random; import copy
from Turnmaster import Turnmaster
from Enemies_Data import enemiespool
import random
from Commands import input_player
from Commands import escolhadealvo
from ColorText import*
from Bosses import boss
import Globals
# from Event_Generator import 
def resetbonus(player):
    player.bonus_strg = 0
    player.bonus_dex = 0
    player.bonus_vit = 0
    player.bonus_luck = 0
    player.bonus_cha = 0
    player.bonus_intel = 0
    player.magicdmgbonus=0

def combat_start(player):
    player.actmana = player.mana_inicial
    player.shield = player.shieldstat
    resetbonus(player)

def combat_end(player):
    for ps in player.passives:
        if ps.trigger=="on_combat_end":
            ps.passiveactivationtrigger(player)

    resetbonus(player)
    while Globals.gamerunning==1:
        if player.xp >= player.xptonext:
               player.level_system()
        if player.xp < player.xptonext:
               break

def player_turn_start():
     pass

def player_turn_end(player):
     player.regen_mana()

def turn_start():
     pass

def turn_end():
     pass

#definições de combate
def playerturn(player, actenemy):
        print("> It`s Your Turn!")
        print(f"> {player.name} actually have {player.acthp}/{player.total_max_hp} health points!")
        print(f"> You actually have [ {player.actmana} / {player.max_mana} ] Mana Points!")

        #Ações possíveis
        print("> Time to Act!\n> Actions:")
        print(light_red("[1] - BASIC ATTACK"))

        for i, ski in enumerate(player.skills):
            print(light_red(f"[{i+2}] - {ski.basename}"))
        ataquebasicoporturno = False

        #Escolha do player
        while Globals.gamerunning==1:
            choice = input_player(player, actenemy)
            if choice =="1":
                if ataquebasicoporturno==True:
                    print("You already used your basic attack this turn!")
                    continue
                    
                else: 
                        target = escolhadealvo(player, actenemy)
                        if target==None:
                             continue
                        if target.acthp > 0:
                            player.basicattack(target, player)
                            ataquebasicoporturno=True

                        if target.acthp <= 0:
                            if target in actenemy:
                                actenemy.remove(target)
                            continue
            
            elif choice.isdigit():
                #calculo pra determinar a skill na posição
                sedex= int(choice) - 2

                #verificando se o número está nas skills do PLAYER
                if 0 <= sedex < len(player.skills):

                    skill = player.skills[sedex] 

                    skill.use(player,escolhadealvo,actenemy)

                #se n for uma skill do player, ou n estiver nas skills dele
                else:
                    print("Sorry, that is a invalid Ability.")
                    continue
            #terminando seu turno
            elif choice == "endturn" or choice == "et":
                print(f"{player.name} ended {player.possessive} turn!")
                player_turn_end(player)
                break

            else:
                print("Sorry, thats a invalid Command.")
                
def enemyturn(enemy, player):
        # print(f">It`s {enemy.name} TURN!\n>He (she) is going to...")
        enemy.attack(player)
        if player.acthp <=0:
            player.death()

#ANCORA 1
def combat(player, enemies):

    oncombat=[player] + enemies
    tm = Turnmaster(oncombat)

    combat_start(player)
    boss_enemy = next((e for e in enemies if isinstance(e,boss)), None)
    if boss_enemy:
         print(light_red(f"{boss_enemy.intro}"))
    else:
         print(light_red("TIME TO DIE!, from the tar of the void some enemies arise!"))

    print("ACTION QUEUE:\n")
    print(yellow(f"- {player.name} ( {player.acthp} / {player.total_max_hp})"))
    print("")
    for e in enemies:
            if e.acthp > 0:
                print(red(f"- {e.name} ( {e.acthp} / {e.totalmaxhp} HP )"))
            print("")
            
    #essa é a parte que define o loop do combat
    while Globals.gamerunning==1:
        #primeiro ele usa a função que remove os inimigos mortos, ela vem do turnmaster que ta em outro arquivo
        tm.removermortos()

        #ele checa se o player morreu
        if player.acthp <= 0:
            player.death()
            break

        #checa se os inimigos morreram
        alive = [e for e in enemies if e.acthp > 0]
        if not alive:
            print("Enemies are all dead!")
            combat_end(player)
            break
        
        actualturn = tm.vezdequem()
        if actualturn==player:
             playerturn(player,enemies)
        else:
             enemyturn(actualturn, player)

        tm.passarturno()