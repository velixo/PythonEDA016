import tkinter
import math
import threading
from datetime import datetime

class SimpleWindow:
	mouse_event = 1
	key_event = 2

	def __init__(self, height, width, title = "SimpleWindow"):
		"""Creates a window and makes it visible."""
		self.root = tkinter.Tk()
		self.root.resizable(width=False, height=False)
		self.root.title(title)
		self.canvas = tkinter.Canvas(self.root, width = width, height = height)
		self.canvas.pack()

		self.width = width
		self.height = height
		self.penx = 0
		self.peny = 0
		self.pencol = "#000"
		self.penw = 1

		self.last_event = None
		self.last_key = None
		self.mousex = -1
		self.mousey = -1
		self.freeze = False

		self.delays_list = [0]

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
		print("pencol: " + self.pencol)
		self.canvas.create_line(self.penx, self.peny, x, y, fill=self.pencol, width=self.penw)
		self.penx = x
		self.peny = y

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
		print('new linecol: ' + col)
		self.pencol = col

	def get_line_width(self):
		"""Returns the current line width."""
		return self.penw

	def get_line_color(self):
		"""Returns the current line color."""
		return self.pencol

	def listen_for_mouse_click(self, extra_func = None, *args):
		"""Listens for mouse clicks. """
		if extra_func != None:
			if args != None:
				self.canvas.bind("<Button-1>", lambda event: self.on_mouse_down(event, extra_func, *args))
			else:
				self.canvas.bind("<Button-1>", lambda event: self.on_mouse_down(event, extra_func))
		else:
			self.canvas.bind("<Button-1>", self.on_mouse_down)
		self.canvas.pack()

	def get_mouse_x(self):
		"""Returns the mouse x coordinate at the last mouse click."""
		return self.mousex

	def get_mouse_y(self):
		"""Returns the mouse y coordinate at the last mouse click."""
		return self.mousey

	def wait_for_event(self):
		"""Waits for event (mouse click or key press)."""
		self.canvas.bind("<Button-1>", self.on_mouse_down)
		self.canvas.bind("<Key>", self.read_keyboard)
		self.canvas.pack()

	def get_event_type(self):
		"""Returns the type of the last event."""
		return self.last_event

	def get_key(self):
		"""Returns the key that was pressed on a key event."""
		return self.last_key

	def delay(self, ms):
		"""Waits for a specified time."""
		last = self.delays_list[len(self.delays_list)-1]
		self.delays_list.append(last + ms)




	def on_mouse_down(self, event, extra_func=None, *args):
		self.mousex = event.x
		self.mousey = event.y
		self.last_event = SimpleWindow.mouse_event
		if extra_func != None:
			if args != None:
				extra_func(*args)
			else:
				extra_func()

	def read_keyboard(self, event):
		self.last_key = event.char
		self.last_event = SimpleWindow.key_event

	def mainloop(self):
		self.canvas.mainloop()



class Square:
	def __init__(self, x, y, side):
		"""Creates a suqare with its center in x,y and a given side length."""
		self.x = x
		self.y = y
		self.side = side
		self.alpha = 0

	def get_x(self):
		"""Returns the x-coordinate."""
		return self.x

	def get_y(self):
		"""Returns the y-coordinate."""
		return self.y

	def get_side(self):
		"""Returns the side length."""
		return self.side

	def move(self, dx, dy):
		"""Moves the square relative to its current position."""
		self.x += dx
		self.y += dy

	def set_side(self, side):
		"""Changes the squares side length."""
		self.side = side

	def rotate(self, beta):
		"""Rotates the square counter-clockwise around its center by beta degrees."""
		self.alpha -= beta * math.pi / 180

	def draw(self, w : SimpleWindow):
		"""Draws the square."""
		side = self.side
		exec_time = w.delays_list[len(w.delays_list) - 1]
		w.canvas.after(exec_time, self._draw, w, side)

	def _draw(self, w : SimpleWindow, side=None):
		if side == None:
			side = self.side

		pi4 = math.pi / 4;
		r = side / 2 * math.sqrt(2);
		w.move_to(self.x + round(r * math.cos(self.alpha + pi4)),
				  self.y + round(r * math.sin(self.alpha + pi4)))
		
		w.line_to(self.x + round(r * math.cos(self.alpha + 3 * pi4)),
				  self.y + round(r * math.sin(self.alpha + 3 * pi4)))
		
		w.line_to(self.x + round(r * math.cos(self.alpha + 5 * pi4)),
				  self.y + round(r * math.sin(self.alpha + 5 * pi4)))
		
		w.line_to(self.x + round(r * math.cos(self.alpha + 7 * pi4)),
				  self.y + round(r * math.sin(self.alpha + 7 * pi4)))
		
		w.line_to(self.x + round(r * math.cos(self.alpha + pi4)),
				  self.y + round(r * math.sin(self.alpha + pi4)))

	def erase(self, w : SimpleWindow):
		oldcol = w.get_line_color()
		exec_time = w.delays_list[len(w.delays_list) - 1]
		w.canvas.after(exec_time, self._erase, w)
		w.canvas.after(exec_time, w.set_line_color, oldcol)


	def _erase(self, w : SimpleWindow):
		"""Erases the square. The square must not be moved between drawing and erasing it.
			Erasing is performed by drawing the square with white color, so crossing
			lines will be erased as well."""
		w.set_line_color("#fff")
		self.draw(w)

