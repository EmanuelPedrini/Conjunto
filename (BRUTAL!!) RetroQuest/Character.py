import random
from utils import rolld100
import sys
from Passive_Data import todasaspassivas
from Skill_Data import todasskills
from Atribute_Rewards_Data import todososgatr
from Commands import input_player
from ColorText import *

class character:
    def __init__(self, name, pronoun, possessive, strg, dex, vit, luck, cha, intel, dodge, vampirism, thorns, armor, 
                 skills, passives, inbornpassives, shieldstat, atkform, cents):
        #textos
        self.name = name 
        self.pronoun = pronoun
        self.possessive = possessive

        self.atkdmgbonus = 0
        self.bonusstrg=0
        self.bonusdex=0
        self.bonusvit=0
        self.bonusintel=0

       

        #estados (não do brasil, lengo lengo lengo)
        self.stunned = False

        #atributes
        self.strg=strg
        self.totalstrg = int(self.strg + self.bonusstrg)

        #dex
        self.dex = int(dex)
        self.totaldex = int(self.dex + self.bonusdex)

        #vit
        self.vit = int(vit)
        self.totalvit = int(self.vit + self.bonusvit)

        self.luck = int(luck)

        self.cha = int(cha)

        self.intel=int(intel)
        self.totalintel = int(self.intel + self.bonusintel)

        #secondary atributes
        self.vampirism=vampirism
        self.realvampirism=float(vampirism*0.01)
        self.thorns=thorns
        self.armor = armor
        self.dodge = dodge 
        self.totaldodge = int(min(5 * self.totaldex + self.dodge, 75))
        self.critchance = 4 * luck
        bonuscritchance = 0
        self.totalcritchance = int(self.critchance + bonuscritchance)
        self.critmult = 2

        self.inbornpassives=inbornpassives
        self.atkform=atkform

        self.skillmagicdmgbonus=0
        self.skillcostmodifier=0

        self.shield = 0
        self.shieldstat = shieldstat

        #level system
        self.level=int(1)
        self.xp=int(0)
        self.xptonext=int(100)

        #calculo de hp maximo
        self.bonushp=0
        self.maxhp= 5 * self.totalvit
        self.totalmaxhp = self.maxhp + self.bonushp
        self.acthp = self.totalmaxhp

        #inventory system
        #inventario é so uma big lista anota ai
        self.inventory =[]

        self.equipments = {
            "Weapon": None,
            "Armor": None,
            "Accessory": None
        }

        #skills pqp
        self.skills= skills
        self.passives = passives
        self.maxskills = 4
        self.maxpassives = 2

        #dineiro
        self.cents=int(cents)

        #mana
        self.maxmana = 5 * self.cha
        self.manaregen = self.totalintel
        self.manainicial = self.cha
        self.actmana = self.manainicial
    
    #definições de sistema de Inventário
    def updating_atributes(self):
        self.maxhp=5*self.vit
        self.totalmaxhp = self.maxhp + self.bonushp
        if self.acthp > self.totalmaxhp:
            self.acthp=self.totalmaxhp
        self.maxmana=5*self.cha
        if self.actmana> self.maxmana:
            self.actmana=self.maxmana
        self.totalstrg = int(self.strg + self.bonusstrg)
        self.totalvit = int(self.vit + self.bonusvit)
        self.totaldex = int(self.dex + self.bonusdex)
        self.totalintel = int(self.intel + self.bonusintel)
        self.manaregen = self.totalintel

        self.totaldodge = min(5 * self.dex + self.dodge, 75)
        self.totalcritchance = 4 * self.luck + self.critchance
        self.realvampirism = float(self.vampirism*0.01)
        self.manainicial=self.cha

    def gain_atr(self, attr, amount):
        setattr(self, attr, getattr(self, attr) + amount)
        self.updating_atributes()

    def lose_atr(self, attr, amount):
        setattr(self, attr, getattr(self, attr) - amount)
        self.updating_atributes()

    def add_item(self, item):
            self.inventory.append(item)
            print(yellow(f"> You obtained {item.name}!"))

    def remove_item(self, item):
            if item in self.inventory:
                self.inventory.remove(item)
                print(red(f"> {item.name} got removed from your inventory!"))
            else:
                print(yellow("> That item isn`t in your inventory"))

    def itemequipped(self, item):
        for atrr, value in item.bonus.items():
            if hasattr(self, atrr):
                self.gain_atr(atrr, value)
            if item.slot=="Weapon":
                self.atkform=item.atkform

    def itemunequipped(self,item):
        for atrr, value in item.bonus.items():
            if hasattr(self, atrr):
                self.gain_atr(atrr, -value)
            if item.slot=="Weapon":
                self.atkform = "melee"

    def itemremove(self, slot):
        retirado2=self.equipments.get(slot)
        if retirado2 is not None:
            retirado2 = self.equipments[slot]
            self.itemunequipped(retirado2)
            self.inventory.append(retirado2)
            self.equipments[slot]=None
            print(red(f"> You unequipped [ {retirado2.name} ]!"))
        else:
            print(red("No items equipped!"))
        

    def equip(self,item):
        #so muda slot pra slot do item em questão
        slot = item.slot

        #removendo item se ja tem algo equipado
        if self.equipments[slot] is not None:
            retirado = self.equipments[slot]
            self.itemunequipped(retirado)
            self.inventory.append(retirado)
            print(red(f"> You unequipped [ {retirado.name} ]!"))

        self.equipments[slot] = item
        if item in self.inventory:
            self.inventory.remove(item)
            print(yellow(f"> Equipped {item.name}"))
        #
        self.itemequipped(item)
    def gain_shield(self, amount):
            self.shield+=amount
            print(yellow(f"You gained {amount} Shield Points!"))

        #regenerar mana
    def regen_mana(self):
        self.updating_atributes()
        self.actmana += self.manaregen
        print(light_cyan(f"{self.name} regenerated {self.manaregen} Mana Points!"))
        if self.actmana > self.maxmana:
            self.actmana = self.maxmana

        #ganhar mana != regenerar mana
    def gain_mana(self, amount):
        self.actmana += amount
        if self.actmana > self.maxmana:
            self.actmana = self.maxmana
        print(light_cyan(f"{self.name} obtained {amount} Mana Points! \nNow {self.pronoun} have [ {self.actmana} / {self.maxmana} ] Mana Points"))

    def mana_use(self, amountused):
        if self.actmana >= amountused:
            print(f"You actually have [ {self.actmana} / {self.maxmana} ] Mana Points! This is enough to cast this Ability!")
            self.actmana -= amountused
            print(f"Now you have [ {self.actmana} / {self.maxmana} ] Mana Points!")
           
        
    #BASIC ATTACK
    def basicattack(self, target, player):
            #rola o Dado
            roll = rolld100()
            rollcrit = rolld100()
            if roll > target.dodge:
                #Computa o Dano
                randomdmg = int((self.totalstrg * 0.75 )+ random.randint(0, int(self.totalstrg * 0.5)))
                damage = randomdmg + self.atkdmgbonus
                crit = False
                if rollcrit < self.totalcritchance:
                    damage *= self.critmult
                    crit = True
                
                if crit==True:
                    print(f"> The [ {self.name} ] got A BRUTAL HIT!! Dealing [ {damage} ] MASSIVE DAMAGE to [ {target.name}!!]")
                else:
                    print(f"> The [ {self.name} ] HIT! Dealing [ {damage} ] DAMAGE to [ {target.name} ]")
                #Computa o tanto que tu curo com o ataque
                if self.vampirism != 0:
                    player.heal(max(1, int(damage*(self.realvampirism))))
                
                #Computa se o alvo tem Thorns
                if target.thorns != 0 and self.atkform=="melee":
                    Espinhado= int(target.thorns)
                    player.toma(int(Espinhado))
                    print(f"> You taked [ {Espinhado} ] damage from the enemy thorns!")
                
                for pas in player.passives:
                    if pas.trigger=="on_hit":
                        pas.passiveactivationtrigger(self, damage)
                
                target.toma(damage, player)

                # if target.
                if target.acthp <= 0:
                    return
            else:
                print(f"You missed {target.name}, you rolled [ {roll} ] !")

    def toma(self, damage):

        if damage>self.shield:
            self.acthp -= (damage - self.shield)
            self.shield=0

        else:
            self.shield -= damage

        for p in self.passives:
            if p.trigger=="on_damage":
                p.passiveactivationtrigger(self)
        self.death()

    def heal(self, amount):
        self.acthp += amount
        print(light_green(f"> {self.name} healed [ {amount} ] Hp"))
        if self.acthp > self.totalmaxhp:
            self.acthp = self.totalmaxhp
            for pas in self.passives:
                if pas.trigger=="on_heal":
                    pas.passiveactivationtrigger(self)


    
    def gain_xp(self, xpamount):
        self.xp+=xpamount
        print(f"> {self.name} gained {xpamount} xp!")

    def gain_cents(self, amount):
        self.cents+=amount
        print(f"> {self.name} gained {amount} cents!")

    def lose_cents(self, amount):
        self.cents -=amount
        print(f"> {amount} cents got away from your wallet!")

    def level_system(self):
        if self.xp>=self.xptonext:
            self.xp -= self.xptonext
            self.level +=1
            print(f"> The {self.name}  leveled up! Now {self.pronoun} is level {self.level}!")
            self.level_up_rewards()
            self.xptonext = int(100 * (1.5 ** (self.level - 1)))
    
    def level_up_rewards(self):
        wh
        totaloptions=[]
        totaloptions += random.sample(todososgatr, min(4, len(todososgatr)))

        #definindo se tu pode receber passivas
        if len(self.passives) < self.maxpassives:
            totaloptions += random.sample(todasaspassivas, min (4, len(todasaspassivas)))

        #mema traquera mas comm skills
        if len(self.skills) < self.maxskills:
            totaloptions += random.sample(todasskills, min (4, len(todasskills)))

        #receba tributos
        if not (len(self.passives) < self.maxpassives) and not (len(self.skills) < self.maxskills):
            totaloptions = random.sample(todososgatr, 4)
        currentoptions = []
        currentoptions = random.sample(totaloptions, 3)

        for x, y in enumerate(currentoptions):
            print(f"{x+1} - {y.basename}")

        choice = input_player(player=self, actenemy=None)
        if choice.isdigit():
            sd=int(choice)-1
            if 0<= sd < len(currentoptions):
                slc= currentoptions[sd]

                if slc in todasaspassivas:
                    self.passives.append(slc)
                    print(f"{slc.basename} added to your skills!")
                elif slc in todasskills:
                    self.skills.append(slc)
                    print(f"{slc.basename} added to your skills!")
                elif slc in todososgatr:
                    slc.apply(self)
                    print(f"you gained {slc.basename}!")
            else:
                print("Invalid Choice")
                return
        else:
            print("Invalid Option")
            return


    def death(self):
        if self.acthp<=0:
            print(f"the {self.name} got killed by a enemy and died in a horrible way!")
            sys.exit()
        