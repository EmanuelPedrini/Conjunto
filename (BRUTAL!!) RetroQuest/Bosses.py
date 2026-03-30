from Enemy import enemy
class boss(enemy):
    def __init__(self, name, totalmaxhp, atk, atkbonus, vampirism, thorns, dodge, centsondeath, xpondeath, atkdist):
        super().__init__(name, totalmaxhp, atk, atkbonus, vampirism, thorns, dodge, centsondeath, xpondeath, atkdist)
        #Diferenças de Boss enemy!
        