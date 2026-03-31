from Passives import passive

def strgonhit(character):
    character.gain_atr("bonusstrg", 1)

def intelonhit(character):
    character.gain_atr("bonusintel", 1)

def intelonspell(character):
    character.gain_atr("bonusintel", 1)

def magicbnsonspell(character):
    character.gain_atr("skillmagicdmgbonus", 1)


#passivas
incansavel= passive("Tireless", "+1 strength when you take damage", strgonhit, "on_damage")
professionalconjurer=passive("Professional Conjurer", "+1 intel when you use a spell", intelonspell, "on_spell")
gg=passive("gg", "gg", intelonhit, "on_damage")
#on_hit
#on_heal
#on_hit
#on_combat_end


#lista de passivas
todasaspassivas =[incansavel]