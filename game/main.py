# main.py
import sys
from player import Player
from world import World
from combat import Combat
from events import EventManager

def main():
    print("Welcome to the Grid-Based Text Adventure!")
    player = Player()
    world = World(width=50, height=50)
    events = EventManager()
    combat = Combat()

    current_location = world.starting_location()
    print(f"You awaken at {current_location.name}.")

    while True:
        command = input("> ").strip().lower()

        if command in ("quit", "exit"):
            print("Thanks for playing! Goodbye.")
            sys.exit(0)

        elif command.startswith("move "):
            direction = command.split(" ", 1)[1]
            new_location = world.move_player(current_location, direction)
            if new_location:
                current_location = new_location
                print(f"You move {direction} to {current_location.name}.")
                # Trigger any events or encounters at new location
                events.trigger(current_location, player)
            else:
                print("You can't move in that direction.")

        elif command.startswith("look"):
            print(f"You look around at {current_location.name}.")
            print(current_location.describe())

        elif command == "status":
            print(player.status())

        elif command.startswith("pick "):
            item_name = command.split(" ", 1)[1]
            if current_location.has_item(item_name):
                player.pick_item(item_name, current_location)
                print(f"You picked up {item_name}.")
            else:
                print(f"There is no {item_name} here.")

        elif command.startswith("inventory"):
            print(player.inventory_list())

        elif command == "help":
            print("Commands: move [direction], look, pick [item], inventory, status, quit")

        else:
            print("I don't understand that command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
