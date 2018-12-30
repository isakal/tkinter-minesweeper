from tkinter import *
from tkinter import messagebox
import webbrowser
from buttons import *


def difficulty1(window, frame):
	rows=10
	columns=10
	resx=25*columns
	resy=25*rows+40
	window.geometry("{}x{}".format(resx,resy))
	buttonsDiff1(frame, rows, columns)


def difficulty2(window, frame):
	rows=10
	columns=15
	resx=25*columns
	resy=25*rows+40
	window.geometry("{}x{}".format(resx,resy))
	#window.geometry("375x290")
	buttonsDiff1(frame, rows, columns)


def difficulty3(window, frame):
	rows=15
	columns=20
	resx=25*columns
	resy=25*rows+40
	window.geometry("{}x{}".format(resx,resy))
	#window.geometry("500x415")
	buttonsDiff1(frame, rows, columns)


def fixGeometry():
	rows=10
	columns=10
	resx=25*columns
	resy=25*rows+40+20


def QuitPrompt(window):
	window.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon="warning")
	if window.quitPrompt.lower() == "yes":
		window.destroy()


def InstructionsInChrome(window):
	webbrowser.open('www.freeminesweeper.org/help/minehelpinstructions.html')


def AboutInChrome(window):
	webbrowser.open('http://www.freeminesweeper.org/help/mineabout.html')

# TODO: add more space above buttons for timer flag check




