import fix_imports
from cs_eda016.prebuilts import *

dim = int(input("Skriv förminskning: "))
w = SimpleWindow(600, 600, "DrawManySquares")
sq = Square(300, 300, 200)
while sq.get_side() > 0:
	sq.draw(w);
	w.delay(200) # w doesnt show until mainloop() so this just slows the opening of the window
	sq.set_side(sq.get_side() - dim);

w.mainloop()