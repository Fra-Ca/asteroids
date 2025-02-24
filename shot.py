from circleshape import*
from constants import*
from asteroids import Asteroid
import random

class Shot(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 1)  # Initially pointing "up".
        self.velocity = self.velocity.rotate(angle)  # Rotate it by the player's current direction.
        self.velocity *= PLAYER_SHOOT_SPEED  # Scale it to the defined bullet speed.
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    def check_collision(self, circleshape):
        distance = self.position.distance_to(circleshape.position)
        
        if distance <= (self.radius + circleshape.radius):
            pass
    def check_shot_collision(self, asteroid):
        distance = self.position.distance_to(asteroid.position)

        if distance <= (self.radius +asteroid.radius):
            return True

    