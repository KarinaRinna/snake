import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True,'A': True, 'D': True, }
length = 1
snake = [(x,y)]
dx, dy = 0, 0
score = 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time. Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)


while True:
    sc.fill(pygame.Color('black'))
    # рисуем змею
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE, SIZE)))for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('Cyan'),(*apple, SIZE,SIZE))
    # вывод очков
    render_score = font_score.render(f'Ваш счет: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    # передвижение змейки за 1 шаг равно размеру ее головы
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    # съесть яблоко
    if snake[-1] == apple:  # если яблоко находится в положении головы змеи
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE) # создаем новое яблоко
        length += 1 # ширину змейки увеличиваем на 1
        score += 1  # при сьедании очки +1
        fps += 1    # скорость змейки +1

    # игра окончена
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #Управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True, } # если движение вверх, то нельзя повернуть вниз
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True, }



# https://www.youtube.com/watch?v=2KRGwOlNAUA&list=WL&index=199