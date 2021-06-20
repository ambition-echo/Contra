from pygame.mixer import music
from pygame.locals import*
from pygame import display
from pygame import event
from pygame import image
from pygame import init
from pygame import font


def check():
    global option_y, flag
    flag = 0
    for i in event.get():
        if i.type == QUIT:
            quit()
        if i.type == KEYDOWN:
            if i.key == K_w or i.key == K_UP:
                option_y = 390
                screen.fill((0, 0, 0))
            if i.key == K_s or i.key == K_DOWN:
                option_y = 440
                screen.fill((0, 0, 0))
            if i.key == K_SPACE:
                if option_y == 390:
                    print('1')
                    screen.fill((0, 0, 0))
                    flag = 1
                if option_y == 440:
                    print('2')
                    screen.fill((0, 0, 0))
                    flag = 1


def data_init():
    # 初始化
    global option_y
    option_y = 390
    global screen, title, option0, option1, option2, sign, option
    init()
    display.init()
    font.init()
    display.set_caption('魂斗罗')
    screen = display.set_mode(
        (900, 600), flags=DOUBLEBUF)
    # 加载图片
    title = image.load('img/menu/title.jpeg').convert()
    icon = image.load('img/icon/icon.jpeg').convert_alpha()
    fonts = font.SysFont("consolas", 32)
    option0 = fonts.render("Press Space to Select", True, (255, 255, 255))
    option1 = fonts.render("1  Player", True, (255, 255, 255))
    option2 = fonts.render("2  Players", True, (255, 255, 255))
    sign = fonts.render("© 2021  Hgy|Wzy|Jyx", True, (255, 255, 255))
    option = image.load('img/menu/option.png').convert()
    display.set_icon(icon)
    # 加载音乐
    music.load('audio/title.ogg')
    music.play(loops=-1, start=0.0)


def showmenu():
    global option_y, screen, title, option0, option1, option2, sign, option
    screen.blit(title, (150, 50))
    screen.blit(option0, (250, 350))
    screen.blit(option1, (350, 400))
    screen.blit(option2, (350, 450))
    screen.blit(sign, (250, 500))
    screen.blit(option, (250, option_y))
    # print(option_y)
    display.flip()


def mainmenu():
    data_init()

    while True:
        check()
        if(flag):
            break
        showmenu()


def main():
    mainmenu()


if __name__ == '__main__':
    main()
