from Passives import passive

def strgonhit(character, damage):
    character.gain_atr("bonusstrg", 1)
#passivas
# brutamontes= passive("Brute", "You dont fear Anyone, you gain", 0 )
# assassin= passive("Assassin", "You blablabla", 0)
# parede = passive("Human Wall", "Galhofinhas", 0)
incansavel= passive("Tireless", "Gugu dada", strgonhit, "on_damage")

#lista de passivas
todasaspassivas =[incansavel]