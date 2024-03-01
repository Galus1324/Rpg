import random



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
            print(f"{self.name} hit {target.name} with {self.weapon.name}")
            target.health -= damage
            target.health = max(target.health, 0)

        else: 
            print(f"{self.name} missed {target.name} with {self.weapon.name}")

player_name = ""

class Player(Character):
    def __init__(self, name: str, health: int, weapon: Weapon, armor_class: int, money: int) -> None:
        super().__init__(name , health, weapon, armor_class)
        self.name = player_name
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

# combat loop
def combat(player,enemy):
    while True:
        print("attack or guard?")
        player.attack(enemy)
        print(f"health of {enemy.name}: {enemy.health}")
        if enemy.health == 0:
            print("you won")
            break
        else:
            pass
        enemy.attack(player)
        print(f"health of {player.name}: {player.health}")
        player.armor_class = player.armor_class_base
        if player.health == 0:
            print("you died")
            break
        else:
            pass

        input()
