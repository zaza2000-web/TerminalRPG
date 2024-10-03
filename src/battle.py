from character import Character,Warrior # import class character
from enemy import Goblin # import calss enemy


def battle(player,goblin):
    print("Battle starts! destroy him")

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

if __name__ == "__main__":
    player = Warrior("Garen")
    goblin = Goblin()

    battle(player,goblin)