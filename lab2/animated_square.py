import fix_imports
from cs_eda016.prebuilts import *

dim = int(input("Skriv förminskning: "))
w = SimpleWindow(600, 600, "DrawManySquares")
sq = Square(300, 300, 200)

counter = 0
while sq.get_side() > 0:
	sq.side -= dim
	side = sq.side
	w.canvas.after(counter*200, sq.draw, w, side)
	counter += 1

#while sq.get_side() > 0:
#	sq._draw(w)
#	sq.set_side(sq.get_side() - dim)
#	sq._delay(200)

w.mainloop()