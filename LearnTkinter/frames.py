from tkinter import *
from PIL import ImageTk, Image

root = Tk()#you always have to have a root
root.title("Icons, Images, and Exit Buttons")
root.iconbitmap('LearnTkinter/images/wow.ico')

frame = LabelFrame(root, text="This is a Frame...", padx=50, pady=50)
frame.pack(padx=25, pady=25)

b = Button(frame, text="Don't Click")
b2 = Button(frame, text="Or Else")

b.grid(row=0, column=0)
b2.grid(row=1, column=1)


#have to make root the main loop
root.mainloop()