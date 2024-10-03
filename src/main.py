from character import Warrior
from enemy import Goblin
from battle import battle


def main():
    # define exemplars
    player = Warrior("Garen")
    goblin = Goblin()
    answer = input("Start game? Yes/No: ")
    running = is_game_start(answer)
    
 

def is_game_start(answer):
        if answer == "Yes".lower():
            print("Game is started")
            return True
        else:
            return False

     

main()