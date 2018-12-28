from tkinter import *
from tkinter import messagebox
import webbrowser
from buttons import *


class GUI:
	def __init__(self, master):
		self.master = master
		global frame1
		self.frame1 = Frame(master, background="grey17")
		self.frame1.pack(fill='both', expand=True)
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
		self.submenu1.add_command(label="New Game")
		self.submenu1.add_separator()
		self.submenu1.add_radiobutton(label="Beginner", value=1, variable=self.variable, command=self.difficulty1)
		self.submenu1.add_radiobutton(label="Intermediate", value=2, variable=self.variable, command=self.difficulty2)
		self.submenu1.add_radiobutton(label="Expert", value=3, variable=self.variable, command=self.difficulty3)
		self.variable.set(1)
		self.difficulty1()

		self.submenu1.add_separator()
		self.submenu1.add_command(label="Quit", command=self.QuitPrompt)

		self.menu.add_cascade(label="Options", menu=self.submenu2)
		self.submenu2.add_checkbutton(label="Tutorial coming soon")

		self.submenu3.add_command(label="Instructions", command=self.InstructionsInChrome)
		self.submenu3.add_separator()
		self.menu.add_cascade(label="Help", menu=self.submenu3)
		self.submenu3.add_command(label="About", command=self.AboutInChrome)






	def difficulty1(self):
		self.master.geometry("300x300")
		self.frame1 = Frame(self.master, background="grey17", width=300, height=300)

	def difficulty2(self):
		self.master.geometry("600x300")
		self.frame1 = Frame(self.master, background="grey17", width=600, height=300)

	def difficulty3(self):
		self.master.geometry("1000x800")
		self.frame1 = Frame(self.master, background="grey17", width=1000, height=800)

	def QuitPrompt(self):
		self.quitPrompt = messagebox.askquestion("Quit", "Are You Sure you want to exit?", icon="warning")
		if self.quitPrompt.lower() == "yes":
			self.master.destroy()

	def InstructionsInChrome(self):
		webbrowser.open('www.freeminesweeper.org/help/minehelpinstructions.html')

	def AboutInChrome(self):
		webbrowser.open('http://www.freeminesweeper.org/help/mineabout.html')

	if __name__ == '__main__':
		print("started game")
		mainloop()
		print("finished game")


root = Tk()
minesweeper = GUI(root)
