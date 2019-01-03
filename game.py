from tkinter import *
from configparser import *
from functions import *

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))

def newGame(diff, window, frame):
	global difficulty
	global gameStarted
	difficulty=diff
	bombs = int(config.get("Difficulty{}".format(str(difficulty)), "bombs"))
	difficultySettings(window, frame, difficulty, True)
	for i in range(0, bombs):
		randomRow = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "rows")) - 1)
		randomColumn = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "columns")) - 1)
		while buttonsDict[(randomRow, randomColumn)] in bomb:
			randomRow = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "rows")) - 1)
			randomColumn = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "columns")) - 1)
		bomb.append(buttonsDict[(randomRow, randomColumn)])
	giveButtonsFunction(frame, int(config.get("Difficulty{}".format(str(difficulty)), "rows")),
						int(config.get("Difficulty{}".format(str(difficulty)), "columns")))
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
			buttonsDict[(row, column)].config(command=lambda row=row, column=column: reveal(row, column, difficulty),
											  state=NORMAL)


def reveal(row, column, difficulty):
	buttonsDict[(row, column)].config(relief=SUNKEN, bg="white", state=DISABLED)
	sunken.append(buttonsDict[(row, column)])
	if buttonsDict[(row, column)] in bomb:
		revealAllBombs()
		bombImage = PhotoImage(file="bomb.gif")
		buttonsDict[(row, column)].config(image=bombImage)
		buttonsDict[(row, column)].image = bombImage
	else:
		countBombs(row, column, difficulty)


def countBombs(row, column, difficulty):
	closeBombs=0
	for relativeRow in range(0,3):
		for relativeColumn in range(0,3):
			skip=False
			differenceRow=row-relativeRow+1
			differenceColumn=column-relativeColumn+1
			if differenceRow < 0:
				differenceRow = 0
				skip=True
			if differenceColumn < 0:
				differenceColumn = 0
				skip=True
			if differenceRow == int(config.get("Difficulty{}".format(str(difficulty)), "rows")):
				differenceRow-=1
				skip=True
			if differenceColumn == int(config.get("Difficulty{}".format(str(difficulty)), "columns")):
				differenceColumn-=1
				skip=True			
			if buttonsDict[(differenceRow, differenceColumn)] in bomb and skip==False:
				closeBombs+=1
			if closeBombs>0:
				buttonsDict[(row, column)].config(text=closeBombs)
	if closeBombs == 0:
		for zeroRow in range(0,3):
			for zeroColumn in range(0,3):
				skip=False
				differenceRow=row-zeroRow+1
				differenceColumn=column-zeroColumn+1
				if differenceRow < 0:
					differenceRow = 0
					skip=True
				if differenceColumn < 0:
					differenceColumn = 0
					skip=True
				if differenceRow == int(config.get("Difficulty{}".format(str(difficulty)), "rows")):
					differenceRow-=1
					skip=True
				if differenceColumn == int(config.get("Difficulty{}".format(str(difficulty)), "columns")):
					differenceColumn-=1
					skip=True
				if buttonsDict[(differenceRow,differenceColumn)] not in zeroTagged and skip == False:
					zeroTagged.append(buttonsDict[(differenceRow,differenceColumn)])
					buttonsDict[(differenceRow,differenceColumn)].config(relief=SUNKEN, bg="white", state=DISABLED)
					countBombs(differenceRow,differenceColumn,difficulty)


def revealAllBombs():
	bombImage = PhotoImage(file="bomb.gif")
	for button in bomb:
		button.config(image=bombImage, bg="white", relief=SUNKEN)
		button.image = bombImage
	for row in range (0, int(config.get("Difficulty{}".format(str(difficulty)), "rows"))):
		for column in range (0, int(config.get("Difficulty{}".format(str(difficulty)),"columns"))):
			buttonsDict[(row,column)].config(state=DISABLED)


def flag(row, column, isGameStarted, difficulty):
	if isGameStarted:
		if buttonsDict[(row, column)] not in flagged:
			if isGameStarted==True and buttonsDict[(row, column)] not in sunken:
				if len(flagged) < int(config.get("Difficulty{}".format(str(difficulty)), "maxFlags")):
					flagImage = PhotoImage(file="flag.gif")
					buttonsDict[(row, column)].config(image=flagImage, state=DISABLED)
					buttonsDict[(row, column)].image = flagImage
					flagged.append(buttonsDict[(row, column)])
		else:
			buttonsDict[(row, column)].config(image="", state=NORMAL)
			flagged.remove(buttonsDict[(row, column)])
	