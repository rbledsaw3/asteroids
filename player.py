import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.line_width = 2
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return a, b, c

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), self.line_width)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, acceleration, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * acceleration * dt
        if self.velocity.length() > PLAYER_MAX_SPEED:
            self.velocity = self.velocity.normalize() * PLAYER_MAX_SPEED

    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOT_COOLDOWN
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity += forward * PLAYER_SHOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(PLAYER_ACCELERATION, dt)
        elif keys[pygame.K_s]:
            self.move(-PLAYER_ACCELERATION, dt)

        self.position += self.velocity * dt
    

        if keys[pygame.K_SPACE]:
            self.shoot()
