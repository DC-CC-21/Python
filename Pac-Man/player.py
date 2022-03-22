from constants import BLOCKSIZE as BSIZE
import pyray as pr
class Player:
    def __init__(self,pos) -> None:
        print(pos)
        self.x = int(pos['x']+(BSIZE-pos['w'])/2)
        self.y = int(pos['y']+(BSIZE-pos['h'])/2)
        self.w = pos['w']
        self.h = pos['h']

    def display(self):
        pr.draw_rectangle(self.x, self.y, self.w, self.h,pr.RED)        