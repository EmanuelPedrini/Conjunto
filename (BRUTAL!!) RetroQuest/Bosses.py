from Enemy import enemy
from ColorText import light_red
class boss(enemy):
    def __init__(self, name, totalmaxhp, atk, atkbonus, vampirism, thorns, dodge, centsondeath, xpondeath, atkdist, intro):
        super().__init__(name, totalmaxhp, atk, atkbonus, vampirism, thorns, dodge, centsondeath, xpondeath, atkdist)
        #Diferenças de Boss enemy!
        self.name = name
        self.intro = intro