import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.line_width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.line_width)

    def update(self, dt):
        self.position += self.velocity * dt
        
