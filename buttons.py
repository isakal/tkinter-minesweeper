from tkinter import *

buttonSize = 25
buttonsDict = {}


def buttonsDiff1(frame):
	global gridButton
	buttonsDict.clear()
	for row in range(0, 10):
		for column in range(0, 10):
			gridButton = Button(frame, relief=RAISED, bg="grey", command=lambda r=row, c=column: CollapseButton(r, c))
			buttonsDict[(row, column)] = gridButton
			buttonsDict[(row, column)].place(height=buttonSize, width=buttonSize, x=row * buttonSize,
											 y=column * buttonSize)


def buttonsDiff2(frame):
	global gridButton
	buttonsDict.clear()
	for row in range(0, 15):
		for column in range(0, 10):
			gridButton = Button(frame, relief=RAISED, bg="grey", command=lambda r=row, c=column: CollapseButton(r, c))
			buttonsDict[(row, column)] = gridButton
			buttonsDict[(row, column)].place(height=buttonSize, width=buttonSize, x=row * buttonSize,
											 y=column * buttonSize)


def buttonsDiff3(frame):
	global gridButton
	buttonsDict.clear()
	for row in range(0, 20):
		for column in range(0, 15):
			gridButton = Button(frame, relief=RAISED, bg="grey", command=lambda r=row, c=column: CollapseButton(r, c))
			buttonsDict[(row, column)] = gridButton
			buttonsDict[(row, column)].place(height=buttonSize, width=buttonSize, x=row * buttonSize,
											 y=column * buttonSize)


def CollapseButton(row, column):
	buttonsDict[(row, column)].config(relief=SUNKEN, bg="grey90")
