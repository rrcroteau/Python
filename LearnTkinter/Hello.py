from tkinter import *

root = Tk()#you always have to have a root

#creating a Label Widget
myLabel = Label(root, text="Hello World!")

#shoving it onto the screen
myLabel.pack()


#have to make root the main loop
root.mainloop()