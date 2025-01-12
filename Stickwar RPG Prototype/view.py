# view.py
import os
from models import List, Player, Character
from typing import List, Dict, Any

class GameView:
    """Handles all game display and user input"""
    def __init__(self):
        self.clear_command = "cls" if os.name == "nt" else "clear"

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system(self.clear_command)

    def display_table(self, headers: List[str], data: List[List[Any]]):
        """Display data in tabulated format"""
        print(data, headers=headers, tablefmt="grid")

    def display_combat_status(self, player: Player, enemy: Character):
        """Display combat information in table format"""
        headers = ["Name", "Health", "Attack"]
        data = [
            [player.name, f"{player.health}/{player.max_health}", player.attack],
            [enemy.name, f"{enemy.health}/{enemy.max_health}", enemy.base_attack]
        ]
        self.display_table(headers, data)

    def display_inventory(self, player: Player):
        """Display inventory in table format"""
        headers = ["Item", "Status"]
        data = [[item, "(Equipped)" if item == player.equipped_weapon else ""] 
                for item in player.inventory]
        self.display_table(headers, data)

    def get_validated_input(self, prompt: str, valid_options: List[str]) -> str:
        """Get and validate user input"""
        while True:
            choice = input(prompt).strip()
            if choice in valid_options:
                return choice
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

    def display_store(self, weapons: Dict[str, int], potion_cost: int):
        """Display store items in table format"""
        headers = ["Item", "Cost"]
        data = [["Potion", potion_cost]] + [[weapon, cost] for weapon, cost in weapons.items()]
        self.display_table(headers, data)