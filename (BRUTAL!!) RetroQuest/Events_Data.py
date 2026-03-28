from Event import event
import random
from Globals import *
from Combat import combat
from Enemies_Data import marshmallowknight
#eventos neutros

def nothing(player):
    print("Nothing Happens, but sometimes...")

def avoid(player):
    roll= random.randint(1,20) + player.dex
    if roll < 12:
        dmg=random.randint(6,12)*globaldangermathsoftcap
        player.toma(int(dmg))
    else:
        print("You avoided the trap in a involuntary reflex!")
def drinkfountain(player):
    roll= random.randint(1,20) + player.luck
    if roll > 7:
        hl= random.randint(9,16)*globaldangermathsoftcap
        player.heal(int(hl))
        print(f"The water have a taste of marshmallows and honey, you fell your body get refilled with jovial energy!")
    elif roll<=7:
        actenemy=[marshmallowknight]
        combat(player, actenemy)

pedrasnocaminho=event("Stones in the path", "You encounter different rocks in the path and you decide to take a look",
    [
    ("Look under the rocks", nothing)
    ]
)

neutralevents=[pedrasnocaminho]

#eventos ruins
pisadaemarmadilha=event(
    "Pisada na armadilha", "In a moment of distraction, you look to the black skies of decandent world and comtemplate your existence, as you" \
    "return to reality, you realize that your feet is going on the direction of a BEAR TRAP!",
    [
        ("Avoid!", avoid)
    ]
)

badevents=[pisadaemarmadilha]

#eventos bons
fontedecura = event(
    "Fonte de Cura", "You found a imposing fountain with healing magic simbols, Drink?",
    [
        ("Ignore", nothing),
        ("Drink", drinkfountain)
    ]
)

goodevents=[fontedecura]

#adicionar no futuro
# ultraevents=[]