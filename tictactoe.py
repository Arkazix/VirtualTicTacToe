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

        l1 = Line(margin[0] + self.size / 3,
                  margin[1] + self.size / 3,
                  self.size - margin[0],
                  self.size - margin[1])

        line_list = [l1]
        self.draw_line(line_list, img)
        
    def draw_line(self, line_list, img):
        for line in line_list:
            cv2.line(img=img, p1=line.p1, p2=line.p2, color=BLACK, thickness=2, lineType=8)