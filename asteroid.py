import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        random_rotation = random.uniform(20, 50)
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid.velocity = self.velocity.rotate(random_rotation) * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid2.velocity = self.velocity.rotate(-random_rotation) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, 2)
    
    def update(self, dts):
        self.position += self.velocity * dts
