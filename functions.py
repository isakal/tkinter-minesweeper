from tkinter import *
from tkinter import messagebox
import webbrowser
from buttons import *
from configparser import *

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))
buttonFramePadding = int(config.get("Buttons","framePreHeight"))

def defaultDiff(window, frame):
	global resx
	global resy
	rows = int(config.get("Buttons", "defaultRows"))
	columns = int(config.get("Buttons", "defaultColumns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding+20
	window.geometry(f"{resx}x{resy}")
	buttonsDiff1(frame, rows, columns)

def getx():
	return resx
def gety():
	return resy

def retryPlace(button):
	button.place(height=25, width=35, x=(resx-35)/2,y=((buttonFramePadding/2)-25)/2+20)

def difficulty1(window, frame):
	global resx
	global resy
	rows = int(config.get("Buttons", "diff1Rows"))
	columns = int(config.get("Buttons", "diff1Columns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	buttonsDiff1(frame, rows, columns)


def difficulty2(window, frame):
	global resx
	global resy
	rows = int(config.get("Buttons", "diff2Rows"))
	columns = int(config.get("Buttons", "diff2Columns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	buttonsDiff1(frame, rows, columns)


def difficulty3(window, frame):
	global resx
	global resy
	rows = int(config.get("Buttons", "diff3Rows"))
	columns = int(config.get("Buttons", "diff3Columns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	buttonsDiff1(frame, rows, columns)


def newGame(difficulty, window, frame):
	if difficulty==1:
		difficulty1(window, frame)
	elif difficulty==2:
		difficulty2(window, frame)
	elif difficulty==3:
		difficulty3(window, frame)


def QuitPrompt(window):
	window.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon="warning")
	if window.quitPrompt.lower() == "yes":
		window.destroy()


def InstructionsInChrome():
	webbrowser.open('www.freeminesweeper.org/help/minehelpinstructions.html')


def AboutInChrome():
	webbrowser.open('www.freeminesweeper.org/help/mineabout.html')
