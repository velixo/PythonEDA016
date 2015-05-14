import turtle

class Square:
	def __init__(self, x, y, side):
		self.x = x
		self.y = y
		self.side = side
		self.rotation = 0

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_side(self):
		return self.side

	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def set_side(self, side):
		self.side = side

	def rotate(self, rotation):
		self.rotation = rotation

	def draw(self, screen : turtle.TurtleScreen):
		ttl = turtle.RawTurtle(screen)
		ttl.penup()
		ttl.hideturtle()
		ttl.speed(10)
		ttl.setpos(self.x, self.y)
		ttl.pendown()

		ttl.setpos(self.x + self.side, self.y)
		ttl.setpos(self.x + self.side, self.y + self.side)
		ttl.setpos(self.x, self.y + self.side)
		ttl.setpos(self.x, self.y)

	def erase(self, screen : turtle.TurtleScreen):
		ttl = turtle.RawTurtle(screen)
		ttl.clear()
		