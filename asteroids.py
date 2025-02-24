from circleshape import*
from constants import*
import random
import sys

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    def check_collision(self, circleshape):
        distance = self.position.distance_to(circleshape.position)
        
        if distance <= (self.radius + circleshape.radius):
            print("Game Over!")
            sys.exit()
    def split(self):
        self.kill()
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            a1 = Asteroid(self.position.x, self. position.y, (self.radius - ASTEROID_MIN_RADIUS))
            a2 = Asteroid(self.position.x, self.position.y, (self.radius -ASTEROID_MIN_RADIUS))
            a1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)
            a2.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)