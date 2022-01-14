# A point class

class Point:

    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def __sum__(self, __o: object):
        return Point(self.x + __o.x, self.y + __o.y)

    def __eq__(self, __o: object) -> bool:
        return (self.x == __o.x) and (self.y == __o.y)

    def dist(self, __o):
        return ((__o.x - self.x) ** 2 + (__o.y - self.y) ** 2) ** (1 / 2)
