
---

# Snake Game 🐍 (Work in Progress)

> **Note**: This project is a work in progress. Some features are still being developed, and the game is actively being improved.

A classic Snake game built in Python with Pygame, featuring multiple modes, power-ups, and debugging options. This project is perfect for coding enthusiasts and gamers looking to enjoy or expand upon a well-known game.

## Table of Contents
- [Features](#features)
- [Game Modes](#game-modes)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Power-Up Toggles](#power-up-toggles)
- [Future Ideas](#future-ideas)
- [Contributing](#contributing)

---

## Features
- **Classic Snake Gameplay**: Maneuver the snake to eat food, grow longer, and try to beat your high score.
- **Endless Mode**: Play infinitely! Collisions reduce the snake’s length rather than ending the game, making it a survival challenge.
- **Debugging Mode**: Track essential game data such as the snake's coordinates, food position, and reverse-control state, making it ideal for testing and fine-tuning.
- **Reverse Control Power-Up**: Randomly appearing items that temporarily reverse controls, adding an exciting twist to the gameplay.
- **Speed Power-Up**: Boost or reduce the snake’s speed with randomly appearing power-ups.
- **Larger Screen**: The game screen size is now set to 800x600 for more room to navigate.

## Game Modes
1. **Normal Mode**: Traditional snake gameplay where the game ends upon hitting the screen boundary or colliding with the snake itself.
2. **Endless Mode**: Keeps the game going indefinitely. In this mode, colliding with walls or the snake’s body reduces the snake’s length, allowing for a continuous experience.
3. **Debug Mode**: 
   - Available in both Normal and Endless modes, Debug Mode shows on-screen information for easier testing and optimization.
   - Displays data like the snake’s current position, the location of food, and if any control reversals are active.

## Installation

1. **Clone the Repository**:
   Clone the repository to your local machine using:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. **Install Dependencies**:
   Make sure you have Python and Pygame installed. Install Pygame with:
   ```bash
   pip install pygame
   ```

## Usage

To run the game, use:
```bash
python main_game.py
```

## Controls
- **W, A, S, D**: Move the snake up, left, down, and right respectively.
- **Escape**: Exits to the main menu when in Endless Mode, allowing you to select another game mode.

## Power-Up Toggles
At the start of the game, you can toggle power-ups on or off:
- **Press T**: Toggles Speed Power-Ups (boost or slowdown).
- **Press R**: Toggles Reverse Control Power-Ups.

If a power-up is active, a notification will appear at the bottom of the screen when you consume it, indicating its effect.

## Future Ideas
Below are some additional features that could further enhance the gameplay:
- **Additional Power-Ups**: New power-ups such as invincibility or food multipliers for added variety.
- **Maze Walls**: Add obstacles to create mazes and additional challenges.

## Contributing
Contributions are welcome! If you'd like to contribute, feel free to fork the project, make your changes, and submit a pull request. For major changes, open an issue first to discuss what you would like to change.

---
