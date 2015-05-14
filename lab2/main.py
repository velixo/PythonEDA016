from square import Square
import turtle

w = turtle.Screen()
w.screensize(600, 600, "#fff")
w.title = "DrawSquare"
w.setworldcoordinates(0, 600, 600, 0)

sq = Square(300, 300, 200)
sq.draw(w)

w.mainloop()