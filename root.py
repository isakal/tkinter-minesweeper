from tkinter import *
from buttons import *
from functions import *


class GUI:
	def __init__(self, master):
		global buttonFrame
		self.master = master
		frame_pre = Frame(master, background="grey17")
		frame_pre.pack(fill=X, ipady=20)
		buttonFrame = Frame(master, background="grey17")
		buttonFrame.pack(fill='both', expand=True)
		master.title("Minesweeper")
		master.iconbitmap(r'mnswpr.ico')
		master.resizable(FALSE, FALSE)

		self.menu = Menu(master, tearoff=0)
		self.variable = IntVar()

		master.config(menu=self.menu)
		self.submenu1 = Menu(self.menu, tearoff=0)
		self.submenu2 = Menu(self.menu, tearoff=0)
		self.submenu3 = Menu(self.menu, tearoff=0)

		self.menu.add_cascade(label="Game", menu=self.submenu1)
		self.submenu1.add_command(label="New Game    F2")
		self.submenu1.add_separator()
		self.submenu1.add_radiobutton(label="Beginner", value=1, variable=self.variable, command=lambda:difficulty1(master))
		self.submenu1.add_radiobutton(label="Intermediate", value=2, variable=self.variable, command=lambda:difficulty2(master))
		self.submenu1.add_radiobutton(label="Expert", value=3, variable=self.variable, command=lambda:difficulty3(master))
		self.submenu1.add_separator()
		self.submenu1.add_command(label="Quit", command=lambda:QuitPrompt(master))

		self.menu.add_cascade(label="Options", menu=self.submenu2)
		self.submenu2.add_checkbutton(label="Tutorial coming soon")

		self.submenu3.add_command(label="Instructions", command=lambda:InstructionsInChrome(master))
		self.submenu3.add_separator()
		self.menu.add_cascade(label="Help", menu=self.submenu3)
		self.submenu3.add_command(label="About", command=lambda:AboutInChrome(master))

		root.bind('<F2>', lambda e:master.destroy())

		self.variable.set(1)
		difficulty1(master)
		master.geometry("250x310")


root = Tk()
minesweeper = GUI(root)

if __name__ == '__main__':
		print("started game")
		mainloop()
		print("finished game")
