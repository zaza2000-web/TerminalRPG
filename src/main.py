from character import Warrior
from enemy import Goblin
from battle import battle
import sys


def main():
    # define exemplars
    player = Warrior("Garen")
    goblin = Goblin()
    answer = input("Start game? Yes/No: ")
    running = is_game_start(answer)


    while running:
         try:
              stats = print("1. check your stats")
              exit_game = print("2. exit")
              start_game = print("3. Go battle")
              user_choice = input("Choice: ")
              if user_choice == "1":
                   get_player_statistics(player)
                   continue
              elif user_choice == "2":
                   sys.exit("Goodbye!")
              elif user_choice == "3":
                   battle(player,goblin)
                   break
         except ValueError:
              pass
    
 

def is_game_start(answer):
        if answer == "Yes".lower():
            print("Game is started")
            return True
        else:
            sys.exit("goodbye!")
        
def get_player_statistics(target):
    
    print(f"{target.name} has: ({target.health}/{target.health}HP, Damage: {target.attack_power}. Mana: {target.mana}/{target.mana})")
    


main()