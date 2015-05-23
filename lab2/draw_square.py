import fix_imports	# enables importing of modules in 'PythonEDA016'
from cs_eda016.prebuilts import *

w = SimpleWindow(600, 600, 'DrawSquare')
sq = Square(300, 300, 200)
sq.draw(w)

# keep the window open. should be fixed, needing to do this outside 
# of the class itself is ugly
w.canvas.mainloop()