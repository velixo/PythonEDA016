import tkinter
from datetime import dattime

class SimpleWindow:
	mouse_event = 1
	key_event = 2

	def __init__(self, height, width, title = "SimpleWindow"):
		"""Creates a window and makes it visible."""
		self.root = tkinter.Tk()
		self.root.resizable(width=False, height=False)
		self.root.title(title)
		
		self.canvas = tkinter.Canvas(self.master, width = width, height = height)
		self.canvas.pack()

		self.width = width
		self.height = height
		self.penx = 0
		self.peny = 0
		self.pencol = "#000"
		self.penw = 1

		self.last_event = None
		self.last_key = None

	def get_width():
		"""Returns the width of the window."""
		return self.width

	def get_height():
		"""Returns the height of the window."""
		return self.height

	def clear():
		"""Clears the window."""
		self.canvas.create_rectangle(0, 0, self.width, self.height, fill="#fff")

	def close():
		"""Closes the window."""
		self.root.withdraw()

	def open():
		"""Opens the window."""
		self.root.deiconify()

	def move_to(x, y):
		"""Moves the pen to a new position."""
		self.penx = x
		self.peny = y		

	def line_to(x, y):
		"""Moves the pen to a new position while drawing a line."""
		self.canvas.create_line(self.penx, self.peny, x, y, fill=self.pencol, width=self.penw)

	def write_text(txt):
		"""Writes a string at the current position."""
		self.canvas.create_text(self.penx, self.peny, text=txt, fill=self.pencol)

	def get_x():
		"""Returns the pen's x coordinate."""
		return self.penx

	def get_y():
		"""Returns the pen's y coordinate."""
		return self.peny

	def set_line_width(width):
		"""Sets the line width."""
		self.penw = width

	def set_line_color(col):
		"""Sets the line color."""
		self.pencol = col

	def get_line_width():
		"""Returns the current line width."""
		return self.penw

	def get_line_color():
		"""Returns the current line color."""
		return self.pencol

	def wait_for_mouse_click():
		"""Waits for a mouse click."""
		self.freeze = False
		self.canvas.bind("<Button-1>", read_mouse_pos)
		self.canvas.pack()
		while self.freeze:
			pass

	def get_mouseX():
		"""Returns the mouse x coordinate at the last mouse click."""
		return self.mousex

	def get_mouseY():
		"""Returns the mouse y coordinate at the last mouse click."""
		return self.mousey

	def wait_for_event():
		"""Waits for event (mouse click or key press)."""
		self.canvas.bind("<Button-1>", read_mouse_pos)
		self.canvas.bind("<Key>", read_keyboard)
		self.canvas.pack()
		while self.freeze:
			pass


	def get_event_type():
		"""Returns the type of the last event."""
		return self.last_event


	def get_key():
		"""Returns the key that was pressed on a key event."""
		return self.last_key


	def delay(ms):
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