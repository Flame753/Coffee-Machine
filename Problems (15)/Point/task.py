from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        dif_x = (self.x - point.x)**2
        dif_y = (self.y - point.y)**2
        return sqrt(dif_x + dif_y)

