import cv2
from line import Line
from square import Square

BLACK = (0, 0, 0)
RED = (255, 0, 0)


class TicTacToe:

    def __init__(self, size, WIN_WIDTH, WIN_HEIGHT) -> None:
        self.nb_plays = 0
        self.plays = [(0, 0) for _ in range(9)]
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
    
    def draw_circle(self, img, s):
        cv2.circle(img, (int(s.cx + self.size / 6), int(s.cy + self.size / 6)), 32, RED, 2)

    def is_in(self, p1, p2):
        x = (p1.x * self.wsize[0] + p2.x * self.wsize[0]) / 2
        y = (p1.y * self.wsize[1] + p2.y * self.wsize[1]) / 2
        
        in_ = -1
        for s in self.square_list:
            in_ = s.is_in_square(x, y)
            if in_ != -1:
                return in_
        return in_