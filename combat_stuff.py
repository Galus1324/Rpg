import random
from functions import *


class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage: int, attack_bonus: int) -> None:
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.attack_bonus = attack_bonus

    def calculate_damage(self) -> int:
        return random.randint(self.min_damage, self.max_damage)

class Character:
    def __init__(self, name: str, health: int, weapon: Weapon, armor_class: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon
        self.armor_class = armor_class
        self.armor_class_base = armor_class
        
    def guard(self):
        self.armor_class += 2
    
    def attack(self, target) -> None:
        if random.randint(1, 20) + self.weapon.attack_bonus >= target.armor_class:
            damage = self.weapon.calculate_damage()
            print(f"{self.name} hit {target.name} with a {self.weapon.name}")
            target.health -= damage
            target.health = max(target.health, 0)

        else: 
            print(f"{self.name} missed {target.name} with a {self.weapon.name}")

player_name = ""

class Player(Character):
    def __init__(self, name: str, health: int, weapon: Weapon, armor_class: int, money: int) -> None:
        super().__init__(name, health, weapon, armor_class)
        self.money = money

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon: Weapon, armor_class: int) -> None:
        super().__init__(name, health, weapon, armor_class)

player = Player

# Define weapons and armor
sword = Weapon(name="Sword", min_damage=4, max_damage=14, attack_bonus=5)
great_axe = Weapon(name="Great Axe", min_damage=1, max_damage=20, attack_bonus=4)
fists = Weapon(name="Fists", min_damage=4, max_damage=4, attack_bonus=3)
spell_book = Weapon(name="spell book", min_damage=5, max_damage=30, attack_bonus=3)
dagger = Weapon(name="dagger", min_damage=10, max_damage=20, attack_bonus=4)


# Create characters
fighter = Player(name=player_name, health=100, weapon=sword, armor_class=17, money=100)
mage = Player(name=player_name,  health=60, weapon=spell_book, armor_class=13, money=200)
rogue = Player(name=player_name, health=70, weapon=dagger, armor_class=15, money=150)
goblin = Enemy(name="Goblin_1", health=50, weapon=sword, armor_class=15)

def player_attack(player, enemy):
    player.attack(enemy)
    print_slow(f"health of {enemy.name}: {enemy.health}\n")

def player_guard(player):
    player.guard()
    print_slow(f"armor class of {player.name} has increased to {player.armor_class}\n")

    
# combat loop
def combat(player, enemy):
    while True:
        multi_choice(["attack", "guard"],
                     [lambda: player_attack(player, enemy),
                      lambda: player_guard(player)])
        if enemy.health == 0:
            print("you won\n")
            break
        else:
            enemy.attack(player)
            print_slow(f"health of {player.name}: {player.health}\n")
            player.armor_class = player.armor_class_base
            if player.health == 0:
                print_slow("you died")
                break
            else:
                pass

        
