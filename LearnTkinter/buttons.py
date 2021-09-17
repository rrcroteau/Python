from tkinter import *

root = Tk()#you always have to have a root

#create a function for the button to call
def myClick():
    myLabel = Label(root, text="Look, I work!").pack()

#creating a button                    #active is default   #change size             #call function without the ()
myButton = Button(root, text="Click Me", state="active", padx=50, pady=50,fg="white", bg="black", command=myClick)

myButton.pack()


#have to make root the main loop
root.mainloop()