import pygame
import random

# กำหนดขนาดหน้าจอ
WIDTH = 400
HEIGHT = 600

# กำหนดสี
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# ฟังก์ชันหลัก
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    bird_pos = [100, HEIGHT // 2]
    bird_velocity = 0
    gravity = 0.5
    flap_strength = -10

    pipes = []
    for i in range(3):
        pipe_height = random.randint(150, 400)
        pipes.append([WIDTH + i * 200, pipe_height])

    clock = pygame.time.Clock()
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird_velocity = flap_strength
                if event.key == pygame.K_r and game_over:  # กด R เพื่อเริ่มเกมใหม่
                    main()  # เรียกฟังก์ชัน main ใหม่เพื่อรีเซ็ตเกม

        if not game_over:
            bird_velocity += gravity
            bird_pos[1] += bird_velocity

            # อัปเดตตำแหน่งท่อ
            for pipe in pipes:
                pipe[0] -= 5
                if pipe[0] < -50:
                    pipe[0] = WIDTH
                    pipe[1] = random.randint(150, 400)
                    score += 1  # เพิ่มคะแนนเมื่อท่อผ่าน

                # ตรวจสอบการชนกัน
                if (pipe[0] < bird_pos[0] + 20 < pipe[0] + 50) and (
                    bird_pos[1] < pipe[1] or bird_pos[1] + 20 > pipe[1] + 150):
                    game_over = True  # เปลี่ยนสถานะเกมเป็น Game Over

        screen.fill(WHITE)
        pygame.draw.circle(screen, GREEN, (bird_pos[0], int(bird_pos[1])), 20)

        # วาดท่อ
        for pipe in pipes:
            pygame.draw.rect(screen, GREEN, (pipe[0], 0, 50, pipe[1]))
            pygame.draw.rect(screen, GREEN, (pipe[0], pipe[1] + 150, 50, HEIGHT))

        # แสดงคะแนน
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # แสดงข้อความ Game Over
        if game_over:
            game_over_text = font.render("Game Over! Press R to Restart", True, BLACK)
            screen.blit(game_over_text, (50, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
