class Goblin:
    def __init__(self,name="Hermet",health=700,mana=35,max_mana=40,attack_power=75):
        self.health = health
        self.mana = mana
        self.max_mana = max_mana
        self.attack_power = attack_power
        self.name = name
    
    # check if goblin is alive

    def is_goblin_alive(self):
        return self.health > 0

    # add attack logic

    def attack(self,enemy):
        if self.is_goblin_alive():
            print(f"{self.name} attack {enemy.name} he deal {self.attack_power}")
            enemy.health -= self.attack_power
        else:
            print(f"{self.name} defeated by {enemy.name}")