import pygame
import time
import random

SNAKE_SPEED = 15

WINDOW_SIZE = (720, 480)

COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WHITE = pygame.Color(255, 255, 255)
COLOR_RED = pygame.Color(255, 0, 0)
COLOR_GREEN = pygame.Color(0, 255, 0)
COLOR_BLUE = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode(WINDOW_SIZE)

fps = pygame.time.Clock()

snake_pos = [100, 50]

snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

fruit_pos = [random.randrange(1, (WINDOW_SIZE[0] // 10)) * 10,
             random.randrange(1, (WINDOW_SIZE[1] // 10)) * 10]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)

    file = open("scores.txt", "w")
    file.write(str(score) + '\n')
    file.close()

    game_over_surface = my_font.render(
        'Your score is ' + str(score), True, COLOR_RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.key.key_code('q'):
                pygame.quit()
                quit()

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (WINDOW_SIZE[0] // 10)) * 10,
                     random.randrange(1, (WINDOW_SIZE[1] // 10)) * 10]

    fruit_spawn = True

    game_window.fill(COLOR_BLACK)

    for pos in snake_body:
        pygame.draw.rect(game_window, COLOR_GREEN,
                         pygame.Rect(
                             pos[0], pos[1], 10, 10)
                         )

    pygame.draw.rect(game_window, COLOR_WHITE, pygame.Rect(
        fruit_pos[0], fruit_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > WINDOW_SIZE[0] - 10:
        if direction == 'LEFT':
            n = 1
        else:
            n = 0

        snake_pos[0] = n*WINDOW_SIZE[0] + (0**n)*(-10)
    if snake_pos[1] < 0 or snake_pos[1] > WINDOW_SIZE[1] - 10:
        if direction == 'UP':
            n = 1
        else:
            n = 0
        snake_pos[1] = n*WINDOW_SIZE[1] + (0**n)*(-10)

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, COLOR_WHITE, 'times new roman', 20)
    pygame.display.update()
    fps.tick(SNAKE_SPEED)