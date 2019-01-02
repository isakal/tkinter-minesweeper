from tkinter import *
from tkinter import messagebox
import webbrowser
from configparser import *
from random import *

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))
buttonFramePadding = int(config.get("Buttons", "framePreHeight"))
buttonsDict = {}
flagged = []
sunken = []
bomb = []
gameStarted = False


def difficultyDefault(window, frame):
	import game
	global resx
	global resy

	rows = int(config.get("Buttons", "defaultRows"))
	columns = int(config.get("Buttons", "defaultColumns"))
	resx = buttonSize * columns
	resy = buttonSize * (rows+1) + buttonFramePadding + 20
	window.geometry(f"{resx}x{resy}")
	game.crateButtonGrid(frame, rows, columns, False, 1)


def getx():
	return resx


def gety():
	return resy


def difficulty1(window, frame, isGameStarted):
	global gameStarted
	gameStarted=isGameStarted
	import game
	global resx
	global resy

	rows = int(config.get("Buttons", "diff1Rows"))
	columns = int(config.get("Buttons", "diff1Columns"))
	resx = buttonSize * columns
	resy = buttonSize * (rows+1) + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	game.crateButtonGrid(frame, rows, columns, isGameStarted, 1)


def difficulty2(window, frame, isGameStarted):
	global gameStarted
	gameStarted=False
	import game
	global resx
	global resy

	rows = int(config.get("Buttons", "diff2Rows"))
	columns = int(config.get("Buttons", "diff2Columns"))
	resx = buttonSize * columns
	resy = buttonSize * (rows+1) + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	game.crateButtonGrid(frame, rows, columns, isGameStarted, 2)


def difficulty3(window, frame, isGameStarted):
	global gameStarted
	gameStarted=False
	import game
	global resx
	global resy

	rows = int(config.get("Buttons", "diff3Rows"))
	columns = int(config.get("Buttons", "diff3Columns"))
	resx = buttonSize * columns
	resy = buttonSize * (rows+1) + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	game.crateButtonGrid(frame, rows, columns, isGameStarted, 3)

#TODO: Merge upper 3 functions into one 


def QuitPrompt(window):
	window.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon="warning")
	if window.quitPrompt.lower() == "yes":
		window.destroy()


def InstructionsInChrome():
	webbrowser.open('www.freeminesweeper.org/help/minehelpinstructions.html')


def AboutInChrome():
	webbrowser.open('www.freeminesweeper.org/help/mineabout.html')


def Credits(window, frame):
	creditsLabel1 = Label(frame, background="grey80",
						  text="Minesweeper {}".format(str(config.get("Buttons", "version"))))
	creditsLabel1.place(x=0, y=0)
	creditsLabel2 = Label(frame, background="grey80", text="")
	creditsLabel2.place(x=0, y=20)
	creditsLabel3 = Label(frame, background="grey80", text="Contributors:")
	creditsLabel3.place(x=0, y=40)
	creditsLabel4 = Label(frame, background="grey80", text="Ivan Sakal aka Saki")
	creditsLabel4.place(x=0, y=60)
	creditsButton1 = Button(frame, background="grey80", text="GitHub", command=SakiGithub, relief=FLAT)
	creditsButton1.place(x=160, y=58)
	creditsLabel5 = Label(frame, background="grey80", text="Davor Najev aka Spinzed")
	creditsLabel5.place(x=0, y=80)
	creditsButton1 = Button(frame, background="grey80", text="GitHub", command=SpinGithub, relief=FLAT)
	creditsButton1.place(x=160, y=78)


def SakiGithub():
	webbrowser.open("https://github.com/isakal")


def SpinGithub():
	webbrowser.open("https://github.com/Spinzed")
