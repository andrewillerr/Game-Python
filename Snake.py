import pygame
import time
import random

# กำหนดสี
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# กำหนดขนาดหน้าจอ
WIDTH = 600
HEIGHT = 400

# กำหนดขนาดบล็อกของงู
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# สร้างหน้าจอ
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# ฟังก์ชันแสดงคะแนน
def your_score(score):
    font = pygame.font.SysFont("comicsansms", 35)
    score_display = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_display, [0, 0])

# ฟังก์ชันหลัก
def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(WHITE)
            font = pygame.font.SysFont("comicsansms", 35)
            mesg = font.render("You Lost! Press C-Play Again or Q-Quit", True, RED)
            screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)
        pygame.draw.rect(screen, GREEN, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(screen, BLACK, [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK])

        your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.time.Clock().tick(SNAKE_SPEED)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    game_loop()
