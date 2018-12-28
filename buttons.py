from tkinter import *
from root import *

for i in range(0,10):
	for j in range(0,10):
		b = Button(frame1, text="")
		x=25
		b.place(height=x,width=x,x=i*x,y=j*x)


