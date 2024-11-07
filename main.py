import pygame
from src import settings
from src.entities import player_entity, enemy_entity
import random
import time
from src import create_buttons
import sys

def main():
    pygame.init()
    # Game title
    pygame.display.set_caption("Python Game Project")
    # Screen size
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    # Setting default mouse cursor
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    clock = pygame.time.Clock()

    # Creating player
    player = player_entity.Player(
        x = settings.INITIAL_PLAYER_POS_X,
        y = settings.INITIAL_PLAYER_POS_Y,
        width = settings.PLAYER_WIDTH,
        height = settings.PLAYER_HEIGHT,
        color = settings.PLAYER_COLOR,
        speed = settings.PLAYER_SPEED,
        health = settings.PLAYER_HEALTH
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
    
    def display_centered_text(text, font, size, color, x, y):
        font = pygame.font.SysFont(font, size)
        txt = font.render(text, True, color)
        txt_rect = txt.get_rect(center = (x, y))
        
        screen.blit(txt, txt_rect)

    def quit_game():
        sys.exit()

    def toggle_pause_game():
        # Accessing the variables from main()
        nonlocal paused, total_pause_time, latest_active_time
        
        # Toggle pause
        paused = not paused

        # Getting the total pause time
        if not paused:
            latest_pause_time = time.time() - latest_active_time
            total_pause_time += latest_pause_time

    def restart_game():
        # Resetting projectile cooldown
        settings.projectile_cooldown = settings.INITIAL_PROJECTILE_COOLDOWN
        main()

    def ui():
        # Wave counter
        display_centered_text(
            text = f"Wave {wave_count}",
            font = "arialblack",
            size = 20,
            color = settings.TEXT_COLOR,
            x = settings.SCREEN_WIDTH / 2,
            y = 20
        )

        # Timer
        display_centered_text(
            text = f"Time {ingame_timer:.2f}s",
            font = "arialblack",
            size = 20,
            color = settings.TEXT_COLOR,
            x = settings.SCREEN_WIDTH / 2,
            y = settings.SCREEN_HEIGHT - 20
        )

        # Drawing the player's health bar
        # Dynamically increases/reduces health points depending on player health
        for i in range(player.health):
            pygame.draw.rect(
                screen, 
                settings.BORDER_COLOR, (
                    settings.HEALTH_POS_X - i * 40, 
                    settings.HEALTH_POS_Y, 
                    settings.HEALTH_WIDTH, 
                    settings.HEALTH_HEIGHT
                )
            )
            pygame.draw.rect(
                screen, 
                settings.HEALTH_COLOR, (
                    settings.HEALTH_POS_X - i * 40 + 2, 
                    settings.HEALTH_POS_Y + 2, 
                    settings.HEALTH_WIDTH - 4, 
                    settings.HEALTH_HEIGHT - 4
                )
            )

    game_paused_buttons = [
        create_buttons.Button(
            text = "Continue",
            font = "arialblack", 
            size = 25, 
            color = settings.TEXT_COLOR,
            x = settings.SCREEN_WIDTH / 2,
            y = settings.SCREEN_HEIGHT / 2,
            action = toggle_pause_game
        ),
        create_buttons.Button(
            text = "Restart",
            font = "arialblack", 
            size = 25, 
            color = settings.TEXT_COLOR,
            x = settings.SCREEN_WIDTH / 2,
            y = settings.SCREEN_HEIGHT / 2 + 50,
            action = restart_game
        ),
        create_buttons.Button(
            text = "Quit",
            font = "arialblack", 
            size = 25, 
            color = settings.TEXT_COLOR,
            x = settings.SCREEN_WIDTH / 2,
            y = settings.SCREEN_HEIGHT / 2 + 100,
            action = quit_game
        )
    ]

    game_result_buttons = [
        create_buttons.Button(
            text = "Restart",
            font = "arialblack", 
            size = 25, 
            color = settings.TEXT_COLOR,
            x = settings.SCREEN_WIDTH / 2,
            y = settings.SCREEN_HEIGHT / 2,
            action = restart_game
        ),
        create_buttons.Button(
            text = "Quit",
            font = "arialblack", 
            size = 25, 
            color = settings.TEXT_COLOR,
            x = settings.SCREEN_WIDTH / 2,
            y = settings.SCREEN_HEIGHT / 2 + 50,
            action = quit_game
        )
    ]

    wave_count = 1 # Initial wave

    # Spawn 1 enemy in the beginning
    amount = 1
    enemies = spawn_enemies(amount)
    boss = None

    launch_time = time.time()
    total_pause_time = 0
    ingame_timer = 0

    running = True
    paused = False
    game_over = False
    game_won = False

    while running:
        for event in pygame.event.get():     
            # Reset mouse cursor
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.QUIT:
                quit_game()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    toggle_pause_game()

            if paused:
                for button in game_paused_buttons:
                    button.is_hovered()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button.interact()

            if game_over or game_won:
                for button in game_result_buttons:
                    button.is_hovered()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button.interact()

        if not paused and not game_over and not game_won:
            latest_active_time = time.time()
            ingame_timer = latest_active_time - launch_time - total_pause_time

            screen.fill(settings.BACKGROUND_COLOR)

            # Drawing the defense line
            pygame.draw.rect(
                screen, 
                settings.DEFENSE_LINE_COLOR, (
                    settings.DEFENSE_LINE_POS_X, 
                    0, 
                    settings.DEFENSE_LINE_WIDTH, 
                    settings.SCREEN_HEIGHT
                )
            )

            ui()

            # Updating and rendering player
            player.update()
            player.render(screen)

            if not enemies:
                wave_count += 1
                # Decrease player's projectile cooldown every 3rd wave
                if wave_count%3 == 0:
                    settings.projectile_cooldown *= 0.85

                if wave_count < 15:
                    # Increase enemy spawn every wave
                    amount += 1
                    enemies = spawn_enemies(amount)
                else:
                    # Creating the boss
                    boss = enemy_entity.Enemy(
                    x = settings.SCREEN_WIDTH - 20, 
                    y = settings.SCREEN_HEIGHT / 2 - settings.BOSS_HEIGHT / 2, 
                    width = settings.BOSS_WIDTH, 
                    height = settings.BOSS_HEIGHT, 
                    color = settings.BOSS_COLOR, 
                    speed = settings.BOSS_SPEED, 
                    health = settings.BOSS_HEALTH
                    )
                    enemies.append(boss)

            for enemy in enemies[:]:
                # Update and render each enemy
                enemy.update()
                enemy.render(screen)

                # Remove enemy and damage player if it passes defense line
                if enemy.x <= settings.DEFENSE_LINE_POS_X:
                    enemies.remove(enemy)
                    if enemy is boss:
                        player.health = 0
                    else:
                        player.health -= 1

                    if player.health <= 0:
                        game_over = True

                for projectile in player.projectiles[:]:
                    # Check if the projectile's hitbox collides with the enemy's hitbox
                    if projectile.hitbox().colliderect(enemy.hitbox()):
                        # Damage enemy and remove projectile
                        enemy.health -= settings.PROJECTILE_DAMAGE
                        player.projectiles.remove(projectile)

                        if enemy.health <= 0:
                            enemies.remove(enemy)

                            # Win if the killed enemy was the boss
                            if enemy is boss:
                                game_won = True
                        break
        
            for projectile in player.projectiles[:]: 
                # Remove projectiles that leave sight
                if projectile.x > settings.SCREEN_WIDTH:
                    player.projectiles.remove(projectile)
        elif paused and not game_over and not game_won:
            screen.fill(settings.BACKGROUND_COLOR)

            ui()

            display_centered_text(
                text = "Game paused",
                font = "arialblack", 
                size = 40, 
                color = settings.TEXT_COLOR,
                x = settings.SCREEN_WIDTH / 2,
                y = settings.SCREEN_HEIGHT / 3
            )

            for button in game_paused_buttons:
                button.render(screen)
        elif game_over:
            screen.fill(settings.BACKGROUND_COLOR)

            display_centered_text(
                text = "GAME OVER",
                font = "arialblack", 
                size = 40, 
                color = settings.TEXT_COLOR,
                x = settings.SCREEN_WIDTH / 2,
                y = settings.SCREEN_HEIGHT / 4
            )

            display_centered_text(
                text = f"You died on wave {wave_count} after {ingame_timer:.2f} seconds!",
                font = "arialblack", 
                size = 25, 
                color = settings.TEXT_COLOR,
                x = settings.SCREEN_WIDTH / 2,
                y = settings.SCREEN_HEIGHT / 3
            )
            
            for button in game_result_buttons:
                button.render(screen)
        elif game_won:
            screen.fill(settings.BACKGROUND_COLOR)

            ui()

            display_centered_text(
                text = "YOU WON!",
                font = "arialblack", 
                size = 40, 
                color = settings.TEXT_COLOR,
                x = settings.SCREEN_WIDTH / 2,
                y = settings.SCREEN_HEIGHT / 4
            )

            display_centered_text(
                text = f"You beat the boss on wave {wave_count} after {ingame_timer:.2f} seconds!",
                font = "arialblack", 
                size = 25, 
                color = settings.TEXT_COLOR,
                x = settings.SCREEN_WIDTH / 2,
                y = settings.SCREEN_HEIGHT / 3
            )

            for button in game_result_buttons:
                button.render(screen)



        # Update screen
        pygame.display.flip()
        clock.tick(60) # Capping framerate at 60 FPS

if __name__ == "__main__":
    main()