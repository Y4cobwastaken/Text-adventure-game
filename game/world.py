# world.py
import random

class Location:
    def __init__(self, x, y, name=None, items=None):
        self.x = x
        self.y = y
        self.name = name if name else f"Location ({x},{y})"
        self.items = items if items else []

    def describe(self):
        desc = f"You are at {self.name}."
        if self.items:
            desc += " You see: " + ", ".join(self.items) + "."
        else:
            desc += " There is nothing of interest here."
        return desc

class World:
    DIRECTIONS = {
        "north": (0, -1),
        "south": (0, 1),
        "east": (1, 0),
        "west": (-1, 0),
    }

    def __init__(self, width=50, height=50):
        self.width = width
        self.height = height
        self.grid = [[self._generate_location(x, y) for y in range(height)] for x in range(width)]

    def _generate_location(self, x, y):
        # Basic biome assignment for demo
        biomes = ["Forest", "Plains", "Hills", "Swamp", "Desert"]
        biome = random.choice(biomes)
        # Randomly add items
        possible_items = ["berries", "spear", "herbs", "stone", "wood"]
        items = random.choices(possible_items, k=random.randint(0, 2))
        return Location(x, y, name=f"{biome} ({x},{y})", items=items)

    def starting_location(self):
        # Start near center of the grid
        center_x = self.width // 2
        center_y = self.height // 2
        return self.grid[center_x][center_y]

    def move_player(self, current_location, direction):
        if direction not in self.DIRECTIONS:
            return None
        dx, dy = self.DIRECTIONS[direction]
        new_x = current_location.x + dx
        new_y = current_location.y + dy
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            return self.grid[new_x][new_y]
        return None
