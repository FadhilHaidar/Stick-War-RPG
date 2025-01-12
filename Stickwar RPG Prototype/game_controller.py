# game_controller.py
import random
from models import gameview, Skill, Enemy, Player, Character
from view import GameView


class GameController:
    """Manages game logic and flow"""
    def __init__(self, view: GameView, ):
        self.view = view
        self.weapons = {
            "Sword": 2,
            "Battle Axe": 4,
            "Magic Staff": 6
        }
        self.potion_cost = 1
        self.setup_initial_data()

    def setup_initial_data(self):
        """Initialize game data"""
        # Define skills
        self.rage = Skill(
            name="Rage",
            description="Increases attack speed and damage drastically.",
            defeats=["Bullseye", "Shield Wall"],
            defeated_by=["Dodge", "Summon"],
            success_message="You attack recklessly and deal massive damage!"
        )
        self.bullseye = Skill(
            name="Bullseye",
            description="Shoots an arrow with perfect precision.",
            defeats=["Rage", "Summon"],
            defeated_by=["Shield Wall", "Dodge"],
            success_message="Your arrow hits the enemy's weak spot!"
        )

        # Define enemies
        self.enemies = [
            Enemy(
                name="Goblin",
                max_health=50,
                health=50,
                base_attack=5,
                skills=[self.rage],
                gold_gain=10
            ),
            Enemy(
                name="Juggerknight",
                max_health=120,
                health=120,
                base_attack=20,
                skills=[self.bullseye],
                gold_gain=50
            )
        ]

    def create_player(self, name: str) -> Player:
        """Create a new player character"""
        return Player(
            name=name,
            max_health=100,
            health=100,
            base_attack=10,
            skills=[self.rage, self.bullseye]
        )

    def handle_combat(self, player: Player, enemy: Character) -> bool:
        """Handle combat sequence"""
        while player.health > 0 and enemy.health > 0:
            self.view.clear_screen()
            self.view.display_combat_status(player, enemy)
            choice = self.view.get_validated_input(
                "1. Attack\n2. Use Skill\n3. Drink Potion\n4. Run\nChoice: ",
                ["1", "2", "3", "4"]
            )

            if choice == "1":
                self.handle_attack(player, enemy)
            elif choice == "2":
                self.handle_skill_usage(player, enemy)
            elif choice == "3":
                self.handle_potion_usage(player)
            elif choice == "4":
                if self.handle_run_attempt():
                    return True

            if enemy.health > 0:
                self.handle_enemy_turn(player, enemy)

            input("Press Enter to continue...")

        if player.health > 0:
            print(f"You defeated the {enemy.name}!")
            player.gold_gain += enemy.gold_gain
            print(f"You gained {enemy.gold_gain} gold.")
            enemy.health = enemy.max_health
            return True
        return False

    def handle_attack(self, player: Player, enemy: Character):
        """Handle basic attack"""
        damage = random.randint(player.attack // 2, player.attack)
        enemy.health = max(0, enemy.health - damage)
        print(f"You dealt {damage} damage to the {enemy.name}!")

    def handle_skill_usage(self, player: Player, enemy: Character):
        """Handle skill usage in combat"""
        player_skill = player.choose_skill()
        enemy_skill = enemy.choose_skill()

        if player_skill and enemy_skill:
            print(f"You use {player_skill.name}!")
            print(f"Enemy uses {enemy_skill.name}!")

            if enemy_skill.name in player_skill.defeats:
                print(player_skill.success_message)
                enemy.health = max(0, enemy.health - random.randint(15, 30))
            elif player_skill.name in enemy_skill.defeats:
                print(f"Enemy's {enemy_skill.name} counters your {player_skill.name}!")
                player.health = max(0, player.health - random.randint(15, 30))
            else:
                print("Both skills neutralize each other!")

    def handle_potion_usage(self, player: Player):
        """Handle potion usage"""
        if player.pots > 0:
            player.pots -= 1
            player.health = min(player.health + 50, player.max_health)
            print("You drank a potion!")
        else:
            print("No potions left!")

    def handle_run_attempt(self) -> bool:
        """Handle escape attempt"""
        return random.choice([True, False])

    def handle_enemy_turn(self, player: Player, enemy: Character):
        """Handle enemy turn in combat"""
        enemy_damage = random.randint(enemy.base_attack // 2, enemy.base_attack)
        player.health = max(0, player.health - enemy_damage)
        print(f"The {enemy.name} dealt {enemy_damage} damage to you!")

    def run(self):
        """Main game loop"""
        self.view.clear_screen()
        print("Welcome to the RPG Game!")
        choice = self.view.get_validated_input(
            "1. Start New Game\n2. Load Game\n3. Exit\nChoice: ",
            ["1", "2", "3"]
        )

        player = None
        if choice == "1":
            try:
                name = input("Enter your character's name: ")
                if not name.strip():
                    raise ValueError("Name cannot be empty")
                player = self.create_player(name)
            except ValueError as e:
                print(f"Error: {e}")
                return
        elif choice == "2":
            player = self.state.load_game()
            if not player:
                print("No save file found or error loading game.")
                return
        else:
            print("Goodbye!")
            return

        self.game_loop(player)

    def game_loop(self, player: Player):
        """Main game loop"""
        while True:
            self.view.clear_screen()
            self.view.display_table(
                ["Stats", "Value"],
                [
                    ["Name", player.name],
                    ["Health", f"{player.health}/{player.max_health}"],
                    ["Attack", player.attack],
                    ["Gold", player.gold_gain],
                    ["Potions", player.pots]
                ]
            )

            choice = self.view.get_validated_input(
                "1. Fight\n2. Store\n3. Inventory\n4. Save\n5. Exit\nChoice: ",
                ["1", "2", "3", "4", "5"]
            )

            if choice == "1":
                enemy = random.choice(self.enemies)
                self.handle_combat(player, enemy)
            elif choice == "2":
                self.handle_store(player)
            elif choice == "3":
                self.handle_inventory(player)
            elif choice == "4":
                if self.state.save_game(player):
                    print("Game saved successfully!")
                input("Press Enter to continue...")
            else:
                print("Goodbye!")
                break

    def handle_store(self, player: Player):
        """Handle store interactions"""
        self.view.clear_screen()
        print("Welcome to the store!")
        self.view.display_store(self.weapons, self.potion_cost)
        
        options = {
            "1": ("Sword", self.weapons["Sword"]),
            "2": ("Battle Axe", self.weapons["Battle Axe"]),
            "3": ("Magic Staff", self.weapons["Magic Staff"]),
            "4": ("Potion", self.potion_cost)
        }
        
        choice = self.view.get_validated_input(
            "Choose item to buy (5 to exit): ",
            list(options.keys()) + ["5"]
        )

        if choice == "5":
            return

        item, cost = options[choice]
        if player.gold_gain >= cost:
            player.gold_gain -= cost
            if item == "Potion":
                player.pots += 1
                print("You bought a potion!")
            else:
                player.inventory.append(item)
                print(f"You bought a {item}!")
        else:
            print("Not enough gold!")
        input("Press Enter to continue...")

    def handle_inventory(self, player: Player):
        """Handle inventory management"""
        while True:
            self.view.clear_screen()
            self.view.display_inventory(player)
            choice = self.view.get_validated_input(
                "Choose item number to equip (0 to go back): ",
                ["0"] + [str(i) for i in range(1, len(player.inventory) + 1)]
            )

            if choice == "0":
                break

            idx = int(choice) - 1
            selected_item = player.inventory[idx]
            if selected_item == player.equipped_weapon:
                print(f"{selected_item} is already equipped.")
            else:
                player.equipped_weapon = selected_item
                print(f"You have equipped {selected_item}.")
            input("Press Enter to continue...")