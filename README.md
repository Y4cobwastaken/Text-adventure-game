> ⚠️ **Warning:** This project is a work in progress and not fully debugged.  
> Use at your own risk. Features and stability may change as development continues.

# Grid-Based Text Adventure Game

A modular, terminal-based survival and exploration game set in a massive grid world.  
You play as a lone wanderer in a desolate, dangerous world filled with procedurally generated terrain, dynamic encounters, and meaningful decisions.

> 🧭 Explore. 💀 Survive. 🛠 Craft. ⚔ Fight.  
> Every move matters in this unforgiving world.

---

## 🎮 Features

- **Massive Grid World:**  
  Explore a customizable map (e.g. 50x50 tiles) with diverse biomes, regions, and landmarks.

- **Player System:**  
  Manage health, hunger, thirst, stamina, and inventory.  
  Make choices that affect survival and long-term outcomes.

- **Items & Crafting:**  
  Pick up, combine, and craft items for tools, food, weapons, and more.

- **Enemies & Combat:**  
  Random encounters, turn-based combat, and unique enemy behaviors.

- **Quests & Events:**  
  Procedural and hand-authored events, side quests, and NPC dialogue.

- **Dialogue System:**  
  Branching conversations with consequences and information-gathering.

- **Save/Load System:**  
  Resume your game at any point. Play across sessions.

---

## 📦 Structure

```bash
game/
├── main.py         # Entry point, game loop
├── world.py        # World/map generation and logic
├── player.py       # Player stats, inventory, movement
├── items.py        # Items, crafting recipes
├── combat.py       # Enemy stats and combat logic
├── events.py       # Random events, scripted encounters
├── dialogue.py     # Dialogue and interaction system
├── save_load.py    # Save/load functionality
└── utils.py        # Common utility functions
```

---

## ▶ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/text-adventure-grid-game.git
   cd text-adventure-grid-game
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python -m game.main
   ```

---

## 🧠 Developer Notes

- Written entirely in Python 3
- Designed to be extensible: easy to add new items, areas, events, or enemies
- Supports clean save/load using JSON
- No external frameworks — pure Python

---

## 💬 Example Gameplay

```
You awaken in the Northern Expanse. Cold wind cuts through your torn jacket.
> move south

You walk cautiously into: Forested Grove
You see: wild berries, broken spear

> pick berries
You add berries to your inventory.

> eat berries
You feel slightly less hungry.

> move east
A hostile scavenger appears!
> fight
You attack with fists (5 damage). The scavenger retaliates (7 damage).
```

---

## 📚 Credits

Built solo by Jacob Dicker, originally as a personal project to explore text-based engines, turn-based logic, and procedural generation.

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
