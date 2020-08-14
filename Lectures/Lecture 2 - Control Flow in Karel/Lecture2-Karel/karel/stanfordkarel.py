import sys
import os
import tkinter as tk
from karel.KarelApplication import KarelApplication
from karel.KarelWorld import KarelWorld
from karel.Karel import Karel
from karel.kareldefinitions import DEFAULT_WORLD_FILE


def move():
	pass


def turn_left():
	pass


def put_beeper():
	pass


def pick_beeper():
	pass


def front_is_clear():
	pass


def front_is_blocked():
	pass


def left_is_clear():
	pass


def left_is_blocked():
	pass


def right_is_clear():
	pass


def right_is_blocked():
	pass


def on_beeper():
	pass


def beepers_in_bag():
	pass


def facing_north():
	pass


def facing_east():
	pass


def facing_west():
	pass


def facing_south():
	pass


def paint_corner():
	pass


def corner_color_is():
	pass


# Defined constants for ease of use by students when coloring corners
RED = "red"
BLACK = "black"
CYAN = "cyan"
DARK_GRAY = "gray30"
GRAY = "gray55"
GREEN = "green"
LIGHT_GRAY = "gray80"
MAGENTA = "magenta3"
ORANGE = "orange"
PINK = "pink"
WHITE = "snow"
BLUE = "blue"
YELLOW = "yellow"

def run_karel_program(world_file=None):
	# Extract the name of the file the student is executing
	student_code_file = sys.argv[0]

	if not world_file:
		# Find world file that matches program name
		base_filename = os.path.basename(student_code_file)
		module_name = os.path.splitext(base_filename)[0]
		karel_world_file = f"worlds/{module_name}.w"
		if os.path.exists(karel_world_file):
			world_file = karel_world_file
		else:
			print(f"Could not find a world matching filename {module_name}.w, defaulting to default world.")
			default_world_file = f"worlds/{DEFAULT_WORLD_FILE}"
			if os.path.exists(default_world_file):
				world_file = default_world_file
			else:
				print("Could not find a default world to use, please specify a world filename.")
				return

	# Create the world as specified in the given world file
	try:
		# Attempt to open the file that has been specified
		world_file = open(world_file, "r")
	except OSError:
		try:
			# Before failing, look inside the worlds folder for this file
			world_file = open(os.path.join("worlds", world_file))
		except OSError:
			# Print warning to user and exit out of the program
			print(f"Could not find world file with name: {world_file}")
			return

	world = KarelWorld(world_file)

	# Create Karel and assign it to live in the newly created world
	karel = Karel(world)

	# Initialize root Tk Window and spawn Karel application
	root = tk.Tk()
	app = KarelApplication(karel, world, student_code_file, master=root)
	app.mainloop()
