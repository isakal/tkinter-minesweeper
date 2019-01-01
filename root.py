from tkinter import *
from buttons import *
from functions import *
from configparser import *

config = ConfigParser()
config.read_file(open(r"config.txt"))


class GUI:
	def __init__(self, master):
		global buttonFrame
		self.master = master
		framePre = Frame(master, background="grey17")
		framePre.pack(fill=X, ipady=buttonFramePadding / 2)
		buttonFrame = Frame(master, background="grey80")
		buttonFrame.pack(fill='both', expand=True)
		defaultDiff(master, buttonFrame)

		self.menu = Menu(master, tearoff=0)
		master.config(menu=self.menu)

		self.submenu1 = Menu(self.menu, tearoff=0)
		self.submenu2 = Menu(self.menu, tearoff=0)
		self.submenu3 = Menu(self.menu, tearoff=0)

		self.menu.add_cascade(label="Game", menu=self.submenu1)
		self.submenu1.add_command(label="New Game    F2", command=lambda: newGame(diff.get(), master, buttonFrame))
		self.submenu1.add_separator()
		self.submenu1.add_radiobutton(label="Beginner", value=1, variable=diff,
									  command=lambda: [createFrame(), difficulty1(master, buttonFrame)])
		self.submenu1.add_radiobutton(label="Intermediate", value=2, variable=diff,
									  command=lambda: [createFrame(), difficulty2(master, buttonFrame)])
		self.submenu1.add_radiobutton(label="Expert", value=3, variable=diff,
									  command=lambda: [createFrame(), difficulty3(master, buttonFrame)])
		self.submenu1.add_separator()
		self.submenu1.add_command(label="Quit", command=lambda: QuitPrompt(master))

		self.menu.add_cascade(label="Options", menu=self.submenu2)
		self.submenu2.add_checkbutton(label="Tutorial coming soon")

		self.menu.add_cascade(label="Help", menu=self.submenu3)
		self.submenu3.add_command(label="Instructions", command=lambda: InstructionsInChrome())
		self.submenu3.add_separator()
		self.submenu3.add_command(label="About", command=lambda: AboutInChrome())
		self.submenu3.add_separator()
		self.submenu3.add_command(label="Credits", command=lambda: [createFrame(), Credits(master, buttonFrame)])

		def createFrame():
			global buttonFrame
			buttonFrame.destroy()
			buttonFrame = Frame(self.master, background="grey80")
			buttonFrame.pack(fill='both', expand=True)

class settings:
	def __init__(self, master):
		global diff
		master.title("Minesweeper")
		master.iconbitmap(r'mnswpr.ico')
		master.resizable(FALSE, FALSE)
		diff = IntVar()
		diff.set(1)


class binds:
	def __init__(self, master):
		root.bind('<F2>', lambda e: newGame(diff.get(), master, buttonFrame))


root = Tk()
settings = settings(root)
minesweeper = GUI(root)
binds = binds(root)

if __name__ == '__main__':
	print("started game")
	mainloop()
	print("finished game")
# TODO: add if __name__ == '__main__': in an seperate file
