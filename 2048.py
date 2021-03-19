import pygame
from random import randint

pygame.init()

WIDTH = 1000
HEIGHT = 600

GREY = (150,150,150)

BLUE = (124, 156, 160)

WHITE = (255, 255, 255)

res = []
for i in range(0, 4):
    res.append([])
    for j in range(0 ,4):
        res[i].append(0)
i = randint(0, 3)
j = randint(0, 3)
res[i][j] = 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def process_arr(arr, start):
    # for i in arr:
    #     print(i, end='  ')
    # print(end='\n')
    # print('--------')
    step = 1
    if start == 3:
        step = -1
    for i in range(start, 3 - start, step):
        for j in range(i+step, (4-start)*step, step):
            if arr[j] == 0: 
                continue
            if arr[i] == arr[j] or arr[i] * arr[j] == 0:
                arr[i] += arr[j]
                arr[j] = 0
            if arr[i] * arr[j] != 0:
                break

def vert_update_value(start):
    global res
    arr = []
    for i in range(0, 4) :
        arr.append(0)
    check = False
    for j in range(0, 4):
        for i in range(0, 4):
            arr[i] = res[i][j]
        process_arr(arr, start)
        # for i in arr:
        #     print(i, end='  ')
        # print(end='\n')
        # print('---------')
        for i in range(0, 4) :
            res[i][j] = arr[i]
        if res[3-start][j] == 0:
            check = True
    while check:
        p = randint(0, 3)
        if res[3-start][p] == 2 or res[3-start][p] == 0:
            res[3-start][p] += 2
            check = False

def hori_update_value(start):
    global res, game_status
    arr = []
    for i in range(0, 4) :
        arr.append(0)
    checl = False
    for i in range(0, 4):
        for j in range(0, 4):
            arr[j] = res[i][j]
        process_arr(arr, start)
        # for j in arr:
        #     print(j, end='  ')
        # print(end='\n')
        # print('---------')
        for j in range(0, 4) :
            res[i][j] = arr[j]
        if res[i][3-start] == 0:
            check = True
    while check:
        p = randint(0, 3)
        if res[p][3-start] == 2 or res[p][3-start] == 0:
            res[p][3-start] += 2
            check = False

def print_num(res):
    pos_x = 305
    pos_y = 105
    for i in range(0, 4):
        for j in range(0, 4):
            if res[i][j] != 0:
                num = str(res[i][j]) + ".png"
                print_num = pygame.image.load(num)
                screen.blit(print_num, (pos_x, pos_y))
            pos_x += 100
        pos_y += 100
        pos_x = 305

running = True
while running:
    
    background = pygame.image.load("background.png")
    screen.blit(background, (0,0))
    
    #duong doc
    pygame.draw.rect(screen ,BLUE, (295, 95, 10, 410))
    pygame.draw.rect(screen ,BLUE, (395, 95, 10, 410))
    pygame.draw.rect(screen ,BLUE, (495, 95, 10, 410))
    pygame.draw.rect(screen ,BLUE, (595, 95, 10, 410))
    pygame.draw.rect(screen ,BLUE, (695, 95, 10, 410))

    #duong ngang
    pygame.draw.rect(screen ,BLUE, (295, 95, 410, 10))
    pygame.draw.rect(screen ,BLUE, (295, 195, 410, 10))
    pygame.draw.rect(screen ,BLUE, (295, 295, 410, 10))
    pygame.draw.rect(screen ,BLUE, (295, 395, 410, 10))
    pygame.draw.rect(screen ,BLUE, (295, 495, 410, 10)) 

    print_num(res)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
                hori_update_value(3)

            elif event.key == pygame.K_LEFT:
                print("LEFT")
                hori_update_value(0)

            elif event.key == pygame.K_UP:
                print("UP")
                vert_update_value(0)

            elif event.key == pygame.K_DOWN:
                print("DOWN")
                vert_update_value(3)    

    pygame.display.flip()

pygame.quit()
