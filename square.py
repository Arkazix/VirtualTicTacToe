class Square:
    
    def __init__(self, x, y, l, n):
        self.cx = x
        self.cy = y
        self.cl = l
        self.n = n
        
    def is_in_square(self, px, py):
        in_ = (px > self.cx) and (py > self.cy) and (py < (self.cy + self.cl)) and (px < (self.cx + self.cl))
        return self.n if in_ else -1
            