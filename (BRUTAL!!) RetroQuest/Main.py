import random; import sys; import tkinter as tk; import copy;
from Combat import combat
from Events_Data import badevents, neutralevents, goodevents
from Enemies_Data import enemiespool
from Characters_Data import allcharacters
from ColorText import rainbow
from Itens_Data import todososequipamentos
from Commands import input_player
# from Combat import encounter

print(rainbow("Welcome to retroquest! if want to stop the game, type [EXIT]"))

def shop(player):
    print(f"In distance, you can see a small hut and you decide to investigate.")
    print(f"Entering on the the small hut, you discover it is a shop, a buff woman in a armor is leaning on the counter")
    print(f"(Agnes) - Hey BRO! what`s up? want to buy something from my shop?")

    shop_total_options = todososequipamentos
    shopactoptions = random.sample(shop_total_options, min(5, len(shop_total_options)))

    for cont, itemI in enumerate(shopactoptions):
        print(f"{cont+1} - {itemI.name}")

    buyintend= input_player(player, None)
    if buyintend.isdigit:
        realbuyintend= int(buyintend)-1
        if 0<= realbuyintend <len(shopactoptions):
            buyed = shopactoptions[realbuyintend]
            player.add_item(buyed)

    print()

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

def gerador_de_eventos(player):
    #número random que define o evento q vai retornar
    escolhadeevento= int((1 + (player.luck/(player.luck+15))) * (random.randint(1, 100)))

    #evento paia
    if escolhadeevento <= 25:
        return (1, random.choice(badevents))
    
    #Combate aleatório
    elif escolhadeevento > 25 and escolhadeevento <= 50:
        quantidadeinimigos = random.randint(1, 3)
        actenemy = [
            copy.deepcopy(e) 
            for e in random.sample(enemiespool, k=min(quantidadeinimigos, len(enemiespool)))
            ]
        return (2, actenemy)
    
    elif 50 < escolhadeevento <=60:
        return (123, shop)
    
    elif escolhadeevento > 60 and escolhadeevento < 85:
        return (3, random.choice(neutralevents))
    
    else:
        return (4, random.choice(goodevents))
    
filadeeventos=[]

while len(filadeeventos) < 2:
    filadeeventos.append(gerador_de_eventos(player))

while True:
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
    
    #ultra events

    filadeeventos.append(gerador_de_eventos(player))

