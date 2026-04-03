from Kimera import kimera
from Skill_Data import *
#BEBEZES
allthebabies = []

#KIMERAS
allkimeras = []

#TODAS DISPÓNIVEIS PARA REPRODUZIR
allthekimerasforbreed = []

#PRINCESAS
princesses = []

def actualize_breed(lista):
    allthekimerasforbreed.clear()
    for kim in lista:
        if kim.age > 2:
            allthekimerasforbreed.append(kim)

def actualize_princesses(lista):
    princesses.clear()
    for k in lista:
        if k.age > 2 and k.status == "Princess":
            princesses.append(k)
    
