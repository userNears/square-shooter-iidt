import pygame
from src import settings
from src.entities import projectile_entity

class Player:
    def __init__(self, x, y, width, height, color, speed, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.health = health
        self.projectiles = []
        self.last_fired = 0 # Last fired in milliseconds

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        # Render each projectile
        for projectile in self.projectiles:
            projectile.render(screen)

    def update(self):
        keys = pygame.key.get_pressed()

        # Movement controls
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y > 0:
                self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y < settings.SCREEN_HEIGHT - self.height:
                self.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x > 0:
                self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # Disable right movement when too close to defense line
            if self.x < settings.DEFENSE_LINE_POS_X - settings.PLAYER_WIDTH - 10:
                self.x += self.speed

        if keys[pygame.K_SPACE]:
            self.shoot()

        # Updating each projectile
        for projectile in self.projectiles:
            projectile.update()
        
    def shoot(self):
        # Current time in milliseconds
        current_time = pygame.time.get_ticks()

        # Checking if cooldown time has passed
        if current_time - self.last_fired >= settings.projectile_cooldown:
            projectile = projectile_entity.Projectile(
                x = self.x + self.width, 
                y = self.y + self.height//2,
                width = settings.PROJECTILE_WIDTH,
                height = settings.PROJECTILE_HEIGHT,
                speed = settings.PROJECTILE_SPEED,
                color = settings.PROJECTILE_COLOR
            )

            self.projectiles.append(projectile)
            self.last_fired = current_time