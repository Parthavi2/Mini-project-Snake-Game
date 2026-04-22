# Snake Game with Login System

## Overview
This project is a GUI-based Snake Game developed using Python. It integrates a basic login authentication system, requiring users to enter valid credentials before accessing the game. The application demonstrates object-oriented programming, event-driven design, and graphical user interfaces using Tkinter.

---

## Features
- User authentication with predefined credentials  
- Interactive graphical user interface using Tkinter  
- Classic snake gameplay with smooth controls  
- Randomized food generation  
- Real-time score tracking  
- Game over detection with restart functionality  
- Background image integration for improved UI  

---

## System Architecture

User  
→ Login Interface (Authentication)  
→ Game Engine  
→ Game Loop (Movement, Collision Detection, Score Update)  

---

## Tech Stack
- Programming Language: Python  
- GUI Framework: Tkinter  
- Image Processing: Pillow (PIL)  
- Programming Paradigm: Object-Oriented Programming  

---

## Project Structure
```
snake-game/
│── main.py
│── snake-game-bg-image.jpg
│── README.md
```

---

## Installation and Setup

### Step 1: Install Required Libraries
```
pip install pillow
```

### Step 2: Run the Application
```
python main.py
```

---

## Login Credentials

- Username: admin | Password: 123  
- Username: player | Password: snake  

These credentials are defined in the code and can be modified as needed.

---

## Controls

- Arrow Keys: Move the snake (Up, Down, Left, Right)  
- R Key: Restart the game after game over  
- Q Key: Quit the game  

---

## Working Description

### Login Module
The login interface collects user credentials and validates them against a predefined dictionary. Upon successful authentication, the game window is launched. Invalid credentials trigger an error message.

### Game Engine
The snake moves continuously based on the current direction. Food is generated at random positions on the grid. When the snake consumes food, its length increases and the score is updated.

### Collision Detection
The game ends when:
- The snake collides with itself  
- The snake hits the boundary of the game area  

### Game Over and Restart
Upon game termination, the final score is displayed. The user is given options to restart or quit the game.

---

## Future Enhancements
- Integration of database-based authentication system  
- Implementation of leaderboard and score persistence  
- Addition of sound effects and animations  
- Multiplayer functionality  
- AI-based snake gameplay  

---

## Notes
- Ensure the background image file is placed in the same directory as the main script  
- The window size is fixed for consistent gameplay  

---

## Author
Developed as a Python GUI-based application demonstrating authentication and game logic integration.

---

## Contribution
Contributions, improvements, and suggestions are welcome. Fork the repository and submit a pull request for enhancements.
