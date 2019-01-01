from tkinter import *
from configparser import *

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))
buttonsDict = {}
flagged = []
sunken = []
bomb = []
gameStarted = False


def gridCreate(frame, rows, columns):
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
	if buttonsDict[(row, column)] not in sunken:
		if buttonsDict[(row, column)] not in flagged:
			flagImage = PhotoImage(file="flag.gif")
			buttonsDict[(row, column)].config(image=flagImage, state=DISABLED)
			buttonsDict[(row, column)].image = flagImage
			flagged.append(buttonsDict[(row, column)])

		else:
			buttonsDict[(row, column)].config(image="", state=NORMAL)
			flagged.remove(buttonsDict[(row, column)])
