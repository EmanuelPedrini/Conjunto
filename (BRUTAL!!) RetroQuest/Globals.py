
globaldanger = 1
globaldangercalc = (0.5*(globaldanger + 1))
globaldangermathsoftcap= (1+(globaldanger*5/((globaldanger*5)+15)))
gamerunning = 2
bosscall = str("notcalled")
cents = 0
breeding = False
endofarun = False
act = 1
day = 1
actualpool = list
from Enemies_Data import enemiespool, enemiespoolact2

if act == 1:
        actualpool = enemiespool
elif act == 2:
        actualpool = enemiespoolact2

from Kimeras_Data import allkimeras, allthekimerasforbreed, princesses

def reds(who):
    HC = 15
    reduction = who.armor / (who.armor + HC) 
    rdss = min(reduction, 0.90)
    return rdss

import time
import builtins

def slowprint(*args, sep=" ", end="\n", delay=0.00001, line_delay=0.2, flush=True):
    text = sep.join(map(str, args)) + end
    skip = False
    i=0
    while i < len(text):
            if msvcrt.kbhit():
                msvcrt.getch()
                skip = True

            if skip:
               builtins._original_print(text[i:], end="", flush=True)
               break

            builtins._original_print(text[i], end="", flush=True)
            time.sleep(delay)
            i += 1
        
    time.sleep(line_delay)

builtins._original_print = builtins.print
builtins.print = slowprint

import builtins
import msvcrt

def safe_input(prompt=""):
    while msvcrt.kbhit():
        msvcrt.getch()
    return builtins._original_input(prompt)

builtins._original_input = builtins.input
builtins.input = safe_input

def looktheirteeths(analized):
    save = (analized.total_max_hp)
    builtins._original_print(f"\n=== {analized.nickname} STATS ===")
    builtins._original_print(f"Level: [ {analized.level} ]\nExperience Points:\n [ {analized.xp} / {analized.xptonext} ]")
    builtins._original_print(f"Health Points   : [ {analized.acthp} / {save} ] + ( {analized.shield} ) SHIELD")
    builtins._original_print(f"Mana Points : [ {analized.actmana} / {analized.max_mana} ]")
    builtins._original_print(f"Attributes:")
    builtins._original_print(f"STR : {analized.total_strg} ( {analized.base_strg} )")
    builtins._original_print(f"DEX : {analized.total_dex} ( {analized.base_dex} )")
    builtins._original_print(f"VIT : {analized.total_vit} ( {analized.base_vit} )")
    builtins._original_print(f"INT : {analized.total_intel} ( {analized.base_intel} )")
    builtins._original_print(f"CHA : {analized.total_cha} ( {analized.base_cha} )")
    builtins._original_print(f"LUCK: {analized.total_luck} ( {analized.base_luck} )")
    builtins._original_print(f"ARMOR: {analized.armor} [ {reds(analized)}% ]")
    builtins._original_print(f"DODGE: {analized.total_dodge} %")
    builtins._original_print(f"VAMPIRISM: {analized.vampirism} %")
    builtins._original_print(f"THORNS: {analized.thorns}")

def banned_from_twitter(banned):
    for lista in (allkimeras, allthekimerasforbreed, princesses):
        if banned in lista:
            lista.remove(banned) 