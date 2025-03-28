import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.line_width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.line_width)

    def update(self, dt):
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
        self.position += self.velocity * dt
        
    def split(self, asteroid_field):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            asteroid_field.count -= 1
            return
        random_angle = random.uniform(20, 50)
        angle_1 = self.velocity.rotate(random_angle)
        angle_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = angle_1 * 1.2
        asteroid_2.velocity = angle_2 * 1.2
        asteroid_field.count += 1


