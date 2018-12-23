from tkinter import *
from tkinter import messagebox



class GUI:
    def __init__(self, master):
        frame1 =  Frame(master)
        frame1.pack()


        self.printButton = Button(frame1,text ="Print Message",command = self.printMessage)
        self.printButton.pack()

        self.menu = Menu(root)
        root.config(menu=self.menu)
        self.submenu1 = Menu(self.menu)
        self.menu.add_cascade(label="cool kids",menu=self.submenu1)
        self.submenu1.add_command(label="esketit",command=self.doNothing)
        self.submenu1.add_command(label="boi",command=self.boi)
        self.submenu1.add_separator()
        self.submenu1.add_command(label="Quit",command =quit)


        self.quitButton = Button(frame1,text="Quit",command=frame1.quit)
        self.quitButton.pack()

    def printMessage(self):
        self.messageBox = messagebox.showinfo("","Hello!")
    def doNothing(self):
        self.messageBox2 = messagebox.showinfo("","esketit")
    def boi(self):
        self.messageBox3 = messagebox.showinfo("","BOI")




root = Tk()
root.geometry("300x200")
esketit = GUI(root)
root.mainloop()