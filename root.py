from tkinter import *
from tkinter import messagebox



class GUI:
    def __init__(self, master):
        frame1 =  Frame(master)
        frame1.pack()


        self.printButton = Button(frame1,text ="Print Message",command = self.printMessage)
        self.printButton.pack()

        self.quitButton = Button(frame1,text="Quit",command=frame1.quit)
        self.quitButton.pack()

    def printMessage(self):
        self.messageBox = messagebox.showinfo("","Hello!")




root = Tk()
root.geometry("100x80")
esketit = GUI(root)
root.mainloop()