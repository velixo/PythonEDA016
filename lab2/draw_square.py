import fix_imports	# enables importing of modules in 'PythonEDA016'
from cs_eda016.prebuilts import *

print('Creating SimpleWindow...')
w = SimpleWindow(600, 600, 'DrawSquare')
print('Creating Square...')
sq1 = Square(0, 0, 200)
sq2 = Square(300, 300, 200)
print('Drawing square...')
sq1.draw(w)
sq2.draw(w)

# keep the window open. should be fixed, needing to do this outside 
# of the class itself is ugly
w.canvas.mainloop()