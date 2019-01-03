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
difficulty=1


def difficultyDefault(window, frame):
	import game
	global resx
	global resy

	rows = int(config.get("Default", "rows"))
	columns = int(config.get("Default", "columns"))
	resx = buttonSize * columns
	resy = buttonSize * (rows+1) + buttonFramePadding + 20
	window.geometry(f"{resx}x{resy}")
	game.crateButtonGrid(frame, rows, columns, False, 1)


def difficultySettings(window, frame, diff, isGameStarted):
	global difficulty
	difficulty=diff
	global gameStarted
	gameStarted=isGameStarted
	import game
	global resx
	global resy

	rows = int(config.get("Difficulty{}".format(str(difficulty)), "rows"))
	columns = int(config.get("Difficulty{}".format(str(difficulty)), "columns"))
	resx = buttonSize * columns
	resy = buttonSize * (rows+1) + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	game.crateButtonGrid(frame, rows, columns, isGameStarted, difficulty)


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