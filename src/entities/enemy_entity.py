import pygame
from src import settings
import random

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
        # Black rect for the border
        pygame.draw.rect(screen, settings.BORDER_COLOR, (self.x, self.y, self.width, self.height))
        # Enemy color
        pygame.draw.rect(screen, self.color, (self.x + 3, self.y + 3, self.width - 6, self.height - 6))

    def update(self):
        # Able to move until passing defense line
        if self.x > settings.DEFENSE_LINE_POS_X:
            self.x -= self.speed

    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
class Boss(Enemy):
    def __init__(self, x, y, width, height, color, speed, health):
        super().__init__(x, y, width, height, color, speed, health)
        
        # Start by moving either up or down
        self.y_direction = random.choice([-1, 1])
        # Random amount of steps in the y axis
        self.y_direction_steps = random.randint(20, 200)
        self.y_speed = self.speed * 5

    def update(self):
        if self.x > settings.DEFENSE_LINE_POS_X:
            self.x -= self.speed
            self.y += self.y_direction * self.y_speed

            self.y_direction_steps -= self.y_speed

            # Switch directions if the direction steps end or if too close to the edges of the screen
            if self.y_direction_steps <= 0 or self.y <= 75 or self.y >= settings.SCREEN_HEIGHT - self.width - 75:
                self.y_direction *= -1

                self.y_direction_steps = random.randint(20, 200)