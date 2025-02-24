import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape
from shot import Shot

import sys



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__( x, y, PLAYER_RADIUS )
        self.rotation = 0
        self.position = pygame.Vector2(x, y)
        self.player_shoot_cooldown = 0
        
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        self.player_shoot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.player_shoot_cooldown <= 0:
                self.shoot()
                self.player_shoot_cooldown = 0.3
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def check_collision(self, circleshape):
        distance = self.position.distance_to(circleshape.position)
        
        if distance <= (self.radius + circleshape.radius):
            print("Game Over!")
            sys.exit()
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, self.rotation)
        for group in Shot.containers:
            group.add(shot)