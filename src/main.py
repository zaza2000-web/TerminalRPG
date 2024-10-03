from character import Warrior
from enemy import Goblin
from battle import battle


def main():
    # define exemplars
    player = Warrior("Garen")
    goblin = Goblin()
    answer = input("Start game? Yes/No: ")
    is_game_start(answer)
    while is_game_start(answer):
         ...
 

def is_game_start(answer):
        if answer == "Yes".lower():
            print("Game starting")
            return True
        else:
            return False

main()