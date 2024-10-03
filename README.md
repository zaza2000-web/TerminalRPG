# Battle Game - Warrior vs Goblin

### Description

Welcome to **Battle Game** — a text-based RPG where you control a warrior fighting against a goblin! This game was created to demonstrate basic **Python** skills, including **Object-Oriented Programming (OOP)**, user interaction, and basic game mechanics.

### Features

- The player controls a warrior with health, attack power, and mana.
- The warrior can use various **buffs** to enhance stats:
  - **Roar** — increases health by 30 points.
  - **Eat** — increases attack power by 5 points.
  - **Sleep** — restores mana by 5 points (one-time use per battle).
- The player can attack the enemy, and the enemy will counterattack.
- The battle continues until one character loses all their health.

### Installation and Setup

1. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/zaza2000-web/TerminalRPG.git
    ```

2. Navigate to the project folder:
    ```bash
    cd battle-game
    ```

3. Make sure you have Python 3 installed. You can check this by running:
    ```bash
    python --version
    ```

4. Run the game:
    ```bash
    python main.py
    ```

### How to Play

1. After launching the game, you'll be prompted to start the battle with a goblin.
2. You can choose actions for your warrior:
   - **Roar**: increases health (costs 10 mana).
   - **Eat**: increases attack power (costs 10 mana).
   - **Sleep**: restores mana (once per battle, +5 mana).
3. After choosing your buffs, the battle will begin, and your warrior will attack the goblin while the goblin counters.
4. The game continues until one of the characters loses all health.

### Example Usage

