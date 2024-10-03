class Goblin:
    def __init__(self,health=700,mana=35,max_mana=40,attack_power=75):
        self.health = health
        self.mana = mana
        self.max_mana = max_mana
        self.attack_power = attack_power
    
    # check if goblin is alive

    def is_goblin_alive(self):
        return self.health > 0

