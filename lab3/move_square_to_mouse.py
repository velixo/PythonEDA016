import fix_imports
from cs_eda016.prebuilts import *

def move_square_to_mouse(sq, w):
	sq.erase(w)
	x = w.get_mouse_x() - sq.get_x()
	y = w.get_mouse_y() - sq.get_y()
	sq.move(x, y)
	sq.draw(w)

w = SimpleWindow(600, 600, "MoveSquareToMouse")
sq = Square(100, 100, 100)
sq.draw(w)
sq.erase(w)
w.listen_for_mouse_click(move_square_to_mouse, sq, w)
w.mainloop()