from tkinter import *
from configparser import *
from functions import *

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))

def newGame(difficulty, window, frame):
	global gameStarted
	if difficulty == 1:
		maxbombs = 10
		difficulty1(window, frame)
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
		difficulty2(window, frame)
		for i in range(0, maxbombs):
			randomRow = randint(0, int(config.get("Buttons", "diff2Rows")) - 1)
			randomColumn = randint(0, int(config.get("Buttons", "diff2Columns")) - 1)
			while buttonsDict[(randomRow, randomColumn)] in bomb:
				randomRow = randint(0, int(config.get("Buttons", "diff2Rows")) - 1)
				randomColumn = randint(0, int(config.get("Buttons", "diff2Columns")) - 1)
			bomb.append(buttonsDict[(randomRow, randomColumn)])
		giveButtonsFunction(frame, int(config.get("Buttons", "diff2Rows")),
							int(config.get("Buttons", "diff2Columns")))

	elif difficulty == 3:
		maxbombs = 27
		difficulty3(window, frame)
		for i in range(0, maxbombs):
			randomRow = randint(0, int(config.get("Buttons", "diff3Rows")) - 1)
			randomColumn = randint(0, int(config.get("Buttons", "diff3Columns")) - 1)
			while buttonsDict[(randomRow, randomColumn)] in bomb:
				randomRow = randint(0, int(config.get("Buttons", "diff3Rows")) - 1)
				randomColumn = randint(0, int(config.get("Buttons", "diff3Columns")) - 1)
			bomb.append(buttonsDict[(randomRow, randomColumn)])
		giveButtonsFunction(frame, int(config.get("Buttons", "diff3Rows")),
							int(config.get("Buttons", "diff3Columns")))

	gameStarted = True


def gridCreate(frame, rows, columns):
	global gameStarted
	print(gameStarted)
	buttonsDict.clear()
	for row in range(0, rows):
		for column in range(0, columns):
			gridButton = Button(frame, bg="grey75", state=DISABLED)
			buttonsDict[(row, column)] = gridButton
			buttonsDict[(row, column)].place(height=buttonSize, width=buttonSize, x=column * buttonSize,
											 y=row * buttonSize)
			buttonsDict[(row, column)].bind('<Button-3>',
											lambda event, row=row, column=column: flag(row, column))


def giveButtonsFunction(frame, rows, columns):
	for row in range(0, rows):
		for column in range(0, columns):
			buttonsDict[(row, column)].config(command=lambda row=row, column=column: sink(row, column),
											  state=NORMAL)


def sink(row, column):
	buttonsDict[(row, column)].config(relief=SUNKEN, bg="white", state=DISABLED)
	sunken.append(buttonsDict[(row, column)])
	if buttonsDict[(row, column)] in bomb:
		bombImage = PhotoImage(file="bomb.gif")
		buttonsDict[(row, column)].config(image=bombImage)
		buttonsDict[(row, column)].image = bombImage


def flag(row, column):
	global gameStarted
	print (gameStarted)
	if gameStarted:
		if buttonsDict[(row, column)] not in sunken:
			if buttonsDict[(row, column)] not in flagged:
				flagImage = PhotoImage(file="flag.gif")
				buttonsDict[(row, column)].config(image=flagImage, state=DISABLED)
				buttonsDict[(row, column)].image = flagImage
				flagged.append(buttonsDict[(row, column)])

			else:
				buttonsDict[(row, column)].config(image="", state=NORMAL)
				flagged.remove(buttonsDict[(row, column)])
