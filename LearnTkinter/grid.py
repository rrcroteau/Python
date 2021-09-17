from tkinter import *

root = Tk()#you always have to have a root

#creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Ron Croteau!")

#display using the grid -- locations are relative
myLabel1.grid(row = 0, column = 0)#you can just add .grid to the end of the label creation
myLabel2.grid(row = 1, column = 0)


#have to make root the main loop
root.mainloop()