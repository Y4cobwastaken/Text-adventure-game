# combat.py
import random

class Combat:
    def __init__(self):
        pass

    def fight(self, player, enemy):
        print(f"A {enemy.name} attacks you!")
        while player.health > 0 and enemy.health > 0:
            player_attack = random.randint(5, 15)
            enemy.health -= player_attack
            print(f"You hit the {enemy.name} for {player_attack} damage. Enemy health: {enemy.health}")

            if enemy.health <= 0:
                print(f"You defeated the {enemy.name}!")
                return True

            enemy_attack = random.randint(3, 12)
            player.health -= enemy_attack
            print(f"The {enemy.name} hits you for {enemy_attack} damage. Your health: {player.health}")

            if player.health <= 0:
                print("You have been defeated!")
                return False

        return False

class Enemy:
    def __init__(self, name, health=50):
        self.name = name
        self.health = health
