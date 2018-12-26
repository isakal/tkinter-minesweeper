from tkinter import *
from tkinter import messagebox
import webbrowser



class GUI:
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()
        root.title("Minesweeper")


        self.printButton = Button(frame1, text="Print Message", command=self.PrintMessage)
        self.printButton.pack()

        self.menu = Menu(root, tearoff=0)

        master.config(menu=self.menu)
        self.submenu1 = Menu(self.menu,tearoff=0)
        self.submenu2 = Menu(self.menu, tearoff=0)
        self.submenu3 = Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label="Game", menu=self.submenu1)
        self.submenu1.add_command(label="esketit", command=self.Esketit)
        self.submenu1.add_command(label="boi", command=self.Boi)
        self.submenu1.add_separator()
        self.submenu1.add_command(label="Quit", command=self.QuitPrompt)

        self.menu.add_cascade(label="Options")

        self.submenu3.add_command(label="Instructions",command=self.InstructionsInChrome)
        self.submenu3.add_separator()
        self.menu.add_cascade(label="Help", menu=self.submenu3)
        self.submenu3.add_command(label="About", command=self.AboutInChrome)

        self.quitButton = Button(frame1, text="Quit", command=self.QuitPrompt)
        self.quitButton.pack()

    def PrintMessage(self):
        self.messageBox = messagebox.showinfo("", "Hello!")
    def Esketit(self):
        self.messageBox2 = messagebox.showinfo("", "esketit")
    def Boi(self):
        self.messageBox3 = messagebox.showinfo("", "BOI")
    def QuitPrompt(self):
        self.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon='warning')
        if self.quitPrompt.lower() == "yes":
            root.destroy()
    def InstructionsInChrome(self):
        webbrowser.open("www.freeminesweeper.org/help/minehelpinstructions.html")
    def AboutInChrome(self):
        webbrowser.open("http://www.freeminesweeper.org/help/mineabout.html")








root = Tk()
root.geometry("300x400+1000+300")
mainwindow = GUI(root)
root.mainloop()
