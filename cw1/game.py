import json
import os
import random
import time

# ============================================================
#                     ASCII ADVENTURE RPG
# ============================================================

SAVE_FILE = "realm_save.json"

def slow(text, speed=0.02):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(speed)
    print()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ============================================================
#                      PLAYER CLASS
# ============================================================

class Player:
    def __init__(self, name, hp=30, atk=5, gold=10, inventory=None, location="village"):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.gold = gold
        self.location = location
        self.inventory = inventory or []

    def save(self):
        data = {
            "name": self.name,
            "hp": self.hp,
            "atk": self.atk,
            "gold": self.gold,
            "location": self.location,
            "inventory": self.inventory
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load():
        if not os.path.exists(SAVE_FILE):
            return None
        with open(SAVE_FILE, "r") as f:
            d = json.load(f)
        return Player(**d)

# ============================================================
#                     MONSTER CLASS
# ============================================================

class Monster:
    def __init__(self, name, hp, atk, gold_min, gold_max):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.gold_min = gold_min
        self.gold_max = gold_max

MONSTERS = {
    "forest": [
        Monster("Shadow Wolf", 10, 4, 3, 7),
        Monster("Corrupted Spirit", 12, 5, 4, 10)
    ],
    "cave": [
        Monster("Rock Golem", 20, 7, 10, 20),
        Monster("Bat Swarm", 15, 4, 5, 12)
    ],
    "castle": [
        Monster("Dark Knight", 25, 8, 20, 40),
        Monster("Fallen Mage", 20, 10, 15, 30)
    ],
}

# ============================================================
#                     COMBAT SYSTEM
# ============================================================

def combat(player, monster):
    clear()
    slow(f"A wild {monster.name} appears!", 0.03)
    time.sleep(1)

    while monster.hp > 0 and player.hp > 0:
        print("\n==================")
        print(f"Your HP: {player.hp}")
        print(f"{monster.name} HP: {monster.hp}")
        print("==================")

        choice = input("(A)ttack   (H)eal (if you have potions)   (R)un: ").lower()

        if choice == "a":
            dmg = random.randint(player.atk - 2, player.atk + 3)
            dmg = max(1, dmg)
            monster.hp -= dmg
            print(f"\nYou hit {monster.name} for {dmg} damage!")

        elif choice == "h":
            if "potion" in player.inventory:
                player.inventory.remove("potion")
                heal = random.randint(8, 15)
                player.hp += heal
                print(f"\nYou drink a potion and heal {heal} HP!")
            else:
                print("You have no potions!")

        elif choice == "r":
            if random.random() < 0.5:
                print("You escaped!")
                return
            else:
                print("You failed to escape!")

        # Monster attacks
        if monster.hp > 0:
            mdmg = random.randint(monster.atk - 2, monster.atk + 2)
            player.hp -= mdmg
            print(f"{monster.name} hits you for {mdmg} damage!")

        time.sleep(1)

    if player.hp <= 0:
        slow("You have been defeated...", 0.03)
        exit()

    gold = random.randint(monster.gold_min, monster.gold_max)
    slow(f"\nYou defeated {monster.name}!", 0.03)
    slow(f"You earn {gold} gold.", 0.02)
    player.gold += gold

# ============================================================
#                     MAP & LOCATIONS
# ============================================================

def visit_village(player):
    clear()
    print("=== VILLAGE ===")
    print("1. Shop")
    print("2. Rest (5 gold)")
    print("3. Go to forest")
    print("4. Go to cave")
    print("5. Go to castle")
    print("6. Save game")
    print("7. Quit")
    choice = input("> ")

    if choice == "1":
        shop(player)
    elif choice == "2":
        rest(player)
    elif choice == "3":
        player.location = "forest"
    elif choice == "4":
        player.location = "cave"
    elif choice == "5":
        player.location = "castle"
    elif choice == "6":
        player.save()
        print("Game saved!")
        input("Press Enter...")
    elif choice == "7":
        exit()

def shop(player):
    clear()
    print("=== SHOP ===")
    print("Gold:", player.gold)
    print("1. Potion (10 gold)")
    print("2. Sword Upgrade (+2 ATK) (25 gold)")
    print("3. Exit")
    choice = input("> ")

    if choice == "1":
        if player.gold >= 10:
            player.gold -= 10
            player.inventory.append("potion")
            print("Bought potion!")
        else:
            print("Not enough gold.")
    elif choice == "2":
        if player.gold >= 25:
            player.gold -= 25
            player.atk += 2
            print("Your sword feels stronger!")
        else:
            print("Not enough gold.")

    input("Press Enter...")

def rest(player):
    if player.gold < 5:
        print("Not enough gold!")
        time.sleep(1)
        return
    player.gold -= 5
    player.hp += 20
    print("You rest and recover 20 HP.")
    time.sleep(1)

def explore(player, area):
    clear()
    slow(f"You explore the {area}...", 0.03)
    time.sleep(1)

    if random.random() < 0.7:
        monster = random.choice(MONSTERS[area])
        combat(player, Monster(monster.name, monster.hp, monster.atk, monster.gold_min, monster.gold_max))
    else:
        slow("The area is quiet...", 0.03)
        time.sleep(1)

# ============================================================
#                    MAIN GAME LOOP
# ============================================================

def game_loop(player):
    while True:
        clear()
        print(f"Location: {player.location}")
        print(f"HP: {player.hp} | ATK: {player.atk} | Gold: {player.gold}")
        print("Inventory:", player.inventory)
        print("\n(Use M to return to village)")

        if player.location == "village":
            visit_village(player)
        else:
            print("1. Explore")
            print("2. Return to village")
            choice = input("> ")

            if choice == "1":
                explore(player, player.location)
            else:
                player.location = "village"

# ============================================================
#                      STARTUP LOGIC
# ============================================================

def main():
    clear()
    print("=== REALM OF SHADOWS ===\n")
    print("1. New Game")
    print("2. Load Game")
    choice = input("> ")

    if choice == "2":
        player = Player.load()
        if player:
            slow("Loaded save file!", 0.03)
        else:
            slow("No save found. Starting new game.", 0.03)
            player = Player(input("Enter name: "))
    else:
        player = Player(input("Enter name: "))

    game_loop(player)

main()
