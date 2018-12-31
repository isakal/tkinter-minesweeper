from tkinter import *
from tkinter import messagebox
import webbrowser
from buttons import *
from configparser import *

config = ConfigParser()
config.readfp(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))
buttonFramePadding = int(config.get("Buttons","framePreHeight"))


class settings:
	def __init__(self,master):
		master.title("Minesweeper")
		master.iconbitmap(r'mnswpr.ico')
		master.resizable(FALSE, FALSE)


def defaultDiff(window, frame):
	rows = int(config.get("Buttons", "defaultRows"))
	columns = int(config.get("Buttons", "defaultColumns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonSize + buttonFramePadding - 5
	window.geometry(f"{resx}x{resy}")
	buttonsDiff1(frame, rows, columns)


def difficulty1(window, frame):
	rows = 10
	columns = 10
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	buttonsDiff1(frame, rows, columns)


def difficulty2(window, frame):
	rows = 10
	columns = 15
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	buttonsDiff1(frame, rows, columns)


def difficulty3(window, frame):
	rows = 15
	columns = 20
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	buttonsDiff1(frame, rows, columns)


def QuitPrompt(window):
	window.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon="warning")
	if window.quitPrompt.lower() == "yes":
		window.destroy()


def InstructionsInChrome():
	webbrowser.open('www.freeminesweeper.org/help/minehelpinstructions.html')


def AboutInChrome():
	webbrowser.open('www.freeminesweeper.org/help/mineabout.html')
