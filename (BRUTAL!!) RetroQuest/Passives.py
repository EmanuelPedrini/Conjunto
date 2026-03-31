#definindo passivas
class passive:
    def __init__(self, name, text, effect, trigger): #adicionar "TRIGGER" depois
        self.basename= name
        self.level=1
        self.text=text
        self.effect=effect
        self.trigger=trigger

    def passiveactivationtrigger(self, kimera):
        self.effect(kimera)

    def nome_modificado(self):
        return f"{self.basename} Lv {self.level}"
    
    def level_up(self):
        self.level+=1
        print(f"{self.basename} leveled up to Lv {self.level}!")