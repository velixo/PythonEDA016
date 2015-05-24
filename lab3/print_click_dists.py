import fix_imports
from cs_eda016.prebuilts import *

old_x = 0
old_y = 0
new_x = 0
new_y = 0
def print_mouse_click_dist(w : SimpleWindow):
	global old_x, old_y, new_x, new_y
	new_x = w.get_mouse_x()
	new_y = w.get_mouse_y()
	print('Avstånd i x-led: ' + str(new_x - old_x) +
				 ' i y-led: ' + str(new_y - old_y))
	old_x = new_x
	old_y = new_y

w = SimpleWindow(600, 600, "PrintClicks")
w.listen_for_mouse_click(print_mouse_click_dist, w)
w.mainloop()
