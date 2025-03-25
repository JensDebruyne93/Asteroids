import pygame, random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            velocity_asteroid1 = pygame.math.Vector2(self.velocity).rotate(random_angle) * 1.2
            velocity_asteroid2 = pygame.math.Vector2(self.velocity).rotate(-random_angle) * 1.2
            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = velocity_asteroid1
            asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
            asteroid2.velocity = velocity_asteroid2