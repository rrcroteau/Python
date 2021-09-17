from tkinter import *
from PIL import ImageTk, Image

root = Tk()#you always have to have a root
root.title("Icons, Images, and Exit Buttons")
root.iconbitmap('LearnTkinter/images/wow.ico')

img_1 = ImageTk.PhotoImage(Image.open("LearnTkinter/images/shadowlands.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("LearnTkinter/images/dormazain.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("LearnTkinter/images/remnant.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("LearnTkinter/images/sylvanas.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("LearnTkinter/images/tarragrue.jpg"))

image_list = [img_1, img_2, img_3, img_4, img_5]

my_label = Label(image=img_1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == len(image_list) - 1:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 0:
        button_back = Button(root, text="<<", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

#have to make root the main loop
root.mainloop()