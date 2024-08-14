import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 6

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

left_paddle = pygame.Rect(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

left_score = 0
right_score = 0

font = pygame.font.Font(None, 74)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
        right_paddle.y += PADDLE_SPEED

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0:
        right_score += 1
        ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    if ball.right >= SCREEN_WIDTH:
        left_score += 1
        ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = -ball_speed_x

    screen.fill(BLACK)

    left_text = font.render(str(left_score), True, WHITE)
    screen.blit(left_text, (SCREEN_WIDTH // 4, 20))
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(right_text, (SCREEN_WIDTH * 3 // 4, 20))

    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
