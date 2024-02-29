import random

class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage: int, attack_bonus: int) -> None:
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.attack_bonus = attack_bonus

    def calculate_damage(self) -> int:
        return random.randint(self.min_damage, self.max_damage)

class Armor:
    def __init__(self, name: str, armor_class: int) -> None:
        self.name = name
        self.armor_class = armor_class

class Character:
    def __init__(self, name: str, health: int, weapon: Weapon, armor: Armor) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon
        self.armor = armor
    
    def attack(self, target) -> None:
        if random.randint(1, 20) + self.weapon.attack_bonus >= target.armor.armor_class:
            damage = self.weapon.calculate_damage()
            print(f"{self.name} hit {target.name} with {self.weapon.name}")
            target.health -= damage
            target.health = max(target.health, 0)

        else: 
            print(f"{self.name} missed {target.name} with {self.weapon.name}")

class Player(Character):
    def __init__(self, name: str, health: int, weapon: Weapon, armor: Armor, money: int) -> None:
        super().__init__(name, health, weapon, armor)
        self.money = money

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon: Weapon, armor: Armor) -> None:
        super().__init__(name, health, weapon, armor)

# Define weapons and armor
sword = Weapon(name="Sword", min_damage=4, max_damage=14, attack_bonus=5)
great_axe = Weapon(name="Great Axe", min_damage=1, max_damage=20, attack_bonus=4)
fists = Weapon(name="Fists", min_damage=4, max_damage=4, attack_bonus=3)

light_armor = Armor(name="Leather Armor", armor_class=13)
medium_armor = Armor(name="Scale Armor", armor_class=15)
heavy_armor = Armor(name="Plate Armor", armor_class=17)

# Create characters
player = Player(name="Gal", health=100, weapon=sword, armor=light_armor, money=100)
goblin = Enemy(name="Goblin_1", health=50, weapon=sword, armor=heavy_armor)

# combat loop
while True:
    player.attack(goblin)
    goblin.attack(player)
    print(f"health of {player.name}: {player.health}")
    print(f"health of {goblin.name}: {goblin.health}")
    if player.health == 0:
        print("you died")
        break
    elif goblin.health == 0:
        print("you won")
        break

    input()
