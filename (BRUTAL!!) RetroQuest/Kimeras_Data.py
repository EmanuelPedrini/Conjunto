from Kimera import kimera
from Skill_Data import *

allkimeras = []
allthekimerasforbreed=[]
princesses = []

def actualize_breed(lista):
    allthekimerasforbreed.clear()
    for i in lista:
        if i.age > 1:
            allthekimerasforbreed.append(i)

def actualize_princesses(lista):
    princesses.clear()
    for k in lista:
        if k.age > 1 and k.status == "Princess":
            princesses.append(k)
    
