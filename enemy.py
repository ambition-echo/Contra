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
        self.player0 = image.load('img/P1/R/player.png')
        self.player1 = image.load('img/P1/R/player1.png')
        self.player2 = image.load('img/P1/R/player2.png')
        self.player3 = image.load('img/P1/R/player3.png')
        self.player4 = image.load('img/P1/R/player4.png')
        self.player5 = image.load('img/P1/R/player5.png')
        self.url = [self.player0, self.player1, self.player2,
                    self.player3, self.player4, self.player5]

        self.shooting = image.load('img/P1/R/shooting3.png')
