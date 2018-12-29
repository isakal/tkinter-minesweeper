from tkinter import *
from tkinter import messagebox
import webbrowser
from buttons import *

def difficulty1(window, frame):
    window.geometry("250x290")
    buttonsDiff1(frame)

def difficulty2(window, frame):
    window.geometry("375x290")
    buttonsDiff2(frame)

def difficulty3(window, frame):
    window.geometry("500x415")
    buttonsDiff3(frame)

def QuitPrompt(window):
    window.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon="warning")
    if window.quitPrompt.lower() == "yes":
        window.destroy()

def InstructionsInChrome(window):
    webbrowser.open('www.freeminesweeper.org/help/minehelpinstructions.html')

def AboutInChrome(window):
    webbrowser.open('http://www.freeminesweeper.org/help/mineabout.html')