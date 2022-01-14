import cv2
from line import Line

BLACK = (0, 0, 0)


class TicTacToe:

    def __init__(self, size, WIN_WIDTH, WIN_HEIGHT) -> None:
        self.nb_plays = 0
        self.plays = [(0, 0) for _ in range(9)]
        self.size = size
        self.wsize = (WIN_WIDTH, WIN_HEIGHT)

        if size > min(WIN_WIDTH, WIN_HEIGHT):
            size = min(WIN_WIDTH, WIN_HEIGHT)

    def draw(self, img):
        margin = ((self.wsize[0] - self.size) / 2,
                  (self.wsize[1] - self.size) / 2)

        l1 = Line(margin[0] + self.size/3,
                  margin[1],
                  margin[0] + self.size / 3,
                  margin[1] + self.size)
        
        l2 = Line(margin[0] + 2 * self.size / 3,
                  margin[1],
                  margin[0] + 2 * self.size / 3,
                  margin[1] + self.size)
        
        l3 = Line(margin[0],
                  margin[1] + self.size / 3,
                  margin[0] + self.size,
                  margin[1] + self.size / 3)
        
        l4 = Line(margin[0],
                  margin[1] + 2 * self.size / 3,
                  margin[0] + self.size,
                  margin[1] + 2 * self.size / 3)

        line_list = [l1, l2, l3, l4]
        self.draw_line(line_list, img)
        
    def draw_line(self, line_list, img):
        for line in line_list:
            cv2.line(img=img, pt1=line.p1, pt2=line.p2, color=BLACK, thickness=2, lineType=8)