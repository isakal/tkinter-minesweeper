from tkinter import *
from tkinter import messagebox
import webbrowser

def difficulty1(window):
    window.geometry("250x310")

def difficulty2(window):
    window.geometry("600x300")

def difficulty3(window):
    window.geometry("1000x800")

def QuitPrompt(window):
    window.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon="warning")
    if window.quitPrompt.lower() == "yes":
        window.destroy()

def InstructionsInChrome(window):
    webbrowser.open('www.freeminesweeper.org/help/minehelpinstructions.html')

def AboutInChrome(window):
    webbrowser.open('http://www.freeminesweeper.org/help/mineabout.html')