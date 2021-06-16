class enemy(object):
    def __init__(self, x, y, width, height):
        self.life = 3
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.url = 'img/enemy/***.png'


class player(object):
    def __init__(self, x, y, width, height):
        self.life = 3
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.url = 'img/P1/R/player.png'
