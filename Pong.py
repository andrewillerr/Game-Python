import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 10

# Ball settings
BALL_SIZE = 15

# Game variables
player1_score = 0
player2_score = 0
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

# Paddle positions
paddle1_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle2_y = (HEIGHT - PADDLE_HEIGHT) // 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= PADDLE_WIDTH and paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT) or \
       (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT):
        ball_speed_x *= -1
    # Ball goes out of bounds
    elif ball_x < 0:
        player2_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Reset ball position
        ball_speed_x = 5 * random.choice((1, -1))
        ball_speed_y = 5 * random.choice((1, -1))
        
    elif ball_x > WIDTH:
        player1_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Reset ball position
        ball_speed_x = 5 * random.choice((1, -1))
        ball_speed_y = 5 * random.choice((1, -1))

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    
    # Draw scores
    font = pygame.font.Font(None, 74)
    score_text = font.render(f"{player1_score} : {player2_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
