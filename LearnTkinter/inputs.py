from tkinter import *

root = Tk()#you always have to have a root

e = Entry(root, width=75, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name: ")

#create a function for the button to call
def myClick():
    myLabel = Label(root, text=e.get())#gets the input from the e entry field
    myLabel.pack()

#creating a button                    
myButton = Button(root, text="Enter Your Name", command=myClick)

myButton.pack()


#have to make root the main loop
root.mainloop()