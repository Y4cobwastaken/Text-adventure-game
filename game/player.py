# player.py

class Player:
    def __init__(self):
        self.health = 100
        self.hunger = 50
        self.thirst = 50
        self.stamina = 100
        self.inventory = []

    def status(self):
        return (
            f"Health: {self.health}\n"
            f"Hunger: {self.hunger}\n"
            f"Thirst: {self.thirst}\n"
            f"Stamina: {self.stamina}\n"
            f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}"
        )

    def pick_item(self, item_name, location):
        if item_name in location.items:
            self.inventory.append(item_name)
            location.items.remove(item_name)
        else:
            print(f"Item {item_name} is not available here.")

    def inventory_list(self):
        if not self.inventory:
            return "Your inventory is empty."
        return "Inventory:\n" + "\n".join(f"- {item}" for item in self.inventory)
