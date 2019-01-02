from tkinter import *
from configparser import *
from functions import *

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))
difficulty=1

def newGame(diff, window, frame):
	global difficulty
	difficulty=diff
	global gameStarted
	if difficulty == 1:
		maxbombs = 10
		difficulty1(window, frame, True)
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
		difficulty2(window, frame, True)
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
		difficulty3(window, frame, True)
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


def crateButtonGrid(frame, rows, columns, isGameStarted, difficulty):
	buttonsDict.clear()
	flagged.clear()
	for row in range(0, rows):
		for column in range(0, columns):
			gridButton = Button(frame, bg="grey75", state=DISABLED)
			buttonsDict[(row, column)] = gridButton
			buttonsDict[(row, column)].place(height=buttonSize, width=buttonSize, x=column * buttonSize,
											 y=row * buttonSize)
			buttonsDict[(row, column)].bind('<Button-3>',
											lambda event, row=row, column=column, gameStarted=isGameStarted: flag(row, column, isGameStarted, difficulty))


def giveButtonsFunction(frame, rows, columns):
	for row in range(0, rows):
		for column in range(0, columns):
			buttonsDict[(row, column)].config(command=lambda row=row, column=column: reveal(row, column),
											  state=NORMAL)


def reveal(row, column):
	closeBombs=0
	buttonsDict[(row, column)].config(relief=SUNKEN, bg="white", state=DISABLED)
	sunken.append(buttonsDict[(row, column)])
	if buttonsDict[(row, column)] in bomb:
		bombImage = PhotoImage(file="bomb.gif")
		buttonsDict[(row, column)].config(image=bombImage)
		buttonsDict[(row, column)].image = bombImage
	else:
		for relativeRow in range(0,3):
			for relativeColumn in range(0,3):
				decoyRow=relativeRow
				decoyColumn=relativeColumn
				if decoyRow < 0:
					decoyRow = 0
				if decoyColumn < 0:
					decoyColumn = 0
				if buttonsDict[(row-1+decoyRow, column-1+decoyColumn)] in bomb:
					closeBombs+=1
		if closeBombs>0:
			buttonsDict[(row, column)].config(text=closeBombs)



def flag(row, column, isGameStarted, difficulty):
	if isGameStarted:
		if buttonsDict[(row, column)] not in flagged:
			if isGameStarted==True and buttonsDict[(row, column)] not in sunken:
				if difficulty==1 and len(flagged) < int(config.get("Buttons", "diff1MaxFlags")):
					flagImage = PhotoImage(file="flag.gif")
					buttonsDict[(row, column)].config(image=flagImage, state=DISABLED)
					buttonsDict[(row, column)].image = flagImage
					flagged.append(buttonsDict[(row, column)])
				if difficulty==2 and len(flagged) < int(config.get("Buttons", "diff2MaxFlags")):
					flagImage = PhotoImage(file="flag.gif")
					buttonsDict[(row, column)].config(image=flagImage, state=DISABLED)
					buttonsDict[(row, column)].image = flagImage
					flagged.append(buttonsDict[(row, column)])
				if difficulty==3 and len(flagged) < int(config.get("Buttons", "diff3MaxFlags")):
					flagImage = PhotoImage(file="flag.gif")
					buttonsDict[(row, column)].config(image=flagImage, state=DISABLED)
					buttonsDict[(row, column)].image = flagImage
					flagged.append(buttonsDict[(row, column)])
		else:
			buttonsDict[(row, column)].config(image="", state=NORMAL)
			flagged.remove(buttonsDict[(row, column)])
	