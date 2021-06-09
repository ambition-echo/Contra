from tkinter import Y
from pygame.mixer import music
from pygame.locals import*
from pygame import display
from pygame import event
from pygame import image
from pygame import init


def data_init():
    global screen, title, P1, x, y
    global move_y_u, move_y_d, move_x_r, move_x_l
    x, y = 0, 180
    move_y_u, move_y_d, move_x_r, move_x_l = 0, 0, 0, 0
    init()
    screen = display.set_mode(
        (900, 600), flags=DOUBLEBUF)
    # 加载图片
    title = image.load('img/map/map.png').convert()
    P1 = image.load('img/P1/R/player.png').convert_alpha()
    music.load('audio/background.ogg')
    music.play(loops=-1, start=0.0)


def check():
    global move_x_l, move_x_r, move_y_u, move_y_d
    for i in event.get():
        # 按关闭按钮时退出
        if i.type == QUIT:
            exit()
        # 检测按键输入
        try:
            if i.key == K_w:
                move_y_u = 0.2
            elif i.key == K_s:
                move_y_d = 0.2
            elif i.key == K_a:
                move_x_l = 0.2
            elif i.key == K_d:
                move_x_r = 0.2
        except:
            pass
        # 按键弹起后归零
        if i.type == KEYUP:
            if i.key == K_w:
                move_y_u = 0
            elif i.key == K_s:
                move_y_d = 0
            elif i.key == K_a:
                move_x_l = 0
            elif i.key == K_d:
                move_x_r = 0


def show():
    global option_y, screen, title, x, y, move_y_u, move_y_d, move_x_r, move_x_l, P1
    screen.blit(title, (x, 0))
    screen.blit(P1, (450, y))
    x += move_x_l-move_x_r
    y += move_y_d-move_y_u

    display.flip()


def maingame():
    data_init()
    while True:
        check()
        show()


def main():
    maingame()


if __name__ == '__main__':
    main()
