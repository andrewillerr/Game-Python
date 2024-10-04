import pygame
import random

# กำหนดขนาดหน้าจอ
WIDTH = 300
HEIGHT = 600
BLOCK_SIZE = 30

# กำหนดสี
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# รูปแบบของบล็อกในเกม Tetris
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 0], [1, 1, 1]]   # T
]

# ฟังก์ชันสำหรับการสร้างบล็อกใหม่
def create_shape():
    return random.choice(SHAPES)

# ฟังก์ชันสำหรับการตรวจสอบการชนกัน
def check_collision(board, shape, offset):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] != 0:
                x = col + offset[1]
                y = row + offset[0]
                if x < 0 or x >= len(board[0]) or y >= len(board) or (y >= 0 and board[y][x] != 0):
                    return True
    return False

# ฟังก์ชันสำหรับการลบแถวที่เต็ม
def clear_lines(board):
    lines_to_clear = []
    for i, row in enumerate(board):
        if all(cell != 0 for cell in row):
            lines_to_clear.append(i)
    for i in lines_to_clear:
        del board[i]
        board.insert(0, [0 for _ in range(len(board[0]))])
    return len(lines_to_clear)

# ฟังก์ชันหลัก
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")

    board = [[0 for _ in range(WIDTH // BLOCK_SIZE)] for _ in range(HEIGHT // BLOCK_SIZE)]

    current_shape = create_shape()
    current_position = [0, WIDTH // BLOCK_SIZE // 2 - len(current_shape[0]) // 2]

    score = 0
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 500  # Speed of the falling blocks in milliseconds

    while True:
        fall_time += clock.get_rawtime()
        if fall_time >= fall_speed:
            current_position[0] += 1
            if check_collision(board, current_shape, current_position):
                current_position[0] -= 1
                for row in range(len(current_shape)):
                    for col in range(len(current_shape[row])):
                        if current_shape[row][col] != 0:
                            board[current_position[0] + row][current_position[1] + col] = 1
                score += clear_lines(board) * 100  # Update score for cleared lines
                current_shape = create_shape()
                current_position = [0, WIDTH // BLOCK_SIZE // 2 - len(current_shape[0]) // 2]
                if check_collision(board, current_shape, current_position):  # Game Over condition
                    print("Game Over")
                    pygame.quit()
                    return
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_position[1] -= 1
                    if check_collision(board, current_shape, current_position):
                        current_position[1] += 1
                elif event.key == pygame.K_RIGHT:
                    current_position[1] += 1
                    if check_collision(board, current_shape, current_position):
                        current_position[1] -= 1
                elif event.key == pygame.K_DOWN:
                    current_position[0] += 1
                    if check_collision(board, current_shape, current_position):
                        current_position[0] -= 1
                elif event.key == pygame.K_UP:  # Rotate shape
                    current_shape = [list(row) for row in zip(*current_shape[::-1])]
                    if check_collision(board, current_shape, current_position):
                        current_shape = [list(row) for row in zip(*current_shape)][::-1]

        screen.fill(WHITE)

        # วาดบอร์ด
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != 0:
                    pygame.draw.rect(screen, BLUE, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # วาดบล็อกปัจจุบัน
        for row in range(len(current_shape)):
            for col in range(len(current_shape[row])):
                if current_shape[row][col] != 0:
                    pygame.draw.rect(screen, RED, ((current_position[1] + col) * BLOCK_SIZE, 
                                                      (current_position[0] + row) * BLOCK_SIZE, 
                                                      BLOCK_SIZE, BLOCK_SIZE))

        # แสดงคะแนน
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, GREEN)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
