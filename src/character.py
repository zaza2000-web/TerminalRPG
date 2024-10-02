class Character:
    # constructor for character
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    # check character's health
    def is_alive_character(self):
        return self.health > 0
    
    # make a logic how to attack
    def attack(self,enemy):
        if self.is_alive_character():
            print(f"{self.name} attack {enemy} which {self.attack_power}")
            enemy.health -= self.attack_power    
        else:
            print(f"{self.name} is defeated by {enemy.name}")


# make warrior class
class Warrior(Character):
    def __init__(self,name,health = 500,attack_power = 40, mana = 50):
        super().__init__(name)
        self.health = health
        self.attack_power = attack_power
        self.mana = mana
        self.max_mana = mana
        self.recovery = False
    
    # check if mana's value is enought for do something

    def _check_mana(self,cost):
        if self.mana >= cost:
            self.mana -= cost
            return True
        else:
            return False
    
    # there i make buff's for warrior class

    # this is buff for +30hp when he roar he get this buff
    def warrior_roar(self):
        cost = 10
        if self._check_mana(cost):
            self.health  += 30
            return f"{self.name} start roar and get +30hp. currnet hp is: {self.health}"
        else:
            return f"not enought mana {self.name} have {self.mana} but u need {cost}  for use 'Roar' "

    # warrior eating some food still he get +5 to his attack_power need mana also 10
    def warrior_eat(self):
        cost = 10
        if self._check_mana(cost):
            self.attack_power += 5
            return f"{self.name} got +5 to power. currnet power is: {self.attack_power}"
        else:
            return f"not enought mana {self.name} have {self.mana} but u need {cost}  for use 'Eat' "
    # warrior can sleep and recovery his mana +5 but max is 50 for this class 
    def warrior_sleep(self):
        
  


        
