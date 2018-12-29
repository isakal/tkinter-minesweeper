from tkinter import *
from root import *



for i in range(0,10):
	for j in range(0,10):
		b = Button(buttonFrame)
		buttonSize=25
		b.place(height=buttonSize,width=buttonSize,x=i*buttonSize,y=j*buttonSize)
root.bind('<F2>', quit)						#added foundation for F2=New Game