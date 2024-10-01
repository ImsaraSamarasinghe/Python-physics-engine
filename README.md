# Physics Engine with Ball Collisions

This project is a simple physics engine built using Python and Pygame. It simulates the movement of multiple balls under the effect of gravity and handles collisions between them, as well as interactions with the environment (walls and the ground). Users can interact with the simulation by clicking and dragging the mouse to launch new balls with different velocities.

## Features

- Simulates balls under gravity.
- Ball-to-ball collision detection and resolution.
- Ball interaction with the environment, including bouncing off walls and the ground.
- Dynamic user input: click and drag to create balls with custom velocities.
- Simple damping to simulate energy loss during collisions.
- Easy-to-clear simulation using the 'X' key.

## How to Use

1. **Launch the simulation**: Run the Python script, and a window will appear with an empty space.
   
2. **Create balls**: 
   - Click and drag your mouse to launch a ball in the direction of the drag.
   - The velocity of the ball is determined by the speed and direction of your mouse movement. If you click without dragging, the ball will simply fall with no initial velocity.

3. **Clear all balls**: Press the 'X' key on your keyboard to clear the screen.

4. **Collision simulation**: Balls will collide with each other, bounce off the walls, and fall due to gravity. Collisions result in a realistic exchange of velocity, simulating real-world physics.

## Controls

- **Mouse Click and Drag**: Create a ball and launch it in the direction of the drag.
- **Press 'X'**: Clear all existing balls from the screen.

## Requirements

- **Python 3.x**
- **Pygame**: Install Pygame using pip:

```bash
pip install pygame
```

## Code Structure

- **`PhysicsEngine` class**: Manages the entire physics simulation, including ball creation, movement, and collisions.
  - `add_ball()`: Adds a new ball to the simulation with a specified position and velocity.
  - `handle_ball_collisions()`: Detects and resolves collisions between balls using basic physics principles.
  - `update()`: Updates the positions and velocities of all balls based on gravity and wall collisions.
  - `draw()`: Draws the balls on the screen.
  - `run()`: The main loop that handles events and runs the simulation at 60 frames per second.

## Running the Code

To run the code, simply execute the script in your terminal or preferred Python environment:

```bash
python physics_engine.py
```

## Output
<div style="text-align: center;">
 <img src="PhysicsEnginewithCollisionsUbuntu2024-09-2614-39-22-ezgif.com-video-to-gif-converter (1).gif" alt="Balls"/>
</div>

## Future Improvements

- Adding more advanced features like ball friction or spin.
- Introducing ball size and mass variations.
- Enhancing the physics engine to simulate more complex objects and interactions.
