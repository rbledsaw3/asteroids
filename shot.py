import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        self.line_width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.line_width)

    def update(self, dt):
        self.position += self.velocity * dt
        
