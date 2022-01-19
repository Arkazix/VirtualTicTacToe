import cv2
from src.line import Line
from src.square import Square

BLACK = (0, 0, 0)
RED = (0, 0, 255)


class TicTacToe:

    def __init__(self, size, WIN_WIDTH, WIN_HEIGHT) -> None:
        self.nb_plays = 0
        self.plays = [[-1, None] for _ in range(9)] # (0: circle, 1: cross)
        self.size = size
        self.wsize = (WIN_WIDTH, WIN_HEIGHT)

        if size > min(WIN_WIDTH, WIN_HEIGHT):
            size = min(WIN_WIDTH, WIN_HEIGHT)
        
        self.margin = ((self.wsize[0] - self.size) / 2,
                       (self.wsize[1] - self.size) / 2)
        self.lines_list = self.get_lines()
        self.square_list = self.get_square_list()

    def get_lines(self):
        l1 = Line(self.margin[0] + self.size/3,
                  self.margin[1],
                  self.margin[0] + self.size / 3,
                  self.margin[1] + self.size)

        l2 = Line(self.margin[0] + 2 * self.size / 3,
                  self.margin[1],
                  self.margin[0] + 2 * self.size / 3,
                  self.margin[1] + self.size)

        l3 = Line(self.margin[0],
                  self.margin[1] + self.size / 3,
                  self.margin[0] + self.size,
                  self.margin[1] + self.size / 3)

        l4 = Line(self.margin[0],
                  self.margin[1] + 2 * self.size / 3,
                  self.margin[0] + self.size,
                  self.margin[1] + 2 * self.size / 3)

        return [l1, l2, l3, l4]

    def draw_line(self, img):
        for line in self.lines_list:
            cv2.line(img=img, pt1=line.p1, pt2=line.p2,
                     color=BLACK, thickness=2, lineType=8)
            
    def get_square_list(self):
        square_list = []
        for h in range(3):
            for w in range(3):
                square_list.append(Square(self.margin[0] + w * self.size / 3,
                                          self.margin[1] + h * self.size / 3,
                                          self.size / 3, 3 * h + w))
        return square_list
    
    def get_square(self, n):
        if n < 0 or n > 8:
            return -1
        return self.square_list[n]
    
    def add_shape(self, n, is_circle, square):
        if self.plays[n][0] == -1:
            self.plays[n][0] = (is_circle == False)
            self.plays[n][1] = square
            return 0
        return -1
    
    def draw_shape(self, img):
        l_m = self.size / 16
        for c in self.plays:
            if c[0] == 0:
                cv2.circle(img, (int(c[1].cx + self.size / 6),
                                 int(c[1].cy + self.size / 6)),
                                int(self.size/9), RED, 2)
            elif c[0] == 1:
                l1 = Line(c[1].cx + l_m, c[1].cy + l_m,
                          c[1].cx + self.size / 3 - l_m,
                          c[1].cy + self.size / 3 - l_m)
                l2 = Line(c[1].cx + self.size / 3 - l_m, c[1].cy + l_m,
                          c[1].cx + l_m, c[1].cy + self.size / 3 - l_m)
                cv2.line(img=img, pt1=l1.p1, pt2=l1.p2, color=RED, thickness=2,
                         lineType=8)
                cv2.line(img=img, pt1=l2.p1, pt2=l2.p2, color=RED, thickness=2,
                         lineType=8)
                    
    def is_in(self, p1, p2):
        x = (p1.x * self.wsize[0] + p2.x * self.wsize[0]) / 2
        y = (p1.y * self.wsize[1] + p2.y * self.wsize[1]) / 2
        
        in_ = -1
        for s in self.square_list:
            in_ = s.is_in_square(x, y)
            if in_ != -1:
                return in_
        return in_