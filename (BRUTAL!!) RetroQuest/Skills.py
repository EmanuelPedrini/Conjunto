
class skill:
    def __init__(self, name, text, damage=0, heal=0, cost=0, target="enemy"):
          other=0
          self.basename = name
          self.level=1
          self.text=text
          self.damage=damage
          self.cost=cost
          self.heal=heal
          self.target=target

    def total_mana_cost(self, player):
          return max(1, self.cost - player.skillcostmodifier)
    @property
    def total_skill_damage(self, player):
          return max(1, self.damage + player.skillmagicdmgbonus)
          

    def nome_modificado(self):
        return f"{self.basename} Lv {self.level}"
    
    def level_up(self):
        self.level+=1
        print(f"{self.basename} leveled up to Lv {self.level}!")

    def use(self, player, escolhadealvo, actenemy):
            cos = self.total_mana_cost(player)
            if player.actmana < cos:
                   print(f"You actually have [ {player.actmana} / {player.maxmana} ] Mana Points! This isn`t enough to cast this Ability!")
                   return
            
            player.mana_use(cos)

            for sp in player.passives:
                  if sp.trigger=="on_spell":
                        sp.passiveactivationtrigger(self)


            if self.target=="self":
                  if self.heal!=0:
                        player.heal(self.heal)
                  return
            
            if self.target=="enemy":
                  if self.damage!=0:
                        dmgt=self.total_skill_damage
                        target = escolhadealvo(player, actenemy)

                        print(f"{player.name} used {self.basename} dealing {dmgt} damage to {target.name}")
                        target.toma(dmgt, player)

                  if target.acthp<=0 and target in actenemy:
                        actenemy.remove(target)
                  return

            if self.target=="allenemies":
                  print(f"{player.name} used {self.basename}!")
                  if self.damage!=0:
                        dmgs = self.total_skill_damage
                        for e in actenemy:
                             e.toma(dmgs, player)
                             print(f"{player.name} dealed {dmgs} DAMAGE to {e.name}!")
                             if e.acthp<=0:
                              actenemy.remove(e)
                  return