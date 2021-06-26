from pygame import image


class enemy(object):
    def __init__(self, x, y, width, height):
        self.life = 3
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.url = image.load('img/enemy/***.png')


class player(object):
    def __init__(self, x, y, width, height):
        self.life = 3
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.player0 = image.load('img/P1/R/player0.png')
        self.down_r = image.load('img/P1/R/down.png')
        self.down_l = image.load('img/P1/L/down.png')
        self.up_r = image.load('img/P1/R/up.png')
        self.up_l = image.load('img/P1/L/up.png')
        self.url_r = [image.load('img/P1/R/player1.png'), image.load('img/P1/R/player2.png'),
                      image.load('img/P1/R/player3.png'), image.load('img/P1/R/player4.png'), image.load('img/P1/R/player5.png')]
        self.url_l = [image.load('img/P1/L/player1.png'), image.load('img/P1/L/player2.png'),
                      image.load('img/P1/L/player3.png'), image.load('img/P1/L/player4.png'), image.load('img/P1/L/player5.png')]

        self.shooting = image.load('img/P1/R/shooting3.png')
