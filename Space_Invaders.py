import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player settings
player_width = 50
player_height = 50
player_speed = 5

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 7

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemy_spawn_rate = 60  # Increase this value to reduce the frequency of new enemies

# Create player
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10

# Create bullets
bullets = []

# Create enemies
enemies = []

# Create helpers
helpers = []

# Game variables
score = 0
lives = 3
frame_count = 0  # To control the enemy spawning
is_helper_active = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit number of bullets on screen
            bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])
    
    # Secret key combination for helpers
    if keys[pygame.K_a] and keys[pygame.K_u] and keys[pygame.K_n]:
        if not is_helper_active:
            is_helper_active = True
            for _ in range(3):  # Create 3 helpers
                helpers.append([random.randint(0, WIDTH - player_width), HEIGHT - player_height - 50])

    # Move bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:  # Remove bullet if it goes off screen
            bullets.remove(bullet)

    # Move helpers and make them shoot
    for helper in helpers[:]:
        if random.randint(0, 50) == 0:  # Random chance to shoot
            bullets.append([helper[0] + player_width // 2 - bullet_width // 2, helper[1]])
        
        # Optional: Move helpers down the screen (if you want)
        helper[1] += 1
        if helper[1] > HEIGHT:  # Reset helper position if it goes off screen
            helpers.remove(helper)

    # Move enemies
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:  # Reset enemy position if it goes off screen
            enemy[0] = random.randint(0, WIDTH - enemy_width)
            enemy[1] = random.randint(50, 150)
            lives -= 1  # Lose a life when enemy reaches the bottom
            if lives <= 0:  # Prevent lives from going below 0
                lives = 0
                running = False  # End the game if lives reach 0

    # Check for collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (bullet[0] < enemy[0] + enemy_width and
                bullet[0] + bullet_width > enemy[0] and
                bullet[1] < enemy[1] + enemy_height and
                bullet[1] + bullet_height > enemy[1]):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10  # Increment score for destroying an enemy

                # Spawn a new enemy
                new_enemy_x = random.randint(0, WIDTH - enemy_width)
                new_enemy_y = random.randint(50, 150)
                enemies.append([new_enemy_x, new_enemy_y])

    # Spawn new enemies periodically
    frame_count += 1
    if frame_count % enemy_spawn_rate == 0:
        new_enemy_x = random.randint(0, WIDTH - enemy_width)
        new_enemy_y = 0  # Start from the top of the screen
        enemies.append([new_enemy_x, new_enemy_y])

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))
    
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Draw helpers
    for helper in helpers:
        pygame.draw.rect(screen, WHITE, (helper[0], helper[1], player_width, player_height))

    # Draw score and lives
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, RED)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    pygame.display.flip()
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
