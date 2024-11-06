import pygame
from src import settings
from src.entities import player_entity, enemy_entity
import random

def main():
    pygame.init()
    # Game title
    pygame.display.set_caption("Python Game Project")
    # Screen size
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    # Creating player
    player = player_entity.Player(
        x = settings.INITIAL_PLAYER_POS_X,
        y = settings.INITIAL_PLAYER_POS_Y,
        width = settings.PLAYER_WIDTH,
        height = settings.PLAYER_HEIGHT,
        color = settings.BLACK,
        speed = settings.PLAYER_SPEED,
        health = 3 # MIGHT CHANGE
    )

    def spawn_enemies(amount):
        enemies = []
        x = settings.SCREEN_WIDTH
        for _ in range(amount):
            y = random.randint(100, settings.SCREEN_HEIGHT - 100)
            
            enemy_type = random.choice(("Enemy A", "Enemy B"))

            if enemy_type == "Enemy A":
                enemies.append(enemy_entity.Enemy(
                    x = x, 
                    y = y, 
                    width = settings.ENEMY_A_WIDTH, 
                    height = settings.ENEMY_A_HEIGHT, 
                    color = settings.ENEMY_A_COLOR, 
                    speed = settings.ENEMY_A_SPEED, 
                    health = settings.ENEMY_A_HEALTH
                ))
            else:
                enemies.append(enemy_entity.Enemy(
                    x = x, 
                    y = y, 
                    width = settings.ENEMY_B_WIDTH, 
                    height = settings.ENEMY_B_HEIGHT, 
                    color = settings.ENEMY_B_COLOR, 
                    speed = settings.ENEMY_B_SPEED, 
                    health = settings.ENEMY_B_HEALTH
                ))
        
        return enemies
    
    # Spawn 1 enemy in the beginning
    amount = 1
    enemies = spawn_enemies(amount)

    def display_centered_text(text, font, size, color):
        font = pygame.font.SysFont(font, size)
        txt = font.render(text, True, color)
        txt_rect = txt.get_rect(center = (settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2))
        
        screen.blit(txt, txt_rect)
    
    running = True
    paused = False
    game_over = False
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                # Toggle pause
                if event.key == pygame.K_ESCAPE:
                    paused = not paused

                # Restart if a key is pressed in the game over screen
                if game_over:
                    main()

        if not paused:
            screen.fill(settings.BACKGROUND_COLOR)

            # Drawing the defense line
            pygame.draw.rect(
                screen, 
                settings.DEFENSE_LINE_COLOR, 
                (settings.DEFENSE_LINE_POS_X, 
                0, 
                settings.DEFENSE_LINE_WIDTH, 
                settings.SCREEN_HEIGHT)
            )

            # Drawing the player's HP
            pygame.draw.rect(
                screen, 
                settings.HP_COLOR, 
                (settings.HP_POS_X, 
                settings.HP_POS_Y, 
                settings.HP_WIDTH, 
                settings.HP_HEIGHT)
            )

            player.update()
            player.render(screen)

            if not enemies:
                amount += 1
                enemies = spawn_enemies(amount)

            for enemy in enemies[:]:
                # Update and render each enemy
                enemy.update()
                enemy.render(screen)

                # Remove enemy if it passes defense line
                if enemy.x <= settings.DEFENSE_LINE_POS_X:
                    enemies.remove(enemy)
                    player.health -= 1

                    if player.health <= 0:
                        game_over = True

                for projectile in player.projectiles[:]:
                    # Check if the projectile's hitbox collides with the enemy's hitbox
                    if projectile.hitbox().colliderect(enemy.hitbox()):
                        enemy.health -= 1
                        player.projectiles.remove(projectile)

                        if enemy.health <= 0:
                            enemies.remove(enemy)
                        break
        
            for projectile in player.projectiles[:]: 
                # Remove projectiles that leave sight
                if projectile.x > settings.SCREEN_WIDTH:
                    player.projectiles.remove(projectile)
        else:
            # Pause screen
            screen.fill(settings.WHITE)
            display_centered_text(
                text = "Game paused",
                font = "arialblack", 
                size = 40, 
                color = settings.BLACK
            )

        if game_over:
            screen.fill(settings.BLACK)  # Optional: change the background color
            display_centered_text(
                text = "GAME OVER! Press any key to restart.",
                font = "arialblack", 
                size = 40, 
                color = settings.WHITE
            )

        # Update screen
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main() # yueil
    