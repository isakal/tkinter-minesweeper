from tkinter import *

buttonSize = 25
buttonsDict = {}


def buttonsDiff1(frame):
	global gridButton
	buttonsDict.clear()
	for row in range(0, 10):
		for column in range(0, 10):
			gridButton = Button(frame, relief=RAISED,command=CollapseButton)
			buttonsDict["field {}{}".format(row, column)] = gridButton
			buttonsDict["field {}{}".format(row, column)].place(height=buttonSize, width=buttonSize, x=row * buttonSize,
								 							   y=column * buttonSize)




def buttonsDiff2(frame):
	global gridButton
	buttonsDict.clear()
	for row in range(0, 15):
		for column in range(0, 10):
			gridButton = Button(frame, relief=RAISED,command=CollapseButton)
			buttonsDict["field {}{}".format(row, column)] = gridButton
			buttonsDict["field {}{}".format(row, column)].place(height=buttonSize, width=buttonSize, x=row * buttonSize,
															   y=column * buttonSize)


def buttonsDiff3(frame):
	global gridButton
	buttonsDict.clear()
	for row in range(0, 20):
		for column in range(0, 15):
			gridButton = Button(frame, relief=RAISED,command=CollapseButton)
			buttonsDict["field {}{}".format(row, column)] = gridButton
			buttonsDict["field {}{}".format(row, column)].place(height=buttonSize, width=buttonSize, x=row * buttonSize,
															   y=column * buttonSize)
def CollapseButton():
	gridButton.config(relief=SUNKEN)