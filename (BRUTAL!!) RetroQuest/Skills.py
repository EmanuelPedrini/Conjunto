
class skill:
    def __init__(self, name, description, damage=0, heal=0, cost=0, target="enemy"):
          other=0
          self.basename = name
          self.level=1
          self.description=description
          self.damage=damage
          self.cost=cost
          self.costmodifier=0
          self.heal=heal
          self.target=target

    @property
    def total_mana_cost(self):
          return max(1, self.cost + self.costmodifier)
          

    def nome_modificado(self):
        return f"{self.basename} Lv {self.level}"
    
    def level_up(self):
        self.level+=1
        print(f"{self.basename} leveled up to Lv {self.level}!")

    def use(self, player, escolhadealvo, actenemy):
            if player.actmana<self.cost:
                   print(f"You actually have [ {player.actmana} / {player.maxmana} ] Mana Points! This isn`t enough to cast this Ability!")
                   return
            
            player.mana_use(self.cost)

            if self.target=="self":
                  if self.heal!=0:
                        player.heal(self.heal)
                  return
            
            if self.target=="enemy":
                  if self.damage!=0:
                        target = escolhadealvo(player, actenemy)

                        print(f"{player.name} used {self.basename} dealing {self.damage} damage to {target.name}")
                        target.toma(self.damage, player)

                  if target.acthp<=0 and target in actenemy:
                        actenemy.remove(target)
                  return

            if self.target=="allenemies":
                  print(f"{player.name} used {self.basename}!")
                  if self.damage!=0:
                        dmgs = self.damage
                        for e in actenemy:
                             e.toma(dmgs, player)
                             print(f"{player.name} dealed {dmgs} DAMAGE to {e.name}!")
                             if e.acthp<=0:
                              actenemy.remove(e)
                  return