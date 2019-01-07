from tkinter import *
from tkinter import messagebox
from configparser import *
from functions import *

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))

def newGame(diff, window, frame, framePre):
	global firstClick
	global difficulty
	global gameStarted
	difficulty=diff
	sunken.clear()
	zeroTagged.clear()
	bomb.clear()
	flagged.clear()
	buttonsDict.clear()
	firstClick=True
	if difficulty==4:
		return 0
	difficultySettings(window, frame, difficulty, framePre, True)
	updateFlagButton()
	generateBombs()
	giveButtonsFunction(frame, int(config.get("Difficulty{}".format(str(difficulty)), "rows")),
						int(config.get("Difficulty{}".format(str(difficulty)), "columns")), framePre, window)


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


def giveButtonsFunction(frame, rows, columns, framePre, window):
	for row in range(0, rows):
		for column in range(0, columns):
			buttonsDict[(row, column)].config(command=lambda row=row, column=column: reveal(row, column, difficulty, frame, framePre, window),
											  state=NORMAL)

def generateBombs():
	global bombs
	bombs = int(config.get("Difficulty{}".format(str(difficulty)), "bombs"))
	for i in range(0, bombs):
		randomRow = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "rows")) - 1)
		randomColumn = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "columns")) - 1)
		while buttonsDict[(randomRow, randomColumn)] in bomb:
			randomRow = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "rows")) - 1)
			randomColumn = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "columns")) - 1)
		bomb.append(buttonsDict[(randomRow, randomColumn)])



def reveal(row, column, difficulty, frame, framePre, window):
	global firstClick
	buttonsDict[(row, column)].config(relief=SUNKEN, bg="white", state=DISABLED)
	if buttonsDict[(row, column)] in bomb:
		if firstClick==False:
			gameOver(row, column, frame, framePre, window, difficulty)
			bombImage = PhotoImage(file="bomb.gif")
			buttonsDict[(row, column)].config(image=bombImage, background="red")
			buttonsDict[(row, column)].image = bombImage
		else:
			bomb.remove(buttonsDict[(row, column)])
			randomRow = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "rows")) - 1)
			randomColumn = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "columns")) - 1)
			while buttonsDict[(randomRow, randomColumn)] in bomb or buttonsDict[(randomRow, randomColumn)]==buttonsDict[(row, column)]:
				randomRow = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "rows")) - 1)
				randomColumn = randint(0, int(config.get("Difficulty{}".format(str(difficulty)), "columns")) - 1)
			countBombs(row, column, difficulty)
	else:
		countBombs(row, column, difficulty)
	if len(sunken) == int(config.get("Difficulty{}".format(difficulty),"rows")) * int(config.get("Difficulty{}".format(difficulty),"columns")) - int(config.get("Difficulty{}".format(difficulty),"bombs")):
		epicWinTime(frame, framePre, window, difficulty)
	firstClick=False


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
	if closeBombs > 0 and buttonsDict[(row, column)] not in sunken:
				buttonsDict[(row, column)].config(text=closeBombs)
				sunken.append(buttonsDict[(row, column)])
	if closeBombs == 0:
		sunken.append(buttonsDict[(row, column)])
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
				if buttonsDict[(differenceRow,differenceColumn)] not in zeroTagged and buttonsDict[(differenceRow,differenceColumn)] not in sunken and skip == False:
					zeroTagged.append(buttonsDict[(differenceRow,differenceColumn)])
					buttonsDict[(differenceRow,differenceColumn)].config(relief=SUNKEN, bg="white", state=DISABLED)
					countBombs(differenceRow,differenceColumn,difficulty)


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
	updateFlagButton()


def gameOver(row, column, frame, framePre, window, difficulty):
	bombImage = PhotoImage(file="bomb.gif")
	for button in bomb:
		button.config(image=bombImage, bg="white", relief=SUNKEN)
		button.image = bombImage
	for row in range (0, int(config.get("Difficulty{}".format(str(difficulty)), "rows"))):
		for column in range (0, int(config.get("Difficulty{}".format(str(difficulty)),"columns"))):
			buttonsDict[(row, column)].config(state=DISABLED)
			buttonsDict[(row, column)].bind('<Button-3>',"")
	newStartButton(frame, framePre, window, difficulty)


def epicWinTime(frame, framePre, window, difficulty):
	for row in range (0, int(config.get("Difficulty{}".format(str(difficulty)), "rows"))):
		for column in range (0, int(config.get("Difficulty{}".format(str(difficulty)),"columns"))):
			buttonsDict[(row, column)].config(state=DISABLED)
			buttonsDict[(row, column)].bind('<Button-3>',"")
	messagebox.showinfo("U gae", "You won! #EpicWinTime")
	newStartButton(frame, framePre, window, difficulty)
