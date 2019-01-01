from tkinter import *
from tkinter import messagebox
import webbrowser
from buttons import *
from configparser import *
from random import *

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))
buttonFramePadding = int(config.get("Buttons", "framePreHeight"))


def defaultDiff(window, frame):
	global resx
	global resy

	rows = int(config.get("Buttons", "defaultRows"))
	columns = int(config.get("Buttons", "defaultColumns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding + 20
	window.geometry(f"{resx}x{resy}")
	gridCreate(frame, rows, columns, False)


def getx():
	return resx


def gety():
	return resy


def difficulty1(window, frame, isGameStarted):
	global resx
	global resy

	rows = int(config.get("Buttons", "diff1Rows"))
	columns = int(config.get("Buttons", "diff1Columns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	gridCreate(frame, rows, columns, isGameStarted)


def difficulty2(window, frame, isGameStarted):
	global resx
	global resy

	rows = int(config.get("Buttons", "diff2Rows"))
	columns = int(config.get("Buttons", "diff2Columns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	gridCreate(frame, rows, columns, isGameStarted)


def difficulty3(window, frame, isGameStarted):
	global resx
	global resy

	rows = int(config.get("Buttons", "diff3Rows"))
	columns = int(config.get("Buttons", "diff3Columns"))
	resx = buttonSize * columns
	resy = buttonSize * rows + buttonFramePadding
	window.geometry(f"{resx}x{resy}")
	gridCreate(frame, rows, columns, isGameStarted)


def newGame(difficulty, window, frame):
	global gameStarted
	gameStarted = True
	if difficulty == 1:
		maxbombs = 10
		difficulty1(window, frame, gameStarted)
		for i in range(0, maxbombs):
			randomRow = randint(0, int(config.get("Buttons", "diff1Rows")) - 1)
			randomColumn = randint(0, int(config.get("Buttons", "diff1Columns")) - 1)
			while buttonsDict[(randomRow, randomColumn)] in bomb:
				randomRow = randint(0, int(config.get("Buttons", "diff1Rows")) - 1)
				randomColumn = randint(0, int(config.get("Buttons", "diff1Columns")) - 1)
			bomb.append(buttonsDict[(randomRow, randomColumn)])
		giveButtonsFunction(frame, int(config.get("Buttons", "diff1Rows")),
							int(config.get("Buttons", "diff1Columns")))

	elif difficulty == 2:
		maxbombs = 17
		difficulty2(window, frame, gameStarted)
		for i in range(0, maxbombs):
			randomRow = randint(0, int(config.get("Buttons", "diff1Rows")) - 1)
			randomColumn = randint(0, int(config.get("Buttons", "diff1Columns")) - 1)
			while buttonsDict[(randomRow, randomColumn)] in bomb:
				randomRow = randint(0, int(config.get("Buttons", "diff1Rows")) - 1)
				randomColumn = randint(0, int(config.get("Buttons", "diff1Columns")) - 1)
			bomb.append(buttonsDict[(randomRow, randomColumn)])
		giveButtonsFunction(frame, int(config.get("Buttons", "diff2Rows")),
							int(config.get("Buttons", "diff2Columns")))

	elif difficulty == 3:
		maxbombs = 27
		difficulty3(window, frame, gameStarted)
		for i in range(0, maxbombs):
			randomRow = randint(0, int(config.get("Buttons", "diff1Rows")) - 1)
			randomColumn = randint(0, int(config.get("Buttons", "diff1Columns")) - 1)
			while buttonsDict[(randomRow, randomColumn)] in bomb:
				randomRow = randint(0, int(config.get("Buttons", "diff1Rows")) - 1)
				randomColumn = randint(0, int(config.get("Buttons", "diff1Columns")) - 1)
			bomb.append(buttonsDict[(randomRow, randomColumn)])
		giveButtonsFunction(frame, int(config.get("Buttons", "diff3Rows")),
							int(config.get("Buttons", "diff3Columns")))


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
