import fix_imports	# enables importing of modules in 'PythonEDA016'
from cs_eda016.prebuilts import *

w = SimpleWindow(600, 600, 'DrawSquare')
sq1 = Square(300, 300, 200)
sq2 = Square(300, 300, 200)
sq3 = Square(300, 300, 200)
sq1.rotate(0)
sq2.rotate(30)
sq3.rotate(60)
sq1.draw(w)
sq2.draw(w)
sq3.draw(w)

# keep the window open. should be fixed, needing to do this outside 
# of the class itself is ugly
w.mainloop()