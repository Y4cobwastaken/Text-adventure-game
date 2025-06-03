# events.py
import random

class EventManager:
    def __init__(self):
        self.events = [
            self.find_berries,
            self.sudden_storm,
            self.abandoned_camp,
            self.wild_animal_encounter
        ]

    def trigger(self, location, player):
        # Random chance to trigger an event when entering a location
        if random.random() < 0.3:  # 30% chance
            event = random.choice(self.events)
            event(location, player)

    def find_berries(self, location, player):
        if "berries" in location.items:
            print("You find some fresh berries here.")
            # Player can pick berries manually later, or you could auto-add
        else:
            print("You look around but find no berries.")

    def sudden_storm(self, location, player):
        print("A sudden storm hits! You lose some stamina.")
        player.stamina = max(player.stamina - 10, 0)

    def abandoned_camp(self, location, player):
        print("You discover an abandoned camp with some supplies.")
        supplies = ["herbs", "wood", "stone"]
        found = random.choice(supplies)
        print(f"You take {found} and add it to your inventory.")
        player.inventory.append(found)

    def wild_animal_encounter(self, location, player):
        print("A wild animal appears! Prepare to fight or flee.")
        # Placeholder: actual combat logic handled elsewhere
