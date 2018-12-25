from tkinter import *
from tkinter import messagebox



class GUI:
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()
        root.title("Minesweeper")


        self.printButton = Button(frame1, text="Print Message", command=self.printMessage)
        self.printButton.pack()

        self.menu = Menu(root, tearoff=0)

        master.config(menu=self.menu)
        self.submenu1 = Menu(self.menu,tearoff=0)
        self.submenu2 = Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label="cool kids", menu=self.submenu1)
        self.submenu1.add_command(label="esketit", command=self.esketit)
        self.submenu1.add_command(label="boi", command=self.boi)
        self.submenu1.add_separator()
        self.submenu1.add_command(label="Quit", command=quit)
        self.submenu2.add_command(label="gay", command=self.gay)
        self.menu.add_cascade(label="gay", menu=self.submenu2)

        self.quitButton = Button(frame1, text="Quit", command=root.quit)
        self.quitButton.pack()

    def printMessage(self):
        self.messageBox = messagebox.showinfo("", "Hello!")
    def esketit(self):
        self.messageBox2 = messagebox.showinfo("", "esketit")
    def boi(self):
        self.messageBox3 = messagebox.showinfo("", "BOI")
    def gay(self):
        self.messageBox4 = messagebox.showinfo("", "GAY")




root = Tk()
root.geometry("300x400+1000+300")
mainwindow = GUI(root)
root.mainloop()
