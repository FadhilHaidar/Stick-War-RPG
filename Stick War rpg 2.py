import os
import random
import pickle
from dataclasses import dataclass, field
from typing import List, Callable, Dict

# Constants
WEAPONS = {"Great Sword": 40, "Battle Axe": 60, "Magic Staff": 80}
POTION_COST = 10
CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"

@dataclass
class Skill:
    name: str
    description: str
    defeats: List[str]  # Skills this skill can defeat
    defeated_by: List[str]  # Skills that can defeat this skill
    success_message: str

@dataclass
class Character:
    name: str
    max_health: int
    health: int
    base_attack: int
    skills: List[Skill] = field(default_factory=list)
    gold_gain: int = 0

    def choose_skill(self) -> Skill:
        return random.choice(self.skills)

@dataclass
class Player(Character):
    inventory: List[str] = field(default_factory=lambda: ["Rusty Sword"])
    equipped_weapon: str = "Rusty Sword"
    pots: int = 0

    @property
    def attack(self) -> int:
        weapon_bonus = {
            "Rusty Sword": 5,
            "Great Sword": 15,
            "Battle Axe": 20,
            "Magic Staff": 25
        }.get(self.equipped_weapon, 0)
        return self.base_attack + weapon_bonus

def clear_screen():
    os.system(CLEAR_COMMAND)

def save_game(player: Player):
    with open('savefile', 'wb') as f:
        pickle.dump(player, f)
    print("Game saved!")

def load_game() -> Player:
    if os.path.exists("savefile"):
        with open('savefile', 'rb') as f:
            return pickle.load(f)
    else:
        print("No save file found.")
        return None

def display_stats(player: Player):
    print(f"Name: {player.name}")
    print(f"Health: {player.health}/{player.max_health}")
    print(f"Attack: {player.attack}")
    print(f"Gold: {player.gold_gain}")
    print(f"Potions: {player.pots}")
    print(f"Equipped Weapon: {player.equipped_weapon}")

def manage_inventory(player: Player):
    while True:
        clear_screen()
        print("Inventory:")
        for idx, item in enumerate(player.inventory, 1):
            equipped = "(Equipped)" if item == player.equipped_weapon else ""
            print(f"{idx}. {item} {equipped}")
        print("b. Back")
        choice = input("Choose an item to equip or 'b' to go back: ")

        if choice == "b":
            break

        if choice.isdigit() and 1 <= int(choice) <= len(player.inventory):
            selected_item = player.inventory[int(choice) - 1]
            if selected_item == player.equipped_weapon:
                print(f"{selected_item} is already equipped.")
            else:
                player.equipped_weapon = selected_item
                print(f"You have equipped {selected_item}.")
        else:
            print("Invalid choice.")
        input("Press Enter to continue...")

# Predefined Skills
rage = Skill(
    name="Rage",
    description="Increases attack speed and damage drastically.",
    defeats=["Bullseye", "Shield Wall"],
    defeated_by=["Dodge", "Summon"],
    success_message="You attack recklessly and deal massive damage!"
)

bullseye = Skill(
    name="Bullseye",
    description="Shoots an arrow with perfect precision.",
    defeats=["Rage", "Summon"],
    defeated_by=["Shield Wall", "Dodge"],
    success_message="Your arrow hits the enemy's weak spot!"
)

# Predefined Enemies
goblin = Character(
    name="Goblin",
    max_health=50,
    health=50,
    base_attack=5,
    skills=[rage],
    gold_gain=10
)
juggerknight = Character(
    name="Juggerknight",
    max_health=120,
    health=120,
    base_attack=20,
    skills=[bullseye],
    gold_gain=50
)

def fight(player: Player, enemy: Character):
    while player.health > 0 and enemy.health > 0:
        clear_screen()
        print(f"{player.name} vs {enemy.name}")
        print(f"{player.name}'s Health: {player.health}/{player.max_health}")
        print(f"{enemy.name}'s Health: {enemy.health}/{enemy.max_health}")
        print("1. Attack\n2. Use Skill\n3. Drink Potion\n4. Run")
        choice = input("-> ")

        if choice == "1":
            damage = random.randint(player.attack // 2, player.attack)
            enemy.health -= damage
            print(f"You dealt {damage} damage to the {enemy.name}!")
        elif choice == "2":
            player_skill = random.choice(player.skills)
            enemy_skill = enemy.choose_skill()
            print(f"You use {player_skill.name}!")
            print(f"Enemy uses {enemy_skill.name}!")

            if enemy_skill.name in player_skill.defeats:
                print(player_skill.success_message)
                enemy.health -= random.randint(15, 30)
            elif player_skill.name in enemy_skill.defeats:
                print(f"Enemy's {enemy_skill.name} counters your {player_skill.name}!")
                player.health -= random.randint(15, 30)
            else:
                print("Both skills neutralize each other!")
        elif choice == "3":
            if player.pots > 0:
                player.pots -= 1
                player.health = min(player.health + 50, player.max_health)
                print("You drank a potion!")
            else:
                print("No potions left!")
        elif choice == "4":
            if random.choice([True, False]):
                print("You successfully ran away!")
                return
            else:
                print("You failed to escape!")
        else:
            print("Invalid choice!")
            continue

        if enemy.health > 0:
            enemy_damage = random.randint(enemy.base_attack // 2, enemy.base_attack)
            player.health -= enemy_damage
            print(f"The {enemy.name} dealt {enemy_damage} damage to you!")

        input("Press Enter to continue...")

    if player.health > 0:
        print(f"You defeated the {enemy.name}!")
        player.gold_gain += enemy.gold_gain
        print(f"You gained {enemy.gold_gain} gold.")
    else:
        print("You have been defeated...")

    enemy.health = enemy.max_health
    input("Press Enter to continue...")

def main():
    clear_screen()
    print("Welcome to the RPG Game!")
    print("1. Start New Game\n2. Load Game\n3. Exit")
    choice = input("-> ")

    if choice == "1":
        name = input("Enter your character's name: ")
        player = Player(
            name=name,
            max_health=100,
            health=100,
            base_attack=10,
            skills=[rage, bullseye]
        )
    elif choice == "2":
        player = load_game()
        if not player:
            main()
            return
    elif choice == "3":
        print("Goodbye!")
        return
    else:
        print("Invalid choice!")
        main()
        return

    while True:
        clear_screen()
        display_stats(player)
        print("1. Fight\n2. Store\n3. Inventory\n4. Save\n5. Exit")
        choice = input("-> ")

        if choice == "1":
            enemy = random.choice([goblin, juggerknight])
            fight(player, enemy)
        elif choice == "2":
            clear_screen()
            print("Welcome to the store!")
            print(f"1. Buy Great Sword ({WEAPONS['Great Sword']} gold)\n2. Buy Potion ({POTION_COST} gold)\n3. Buy Battle Axe ({WEAPONS['Battle Axe']} gold)\n4. Buy Magic Staff ({WEAPONS['Magic Staff']} gold)\n5. Exit")
            store_choice = input("-> ")
            if store_choice == "1" and player.gold_gain >= WEAPONS["Great Sword"]:
                player.gold_gain -= WEAPONS["Great Sword"]
                player.inventory.append("Great Sword")
                print("You bought a Great Sword!")
            elif store_choice == "2" and player.gold_gain >= POTION_COST:
                player.gold_gain -= POTION_COST
                player.pots += 1
                print("You bought a potion!")
            elif store_choice == "3" and player.gold_gain >= WEAPONS["Battle Axe"]:
                player.gold_gain -= WEAPONS["Battle Axe"]
                player.inventory.append("Battle Axe")
                print("You bought a Battle Axe!")
            elif store_choice == "4" and player.gold_gain >= WEAPONS["Magic Staff"]:
                player.gold_gain -= WEAPONS["Magic Staff"]
                player.inventory.append("Magic Staff")
                print("You bought a Magic Staff!")
            elif store_choice in ["1", "2", "3", "4"]:
                print("Not enough gold!")
            elif store_choice == "5":
                continue
            else:
                print("Invalid choice!")
            input("Press Enter to continue...")
        elif choice == "3":
            manage_inventory(player)
        elif choice == "4":
            save_game(player)
            input("Press Enter to continue...")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
