import tkinter
import math
from datetime import datetime

class SimpleWindow:
	mouse_event = 1
	key_event = 2

	def __init__(self, height, width, title = "SimpleWindow"):
		"""Creates a window and makes it visible."""
		self.root = tkinter.Tk()
		self.root.resizable(width=False, height=False)
		self.root.title(title)

		self.width = width
		self.height = height
		self.penx = 0
		self.peny = 0
		self.pencol = "#000"
		self.penw = 1

		self.last_event = None
		self.last_key = None
		
		self.canvas = tkinter.Canvas(self.root, width = width, height = height)
		self.canvas.pack()
		#self.canvas.mainloop()

	def get_width(self):
		"""Returns the width of the window."""
		return self.width

	def get_height(self):
		"""Returns the height of the window."""
		return self.height

	def clear(self):
		"""Clears the window."""
		self.canvas.create_rectangle(0, 0, self.width, self.height, fill="#fff")

	def close(self):
		"""Closes the window."""
		self.root.withdraw()

	def open(self):
		"""Opens the window."""
		self.root.deiconify()

	def move_to(self, x, y):
		"""Moves the pen to a new position."""
		self.penx = x
		self.peny = y		

	def line_to(self, x, y):
		"""Moves the pen to a new position while drawing a line."""
		self.canvas.create_line(self.penx, self.peny, x, y, fill=self.pencol, width=self.penw)

	def write_text(self, txt):
		"""Writes a string at the current position."""
		self.canvas.create_text(self.penx, self.peny, text=txt, fill=self.pencol)

	def get_x(self):
		"""Returns the pen's x coordinate."""
		return self.penx

	def get_y(self):
		"""Returns the pen's y coordinate."""
		return self.peny

	def set_line_width(self, width):
		"""Sets the line width."""
		self.penw = width

	def set_line_color(self, col):
		"""Sets the line color."""
		self.pencol = col

	def get_line_width(self):
		"""Returns the current line width."""
		return self.penw

	def get_line_color(self):
		"""Returns the current line color."""
		return self.pencol

	def wait_for_mouse_click(self):
		"""Waits for a mouse click."""
		self.freeze = False
		self.canvas.bind("<Button-1>", read_mouse_pos)
		self.canvas.pack()
		while self.freeze:
			pass

	def get_mouseX(self):
		"""Returns the mouse x coordinate at the last mouse click."""
		return self.mousex

	def get_mouseY(self):
		"""Returns the mouse y coordinate at the last mouse click."""
		return self.mousey

	def wait_for_event(self):
		"""Waits for event (mouse click or key press)."""
		self.canvas.bind("<Button-1>", read_mouse_pos)
		self.canvas.bind("<Key>", read_keyboard)
		self.canvas.pack()
		while self.freeze:
			pass


	def get_event_type(self):
		"""Returns the type of the last event."""
		return self.last_event


	def get_key(self):
		"""Returns the key that was pressed on a key event."""
		return self.last_key


	def delay(self, ms):
		"""Wait for a specified time."""
		dt = datetime.now()
		startms = dt.day*24*60*60*1000 + dt.hour*60*1000 + dt.second*1000 + dt.microsecond*0.001
		timediff = 0
		while timediff < ms:
			dt = datetime.now()
			currms = dt.day*24*60*60*1000 + dt.hour*60*1000 + dt.second*1000 + dt.microsecond*0.001
			timediff = currms - startms




	def read_mouse_pos(event):
		self.mousex = event.x
		self.mousey = event.y
		self.last_event = SimpleWindow.mouse_event
		self.freeze = False

	def read_keyboard(event):
		self.last_key = event.char
		self.last_event = SimpleWindow.key_event
		self.freeze = False



class Square:
	def __init__(self, x, y, side):
		"""Skapar en kvadrat med medelpunkten i x,y och med en given sidlängd."""
		self.x = x
		self.y = y
		self.side = side
		self.alpha = 0

	def get_x(self):
		"""Tar reda på x-koordinaten."""
		return self.x

	def get_y(self):
		"""Tar reda på y-koordinaten."""
		return self.y

	def get_side(self):
		"""Tar reda på sidlängden."""
		return self.side

	def move(self, dx, dy):
		"""Flyttar kvadraten relativt det aktuella läget."""
		self.x += dx
		self.y += dy

	def set_side(self, side):
		"""Ändrar sidlängden."""
		self.side = side


	def rotate(self, beta):
		"""Roterar kvadraten motsols kring sin medelpunkt."""
		self.alpha = beta


	def draw(self, w : SimpleWindow):
		"""Ritar kvadraten."""
		pi4 = math.pi / 4;
		r = self.side / 2 * math.sqrt(2);
		x0 = self.x + round(r * math.cos(self.alpha + pi4))
		y0 = self.y + round(r * math.sin(self.alpha + pi4))
		x1 = self.x + round(r * math.cos(self.alpha + 3 * pi4))
		y1 = self.y + round(r * math.sin(self.alpha + 3 * pi4))
		x2 = self.x + round(r * math.cos(self.alpha + 5 * pi4))
		y2 = self.y + round(r * math.sin(self.alpha + 5 * pi4))
		x3 = self.x + round(r * math.cos(self.alpha + 7 * pi4))
		y3 = self.y + round(r * math.sin(self.alpha + 7 * pi4))
		x4 = self.x + round(r * math.cos(self.alpha + pi4))
		y4 = self.y + round(r * math.sin(self.alpha + pi4))

		print('(self.x, self.y) = ' + str((self.x, self.y)))
		print('(x0, y0) = ' + str((x0, y0)))
		print('(x1, y1) = ' + str((x1, y1)))
		print('(x2, y2) = ' + str((x2, y2)))
		print('(x3, y3) = ' + str((x3, y3)))
		print('(x4, y4) = ' + str((x4, y4)))

		w.move_to(x0, y0)
		w.line_to(x1, y1)
		w.line_to(x2, y2)
		w.line_to(x3, y3)
		w.line_to(x4, y4)

#		w.move_to(self.x + round(r * math.cos(self.alpha + pi4)),
#				  self.y + round(r * math.sin(self.alpha + pi4)))
		
#		w.line_to(self.x + round(r * math.cos(self.alpha + 3 * pi4)),
#				  self.y + round(r * math.sin(self.alpha + 3 * pi4)))
		
#		w.line_to(self.x + round(r * math.cos(self.alpha + 5 * pi4)),
#				  self.y + round(r * math.sin(self.alpha + 5 * pi4)))
		
#		w.line_to(self.x + round(r * math.cos(self.alpha + 7 * pi4)),
#				  self.y + round(r * math.sin(self.alpha + 7 * pi4)))
		
#		w.line_to(self.x + round(r * math.cos(self.alpha + pi4)),
#				  self.y + round(r * math.sin(self.alpha + pi4)))


	def erase(self, w : SimpleWindow):
		"""Raderar bilden av kvadraten. Kvadraten får inte flyttas mellan uppritning
				och radering. Raderingen görs genom att bilden ritas över med vit färg,
				så även korsande linjer kommer att raderas."""
		oldcol = w.get_line_color
		w.set_line_color("#fff")
		draw(w)
		w.set_line_color(oldcol)

