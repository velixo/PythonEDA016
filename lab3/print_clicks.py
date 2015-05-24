import fix_imports
from cs_eda016.prebuilts import *

def print_mouse_pos(w : SimpleWindow):
	print('x = ' + str(w.get_mouse_x()) + ', ' + 'y = ' + str(w.get_mouse_y()))

w = SimpleWindow(600, 600, "PrintClicks")
w.listen_for_mouse_click(print_mouse_pos, w)
w.mainloop()
