import pygame
import random

# กำหนดขนาดหน้าจอ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# กำหนดสี
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# ฟังก์ชันหลัก
def main():
    pygame.init()

    # สร้างหน้าจอ
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dodge the Falling Blocks")

    # กำหนดตัวละคร
    player_size = 50
    player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
    enemy_size = 50
    enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_size), 0]

    # กำหนดความเร็ว
    enemy_speed = 10

    # ตั้งค่าระยะเวลา
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # เคลื่อนที่ตัวละคร
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 10
        if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
            player_pos[0] += 10

        # เคลื่อนที่อุปสรรค
        if enemy_pos[1] >= 0 and enemy_pos[1] < SCREEN_HEIGHT:
            enemy_pos[1] += enemy_speed
        else:
            enemy_pos[1] = 0
            enemy_pos[0] = random.randint(0, SCREEN_WIDTH - enemy_size)

        # ตรวจสอบการชน
        if (player_pos[0] < enemy_pos[0] < player_pos[0] + player_size or
                player_pos[0] < enemy_pos[0] + enemy_size < player_pos[0] + player_size) and \
                (player_pos[1] < enemy_pos[1] < player_pos[1] + player_size or
                 player_pos[1] < enemy_pos[1] + enemy_size < player_pos[1] + player_size):
            game_over = True

        # วาดตัวละครและอุปสรรค
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))
        pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

        # อัปเดตหน้าจอ
        pygame.display.update()

        # ตั้งค่า FPS
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
