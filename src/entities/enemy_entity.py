import pygame
from src import settings

class Enemy:
    def __init__(self, x, y, width, height, color, speed, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.health = health

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        # Able to move until passing defense line
        if self.x > settings.DEFENSE_LINE_POS_X:
            self.x -= self.speed

    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)