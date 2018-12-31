from tkinter import *
from configparser import *

config = ConfigParser()
config.read_file(open(r"config.txt"))
buttonSize = int(config.get("Buttons", "buttonSize"))
buttonsDict = {}
flagged=[]
sunken=[]


def buttonsDiff1(frame, rows, columns):
	buttonsDict.clear()
	for row in range(0, rows):
		for column in range(0, columns):
			gridButton = Button(frame, bg="grey75", command=lambda row=row, column=column: sink(row, column))
			buttonsDict[(row, column)] = gridButton
			buttonsDict[(row, column)].place(height=buttonSize, width=buttonSize, x=column * buttonSize,
											 y=row * buttonSize)
			buttonsDict[(row, column)].bind('<Button-3>',
											lambda event, row=row, column=column: flag(row, column))


def sink(row, column):
	buttonsDict[(row, column)].config(relief=SUNKEN, bg="white", state=DISABLED)
	sunken.append(buttonsDict[(row, column)])


def flag(row, column):
	if buttonsDict[(row, column)] not in sunken:
		if buttonsDict[(row, column)] not in flagged:
			flag=PhotoImage(file="image2.gif")
			buttonsDict[(row, column)].config(image=flag,state=DISABLED)
			buttonsDict[(row, column)].image=flag	
			flagged.append(buttonsDict[(row, column)])

		else:
			buttonsDict[(row, column)].config(image="",state=NORMAL)
			flagged.remove(buttonsDict[(row, column)])