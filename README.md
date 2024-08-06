# Classic Snake Game

Experience the classic Snake arcade game using Python's `turtle` module. This game allows you to relive the nostalgia of the arcade with a simple yet engaging implementation. The game records and stores your high score in a text file, updating it whenever you achieve a new high score. Control the snake using the keyboard arrows and try to beat your own high score!

## Features

- **Classic Snake Gameplay:** Navigate the snake to collect food, grow in size, and avoid collisions with the walls and itself.
- **High Score Tracking:** The game records your high score in a `highscore.txt` file and updates it if you achieve a new high score.
- **Game Over Detection:** Detects when the snake collides with the walls or itself and ends the game.
- **Graphical User Interface:** Provides a simple and intuitive interface for playing the game.
- **Keyboard Controls:** Use the arrow keys to change the snake's direction.

## Key Concepts Demonstrated

- **Object-Oriented Programming (OOP):** Uses classes and objects to manage the snake, scoreboard, food, and game functions.
- **GUI Design:** Implements a graphical interface using the `turtle` module for real-time game rendering.
- **Event Handling:** Manages user input for controlling the snake's direction.

## Code Overview

### Main Program (`main.py`)

- **Game Initialization:** Sets up the game window and initializes the game components.
- **Game Loop:** Continuously updates the game state, renders the graphics, and checks for collisions.
- **User Input Handling:** Captures user input to change the snake's direction.

### Scoreboard (`scoreboard.py`)

- **Score Management:** Tracks and updates the player's score.
- **Display:** Renders the current score on the game screen.

### Snake (`snake.py`)

- **Snake Movement:** Manages the snake's movement, growth, and direction.
- **Collision Detection:** Checks for collisions with the walls and the snake itself.
- **Growth Management:** Increases the snake's length when it collects food.

### Food (`food.py`)

- **Food Initialization:** Creates the food object using the `turtle` module, setting its shape, color, and initial position.
- **Random Positioning:** Places the food at a random position on the screen each time it is eaten by the snake.
- **Appearance:** Food appears as a small blue circle, making it easily distinguishable from other game elements.

## Quantifiable Results

- **Real-time Rendering:** The game renders at a consistent frame rate for smooth gameplay.
- **Score Tracking:** Accurately tracks the player's score throughout the game session.
- **Collision Detection:** Reliably detects collisions to end the game when necessary.

