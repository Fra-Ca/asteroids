from circleshape import*
from constants import*

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