#definindo passivas
class passive:
    def __init__(self, name, description, effect, trigger): #adicionar "TRIGGER" depois
        self.basename= name
        self.level=1
        self.description=description
        self.effect=effect
        self.trigger=trigger

    def passiveactivationtrigger(self, character, damage):
        self.effect(character, damage)

    def nome_modificado(self):
        return f"{self.basename} Lv {self.level}"
    
    def level_up(self):
        self.level+=1
        print(f"{self.basename} leveled up to Lv {self.level}!")