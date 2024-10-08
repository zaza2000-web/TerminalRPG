from character import Character,Warrior # import class character
from enemy import Goblin # import calss enemy


def battle(player,goblin):
    print("Battle starts! destroy him")


    # check buffs

    if isinstance(player,Warrior):
        action = input("Choose an action (roar, eat, sleep):").lower()

        if action == "roar":
            print(player.warrior_roar())
        elif action == "eat":
            print(player.warrior_eat())
        elif action == "sleep":
            print(player.warrior_sleep())
        else:
            print("Invalid buff, attack default")
        

    while player.is_alive_character() and goblin.is_goblin_alive():
        # player's turn
        player.attack(goblin)
        if not goblin.is_goblin_alive():
            print(f"Goblin {goblin.name} has been defeated")
            break

        # enemy's turn
        goblin.attack(player)
        if not player.is_alive_character():
            print(f"Player {player.name} has been defeated by {goblin.name}")
            break

