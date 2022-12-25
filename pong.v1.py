import pygame
import sys

# здесь определяются константы,
# классы и функции
FPS = 60
SCREEN_WIDTH=1920
SCREEN_HEIGHT=1000
BAT_WIDTH=20
BAT_HEIGHT=120
BAT_OFFSET=10
BAT_2_WIDTH=20
BAT_2_HEIGHT=120
BAT_2_OFFSET=10
# здесь происходит инициация,
# создание объектов

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
ORANGE = (255,155,100)
BLACK = (0,0,0)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
sc = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))

# радиус круга
r = 20
# координаты круга
# скрываем за левой границей
ball_x = SCREEN_WIDTH//2
# выравнивание по центру по вертикали
ball_y = SCREEN_HEIGHT // 2
# скорости мяча
ball_speed_x=5
ball_speed_y=4
#КООРДИНАТЫ РАКЕТКИ
bat_x=BAT_OFFSET
bat_y=(SCREEN_HEIGHT-BAT_HEIGHT)//2
#скорость ракетки
bat_speed_y=0
#КООРДИНАТЫ РАКЕТКИ
bat_2_x=SCREEN_WIDTH-BAT_2_OFFSET-BAT_2_WIDTH
bat_2_y=(SCREEN_HEIGHT-BAT_2_HEIGHT)//2
#скорость ракетки
bat_2_speed_y=0
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # передвигаем мяч по экарну
    ball_x+=ball_speed_x
    ball_y+=ball_speed_y
    #выход за левый кран экрана
    if ball_x <= r:
        # летел налево - полетел направо
        ball_speed_x=-ball_speed_x
    if ball_x>= SCREEN_WIDTH - r:
        #летел направо - полетел налево
        ball_speed_x= -ball_speed_x
    #выход за верхний край
    if ball_y>= SCREEN_HEIGHT - r:
        #летел наверх-полетел вниз
        ball_speed_y=-ball_speed_y
    #выход за нижний край
    if ball_y<=r:
        #летел вниз-полетел наверх
        ball_speed_y=-ball_speed_y
    #передвигаем ракетку по экрану
    bat_y+=bat_speed_y
    bat_2_y+=bat_2_speed_y

    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_w]:
        bat_speed_y+=-1
    elif keys[pygame.K_s]:
        bat_speed_y += 1
    else:
        bat_speed_y=0
    if bat_y<=0:
        bat_y = 0
    if bat_y >= SCREEN_HEIGHT - BAT_HEIGHT:
        bat_y = SCREEN_HEIGHT - BAT_HEIGHT
        
    if keys[pygame.K_UP]:
        bat_2_speed_y+=-1
    elif keys[pygame.K_DOWN]:
        bat_2_speed_y += 1
    else:
        bat_2_speed_y=0
    if bat_2_y<=0:
        bat_2_y = 0
    if bat_2_y >= SCREEN_HEIGHT - BAT_2_HEIGHT:
        bat_2_y = SCREEN_HEIGHT - BAT_2_HEIGHT
        
    
    # заливаем фон
    sc.fill(BLACK)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    pygame.draw.rect(sc, WHITE,(bat_x,bat_y,BAT_WIDTH,BAT_HEIGHT))
    pygame.draw.rect(sc, WHITE,(bat_2_x,bat_2_y,BAT_2_WIDTH,BAT_2_HEIGHT))
    # обновляем окно
    pygame.display.update()


    clock.tick(FPS)
