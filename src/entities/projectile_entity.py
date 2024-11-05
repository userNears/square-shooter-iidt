import pygame
from src import settings

class Projectile:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        # Stops moving after passing the screen width
        if self.x < settings.SCREEN_WIDTH:
            self.x += self.speed

    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    

