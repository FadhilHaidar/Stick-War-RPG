import random

# Classes for game components
class Skill:
    def __init__(self, name, counter, effect):
        self.name = name
        self.counter = counter  # The type this skill counters
        self.effect = effect  # Description of the skill's effect

class Character:
    def __init__(self, name, char_class, skills):
        self.name = name
        self.char_class = char_class
        self.hp = 100  # Default HP
        self.skills = skills  # List of Skill objects

class Enemy:
    def __init__(self, name, skill):
        self.name = name
        self.hp = 100  # Default HP
        self.skill = skill  # Skill object

# Initialize skills
fireball = Skill("Spear", counter="Shield", effect="Menusuk Musuh")
shield = Skill("Shield", counter="Knive", effect="Menahan serangan")
sword_strike = Skill("Knive", counter="Spear", effect="menebas slash")

# Sample characters and enemies
player = Character("Atrey", "Spearton", [fireball, shield, sword_strike])
goblin = Enemy("Clawler", sword_strike)

# ASCII Art for visuals
def show_ascii_art(entity):
    if isinstance(entity, Character):
        print(f"[ {entity.name} ]")
    elif isinstance(entity, Enemy):
        print(f"[ {entity.name} ]")


# Combat System
def combat(player, enemy):
    print("\nA wild enemy appears!")
    show_ascii_art(enemy)

    while player.hp > 0 and enemy.hp > 0:
        print("\nPilih skill yang ingin kamu gunakan:")
        for i, skill in enumerate(player.skills):
            print(f"{i + 1}. {skill.name} - {skill.effect}")
        
        choice = int(input("Enter skill number: ")) - 1
        player_skill = player.skills[choice]

        print(f"Kamu menggunakan {player_skill.name}!")

        # Determine combat outcome
        if player_skill.counter == enemy.skill.name:
            print(f"{player_skill.name} kamu mengalahkan {enemy.skill.name}! Kamu memenangkan pertempuran!")
            return "Menang"
        elif enemy.skill.counter == player_skill.name:
            print(f" {enemy.skill.name} musuh menahan {player_skill.name}! kamu kalah!")
            return "Kalah"
        else:
            print("Tidak terjadi apa-apa! Coba lagi!")

# Exploration System
def explore():
    print("\nKamu sedang menjelajah...")
    event = random.choice(["enemy", "nothing"])

    if event == "enemy":
        print("Kamu dihadang musuh!")
        result = combat(player, goblin)
        if result == "Menang":
            print("Kamu melanjutkan perjalanan mu")
        elif result == "Kalah":
            print("Kamu Tewas mengenaskan.")
            exit()
    else:
        print("Tidak terjadi apa-apa. Terus berjalan.")

# Main Game Loop
def main():
    print("Selamat datang di Stick War: RPG!")
    while True:
        print("\nApa yang ingin kamu lakukan?")
        print("1. Menjelajah")
        print("2. bising bodo aku nak tido!")

        choice = input("Apa pilihan mu?: ")

        if choice == "1":
            explore()
        elif choice == "2":
            print("Yaudah besok aja...")
            break
        else:
            print("Invalid choice. Try again.")

# Start the game
if __name__ == "__main__":
    main()
