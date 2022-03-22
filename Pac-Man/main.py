import pyray as pr
from game import Game
import constants as const

g = Game()
g.createLevel()

pr.init_window(const.CANVASSIZE,const.CANVASSIZE, "Hello")
while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
    g.display()
    pr.draw_text("Hello world", 190, 200, 20, pr.VIOLET)
    pr.end_drawing()
pr.close_window()


