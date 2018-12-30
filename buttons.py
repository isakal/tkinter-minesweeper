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


def buttonsDiff2(frame):
	buttonsDict.clear()
	for row in range(0, 15):
		for column in range(0, 10):
			gridButton = Button(frame, bg="grey75", command=lambda row=row, column=column: sink(row, column))
			buttonsDict[(row, column)] = gridButton
			buttonsDict[(row, column)].place(height=buttonSize, width=buttonSize, x=row * buttonSize,
											 y=column * buttonSize)


def buttonsDiff3(frame):
	buttonsDict.clear()
	for row in range(0, 20):
		for column in range(0, 15):
			gridButton = Button(frame, bg="grey75", command=lambda row=row, column=column: sink(row, column))
			buttonsDict[(row, column)] = gridButton
			buttonsDict[(row, column)].place(height=buttonSize, width=buttonSize, x=row * buttonSize,
											 y=column * buttonSize)


def sink(row, column):
	buttonsDict[(row, column)].config(relief=SUNKEN, bg="white")
