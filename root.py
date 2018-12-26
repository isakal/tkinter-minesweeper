from tkinter import *
from tkinter import messagebox
import webbrowser




class GUI:
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()
        root.title("Minesweeper")



        self.printButton = Button(frame1, text="Print Message")
        self.printButton.pack()

        self.menu = Menu(root, tearoff=0)
        root.resizable(FALSE,FALSE)

        master.config(menu=self.menu)
        self.submenu1 = Menu(self.menu,tearoff=0)
        self.submenu2 = Menu(self.menu, tearoff=0)
        self.submenu3 = Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label="Game", menu=self.submenu1)                 #add self.command to tkinter commands
        self.submenu1.add_command(label="New Game")
        self.submenu1.add_separator()
        self.submenu1.add_radiobutton(label="Beginner")
        self.submenu1.add_radiobutton(label="Intermediate")
        self.submenu1.add_radiobutton(label="Expert")
        self.submenu1.add_separator()
        self.submenu1.add_command(label="Quit",command=self.QuitPrompt)

        self.menu.add_cascade(label="Options", menu=self.submenu2)
        self.submenu2.add_checkbutton(label="")


        self.submenu3.add_command(label="Instructions",command=self.InstructionsInChrome)
        self.submenu3.add_separator()
        self.menu.add_cascade(label="Help", menu=self.submenu3)
        self.submenu3.add_command(label="About", command=self.AboutInChrome)

        self.quitButton = Button(frame1, text="Quit", command=self.QuitPrompt)
        self.quitButton.pack()


    def QuitPrompt(self):
        self.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon="warning")
        if self.quitPrompt.lower() == "yes":
            root.destroy()
    def InstructionsInChrome(self):
        webbrowser.open("www.freeminesweeper.org/help/minehelpinstructions.html")
    def AboutInChrome(self):
        webbrowser.open("http://www.freeminesweeper.org/help/mineabout.html")








root = Tk()
root.geometry("300x400+700+300")
minesweeper = GUI(root)
root.mainloop()
