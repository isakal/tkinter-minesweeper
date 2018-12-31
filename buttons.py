from tkinter import *
from configparser import *

config = ConfigParser()
config.readfp(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))
buttonsDict = {}


def buttonsDiff1(frame, rows, columns):
	buttonsDict.clear()
	print(rows, columns)
	for row in range(0, rows):
		for column in range(0, columns):
			gridButton = Button(frame, bg="grey75", command=lambda row=row, column=column: sink(row, column))
			buttonsDict[(row, column)] = gridButton
			buttonsDict[(row, column)].place(height=buttonSize, width=buttonSize, x=column * buttonSize,
											 y=row * buttonSize)


def sink(row, column):
	buttonsDict[(row, column)].config(relief=SUNKEN, bg="white",state=DISABLED)
