from msilib.schema import Directory
from pygame.mixer import music
from pygame.locals import*
from pygame import display
from pygame import event
from pygame import image
from pygame import init
import threading
import bullet
import enemy


def data_init():
    global screen, mapp, P1, p1, bullets, p_c, c, p_cc, direction
    direction = 'r'
    p_c = 0
    p_cc = 0
    c = 0
    bullets = []
    global move_y_u, move_y_d, move_x_r, move_x_l
    move_y_u, move_y_d, move_x_r, move_x_l = 0, 0, 0, 0
    init()
    p1 = enemy.player(0, 180, 100, 100)
    screen = display.set_mode(
        (900, 600), flags=DOUBLEBUF)
    # 加载图片
    mapp = image.load('img/map/map.png').convert()
    P1 = p1.url_r[p_c]
    music.load('audio/background.ogg')
    music.play(loops=-1, start=0.0)


def check():
    global move_x_l, move_x_r, move_y_u, move_y_d, P1, p1, p_c, c, p_cc, direction
    for i in event.get():
        # 按关闭按钮时退出
        if i.type == QUIT:
            exit()
        # 检测按键输入
        if i.type == KEYDOWN:
            if i.key == K_w:
                if c == 1:
                    if direction == 'r':
                        direction = 'ru'
                    else:
                        direction = 'lu'
                else:
                    if direction == 'r':
                        P1 = p1.up_r
                        p1.y -= 30
                    else:
                        P1 = p1.up_l
                        p1.y -= 30
                    #direction = 'u'
            elif i.key == K_s:
                if direction == 'r':
                    P1 = p1.down_r
                    p1.y += 65
                if direction == 'l':
                    P1 = p1.down_l
                    p1.y += 65
                move_x_l = 0
                move_x_r = 0
            elif i.key == K_a:
                move_x_l = 0.3
                direction = 'l'
                c = 1
            elif i.key == K_d:
                move_x_r = 0.3
                direction = 'r'
                c = 1
            elif i.key == K_j:
                if P1 == p1.down_l or P1 == p1.down_r:
                    if direction == 'r':
                        bullets.append(bullet.bullet(
                            direction, 580, p1.y+15, 0.7))
                    else:
                        bullets.append(bullet.bullet(
                            direction, 420, p1.y+15, 0.7))
                else:
                    P1 = p1.shooting
                    if direction == 'r':
                        bullets.append(bullet.bullet(
                            direction, 550, p1.y+25, 0.7))
                    else:
                        bullets.append(bullet.bullet(
                            direction, 420, p1.y+25, 0.7))

        # 按键弹起后归零
        if i.type == KEYUP:
            if i.key == K_w:
                if direction == 'r':
                    P1 = p1.url_r[p_cc]
                    p1.y += 30
                if direction == 'l':
                    P1 = p1.url_l[p_cc]
                    p1.y += 30
            elif i.key == K_s:
                if direction == 'r':
                    P1 = p1.url_r[p_cc]
                    p1.y -= 65
                    #move_x_r = 0.3
                if direction == 'l':
                    P1 = p1.url_l[p_cc]
                    p1.y -= 65
                    #move_x_l = 0.3
            elif i.key == K_a:
                move_x_l = 0
                c = 0
                p_c = 0
            elif i.key == K_d:
                move_x_r = 0
                c = 0
                p_c = 0
            elif i.key == K_j:
                if P1 == p1.down_l or P1 == p1.down_r:
                    pass
                else:
                    P1 = p1.player0
    p1.x += move_x_l-move_x_r
    p1.y += move_y_d-move_y_u
    p_c += c
    p_c %= 480
    if 0 <= p_c < 80:
        p_cc = 0
    if 80 <= p_c < 160:
        p_cc = 1
    if 160 <= p_c < 240:
        p_cc = 2
    if 240 <= p_c < 320:
        p_cc = 3
    if 320 <= p_c < 400:
        p_cc = 4
    if 400 <= p_c < 480:
        p_cc = 5
    if direction == 'r' and P1 != p1.down_r and P1 != p1.down_l and P1 != p1.up_r and P1 != p1.up_l:
        P1 = p1.url_r[p_cc]
    if direction == 'l' and P1 != p1.down_r and P1 != p1.down_l and P1 != p1.up_r and P1 != p1.up_l:
        P1 = p1.url_l[p_cc]
    for i in bullets:
        i.move()
        if i.x > 900 or i.x < 0 or i.y < 0 or i.y > 600:
            bullets.remove(i)


def show():
    global option_y, screen, mapp, p1, move_y_u, move_y_d, move_x_r, move_x_l, P1
    screen.blit(mapp, (p1.x, 0))
    screen.blit(P1, (450, p1.y))
    for i in bullets:
        screen.blit(i.url, (i.x, i.y))

    display.flip()


def maingame():
    data_init()
    threading.Thread()
    while True:
        check()
        show()


def main():
    maingame()


if __name__ == '__main__':
    main()
