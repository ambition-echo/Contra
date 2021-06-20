import enemy
from pygame import image


def check(x, y, target):

    if target.x <= x <= target.x+target.width:
        if target.y <= y <= target.y+target.height:
            return 1
        else:
            return 0
    else:
        return 0


class bullet(object):
    def __init__(self, direction, x, y, speed):
        self.direction = direction
        self.x = x
        self.y = y
        self.speed = speed
        self.url = image.load('img/bullet/bullet1.png')

    def boom(self, target):
        if check(self.x, self.y, target):
            print('Booooooooom!!!!!!!!!!!!!!!!')
            self.direction = 'o'
            return 1

    def move(self):
        if self.direction != 'o':
            if self.direction == 'r':
                self.x += self.speed
            if self.direction == 'l':
                self.x -= self.speed
            if self.direction == 'u':
                self.y -= self.speed
            if self.direction == 'd':
                self.y += self.speed
            if self.direction == 'ru':
                self.x += self.speed*0.707
                self.y -= self.speed*0.707
            if self.direction == 'ld':
                self.x -= self.speed*0.707
                self.y += self.speed*0.707
            if self.direction == 'lu':
                self.y -= self.speed*0.707
                self.x -= self.speed*0.707
            if self.direction == 'rd':
                self.y += self.speed*0.707
                self.x += self.speed*0.707


if __name__ == '__main__':
    b1 = bullet('r', 300, 300, 0.5)
    e1 = enemy.enemy(0, 0, 100, 100)
    b1.boom(e1)
