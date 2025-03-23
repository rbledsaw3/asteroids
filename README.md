# Asteroids

This project is a Python implementation of the classic arcade game *Asteroids*, developed using Pygame. Players control a spaceship navigating through an asteroid field, aiming to destroy asteroids and avoid collisions.

## Features
- **Player Movement:** Smooth rotation and acceleration-based movement for realistic spaceship control.
- **Screen Wrapping:** Objects (player, asteroids, shots) wrap around the screen boundaries seamlessly.
- **Asteroid Splitting:** Larger asteroids split into smaller ones upon destruction.
- **Shot Mechanics:** Rate-limited firing to balance gameplay.
- **Shot Culling:** Shots disappear after leaving the visible play area.

## Installation

Ensure Python 3.10+ is installed, then:

```bash
pip install -r requirements.txt
```

## Running the Game

```bash
python main.py
```

## Controls
- **W/S:** Accelerate/Decelerate
- **A/D:** Rotate Left/Right
- **Space:** Shoot

## Future Improvements
- Scoring system
- Multiple lives and respawning
- Explosion effects
- Background imagery
- Additional weapons
- Power-ups (shields, speed boosts, bombs)

## Dependencies
- [Pygame 2.6.0](https://www.pygame.org/)

---

Created by Robert Bledsaw III

