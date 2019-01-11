from tkinter import *
from tkinter import messagebox
import webbrowser
from configparser import *
from random import *
import time

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))
buttonFramePadding = int(config.get("Buttons", "framePreHeight"))
buttonsDict = {}
flagged = []
sunken = []
bomb = []
zeroTagged = []
gameStarted = False
difficulty=1
firstClick=True
stopwatch = time.time()

def difficultyDefault(window, frame):
	import game
	global resx
	global resy

	rows = int(config.get("Default", "rows"))
	columns = int(config.get("Default", "columns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding + 20
	window.geometry("{}x{}".format(resx, resy))
	game.crateButtonGrid(frame, rows, columns, False, 1)


def difficultySettings(window, frame, diff, framePre, isGameStarted):
	global difficulty
	difficulty=diff
	global gameStarted
	gameStarted=isGameStarted
	import game
	global resx
	global resy
	if gameStarted == False:
		game.newStartButton(frame, framePre, window, difficulty)
	else:
		game.destroyStartButton()
	flagButton.config(text="--")

	if difficulty==4:
		pass

	rows = int(config.get("Difficulty{}".format(str(difficulty)), "rows"))
	columns = int(config.get("Difficulty{}".format(str(difficulty)), "columns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry("{}x{}".format(resx, resy))
	game.crateButtonGrid(frame, rows, columns, isGameStarted, difficulty)


def QuitPrompt(window):
	window.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon="warning")
	if window.quitPrompt.lower() == "yes":
		window.destroy()


def InstructionsInChrome():
	webbrowser.open('www.freeminesweeper.org/help/minehelpinstructions.html')


def AboutInChrome():
	webbrowser.open('www.freeminesweeper.org/help/mineabout.html')


def Credits(window, frame, button):
	button.destroy()
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

def destroyStartButton():
	global startButton
	try:
		startButton.destroy()
	except:
		pass

def newStartButton(frame, framePre, window, difficulty):
	import game
	global startButton
	try:
		startButton.destroy()
	except:
		pass
	startButton = Button(framePre,text="Start New Game",command=lambda:[game.newGame(difficulty, window, frame, framePre), startButton.destroy()])
	startButton.place(relx=0.5, rely=0.5, anchor=CENTER)
	return startButton

def newFlagButton(framePre):
	global flagButton
	flagButton = Button(framePre, text="--", state=DISABLED, relief=SUNKEN)
	flagButton.place(width=25, height=25, relx=0.05, rely=0.5, anchor=W)
	return flagButton


def updateFlagButton():
	if gameStarted==True:
		remaining=int(config.get("Difficulty{}".format(difficulty), "maxFlags")) - len(flagged)
		flagButton.config(text=remaining)


def SakiGithub():
	webbrowser.open("https://github.com/isakal")


def SpinGithub():
	webbrowser.open("https://github.com/Spinzed")


def startTimer():
	global stopwatch
	stopwatch = time.time()
	

def stopTimer():
	global stopwatch
	stopwatch = time.time() - stopwatch


def getTimer():
	global stopwatch
	stopwatch = time.time() - stopwatch
	return stopwatch


def printTimer():
	global stopwatch
	print("Time taken: {0:.3} seconds".format(stopwatch), flush=True)
