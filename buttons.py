from tkinter import *
mine= PhotoImage(file="mnswpr.ico")


def buttonsDiff1(frame):
	for row in range(0,10):
		for column in range(0,10):
			b = Button(frame)
			buttonSize=25
			b.place(height=buttonSize,width=buttonSize,x=row*buttonSize,y=column*buttonSize)

def buttonsDiff2(frame):
	for row in range(0,15):
		for column in range(0,10):
			b = Button(frame)
			buttonSize=25
			b.place(height=buttonSize,width=buttonSize,x=row*buttonSize,y=column*buttonSize)

def buttonsDiff3(frame):
	for row in range(0,20):
		for column in range(0,15):
			button = Button(frame)
			buttonSize=25
			button.place(height=buttonSize,width=buttonSize,x=row*buttonSize,y=column*buttonSize)