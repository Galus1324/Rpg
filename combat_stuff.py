import random, os, time
from functions import *
from health_bar import HealthBar


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
    
    def rest(self):
        self.health = self.health_max
        
    def guard(self):
        self.armor_class += 2
        print(f"armor class of {self.name} has increased to {self.armor_class}\n")
    
    def attack(self, target) -> None:
        if random.randint(1, 20) + self.weapon.attack_bonus >= target.armor_class:
            damage = self.weapon.calculate_damage()
            print(f"{self.name} hit {target.name} with {self.weapon.name}\n")
            target.health -= damage
            target.health = max(target.health, 0)
            target.health_bar.update()

        else: 
            print(f"{self.name} missed {target.name} with {self.weapon.name}\n")

player_name = ""

class Player(Character):
    def __init__(self, name: str, health: int, weapon: Weapon, armor_class: int, money: int, lockpicking_bonus: int) -> None:
        super().__init__(name, health, weapon, armor_class)
        self.health_bar = HealthBar(self, color="green")
        self.money = money
        self.lockpicking_bonus = lockpicking_bonus
        self.health_potion = 0

    def potion(self):
        print(f"{self.name} drank the healing potion and regained all hp")
        self.health_potion -=1
        self.rest()
        
    def lockpicking(self):
        if random.randint(1,20) + self.lockpicking_bonus > 12:
            return True
        else:
            return False

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon: Weapon, armor_class: int) -> None:
        super().__init__(name, health, weapon, armor_class)
        self.health_bar = HealthBar(self, color="red")

player = Player

# Define weapons and armor
sword = Weapon(name="a Sword", min_damage=10, max_damage=40, attack_bonus=9)
great_axe = Weapon(name="a Great Axe", min_damage=5, max_damage=50, attack_bonus=8)
fists = Weapon(name="Fists", min_damage=4, max_damage=4, attack_bonus=6)
spell_book = Weapon(name="a spell book", min_damage=1, max_damage=60, attack_bonus=6)
dagger = Weapon(name="a dagger", min_damage=20, max_damage=35, attack_bonus=8)
horns = Weapon(name="horns", min_damage=5, max_damage=8, attack_bonus=5)
tail = Weapon(name="a tail", min_damage=1, max_damage=8, attack_bonus=7)
rusted_sword = Weapon(name="a rusted sword", min_damage=5, max_damage=15, attack_bonus=3)

# Create characters
fighter = Player(name=player_name, health=100, weapon=sword, armor_class=17, money=100, lockpicking_bonus=0)
mage = Player(name=player_name,  health=60, weapon=spell_book, armor_class=13, money=200, lockpicking_bonus=3)
rogue = Player(name=player_name, health=70, weapon=dagger, armor_class=15, money=150, lockpicking_bonus=7)
goblin_1 = Enemy(name="Orki", health=50, weapon=sword, armor_class=15)
goblin_2 = Enemy(name="Porky", health=50, weapon=sword, armor_class=15)
triceratops = Enemy(name="triceratops", health=200, weapon=horns, armor_class=12)
skeleton = Enemy(name="skeleton", health=50, weapon=rusted_sword, armor_class=12)
   

    
# combat loop
def combat(player, enemy):
    print_slow(f"combat between {player.name} and {enemy.name} has started.\n")
    print("enter to continue")
    input()

    while True:
        os.system("cls")
        if player.health_potion > 0:
            multi_choice(["attack", "guard", "drink potion"],
                         [lambda: player.attack(enemy),
                          lambda: player.guard(),
                          lambda: player.potion()])
        else:
            multi_choice(["attack", "guard"],
                         [lambda: player.attack(enemy),
                          lambda: player.guard()])

        if enemy.health == 0:
            enemy.rest()
            print_slow("you won\n")
            break
        else:
            enemy.attack(player)
            player.armor_class = player.armor_class_base
            player.health_bar.draw()
            enemy.health_bar.draw()
            print("enter to continue")
            input()

            if player.health == 0:
                print_slow("you died\n")
                game_over()
            else:
                pass
            

        
