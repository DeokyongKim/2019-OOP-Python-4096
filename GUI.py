import pygame

pygame.init()

width, height = 500, 500
distance_to_go = 100

TARGET_FPS = 50
clock = pygame.time.Clock()

# 상수 지정해놓기
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (100,0,100)

# POS는 위치임
POS = [0, 0]
player = pygame.image.load("play.jpg")
background = pygame.image.load("spiderman_new universe.jpg")

screen = pygame.display.set_mode((width,height))
while True:
    # 화면을 채운다 / 색깔로
    screen.fill(PURPLE)

    # 배경을 먼저 그려야 함
    for x in range(width//background.get_width()+1):
        for y in range(height//background.get_height()+1):
            screen.blit(background, (x*300, y*300))

    # 모든 요소를 다시 그린다 / 캐릭터들
    screen.blit(player, (POS[0], POS[1]))

    pygame.display.flip()

    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue

        if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                POS[0] += distance_to_go

            if event.key == pygame.K_LEFT:
                POS[0] -= distance_to_go

            if event.key == pygame.K_UP:
                POS[1] -= distance_to_go

            if event.key == pygame.K_DOWN:
                POS[1] += distance_to_go

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)

    clock.tick(TARGET_FPS)
