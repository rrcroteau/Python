#Ron Croteau
#Final
#September 25, 2021
#SE126.02

#PROGRAM PROMPT: This program allows the user to determine which armor loot drops from the Sanctum of Domination raid bosses in the 9.1 World of Warcraft patch.  The user will be presented menus via a graphical user interface(GUI) where the loot can be sorted and displayed by armor type, armor slot, boss which drops the loot, search by unique ID, or a random piece of armor. All sorted lists will present the armor in order of the appearance of the boss in the raid. The user must simply press buttons on the GUI in order to navigate the menus and can search/sort as many times as they would like.

#VARIABLE DICTIONARY:

#csvfile --> shorthand name for file location, full file path
#file --> friendly name for file data, after it has been passed through csv.reader()
#rec --> LIST, an individual record from the file; only used when connected to file
#armorType--> LIST, STR, contains the armor type (eg. Plate) ( rec[0] )
#armorSlot --> LIST, STR, contains the slot the armor is worn (eg. Head) ( rec[1] )
#armorName --> LIST, STR, contains the name of the armor piece (eg. Shadowsteel Facecage) ( rec[2] )
#boss --> LIST, STR, contains the name of the boss that drops the armor piece (eg. The Tarragrue) ( rec[3] )
#ilvl --> LIST, STR, contains the item level of the armor, which is dependant on the boss ( rec[3] ) that drops the armor
#order --> LIST, INT, contains the order of which the bosses appear in the raid
#_id --> LIST, INT, contains a unique ID for each piece of armor that is dropped
#startID --> INT, the starting ID for items, will be incremented on
#randomChoice --> STR, contains a random number between 10000 and 10067 selected by using random.choice() on the _id list, used to display a random piece of armor to the user when desired
#root --> WINDOW, the main window presented to the user via Tkinter
#*name*_frame --> FRAME widget contains the name of a frame which is relavant to what frame is holding all the widgets on the current view
#*name*_menu --> LABEL widget which has a relevant name of menu being displayed and acts as the the FRAME header
#*name*_button --> BUTTON widget which has a relevant name of text being displayed on the button
#e --> ENTRY widget which will store the STR the user entered in the field once it has been submitted with a BUTTON click
#header_*name* --> LABEL widget which has a relavent name for the header it is used to display
#armor_*name* --> LABEL widget which has a relavent name for the armor it is used to display

#--IMPORTS--#

#for text file handling
import csv
#for a random armor selection
import random 
#to create a GUI
from tkinter import * 

#--FUNCTIONS--#

def swap(list, index):

    '''This function takes a list name and an index and swaps value of the current index with the index + 1, used for bubble sorting'''

    t = list[index]
    list[index]= list[index + 1]
    list[index + 1] = t

def bubble(list):

    '''This function takes a list name and bubble sorts all the list based on the passed list's value'''

    for i in range(0, len(list) - 1):#outer loop
    
        for index in range(0, len(list) - 1):#inner loop

            #list used is the list being sorted
            # > is for increasing order, < for decreasing
            if(list[index] > list[index + 1]):
                
                #swap all lists using the swap function
                swap(armorType, index)
                swap(armorSlot, index)
                swap(armorName, index)
                swap(boss, index)
                swap(ilvl, index)
                swap(order, index)
                swap(_id, index)

def menu(previous_frame):

    '''Displays the main menu to the user. Passes the name of the frame on the previous display so it can be destroyed'''

    #this will only == "start" the very first time it is created, in all other instances it will wipe the screen clean so a frame can be built
    if previous_frame != "start":

        previous_frame.destroy()    

    #build the main menu frame and all widgets to be displayed
    global main_frame#make this global so the frame can be deleted in other menus without having to pass it
    main_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    main_frame.pack(padx=25, pady=25)

    #create a header for the menu to be placed above the clickable buttons
    main_menu = Label(main_frame, text="MAIN MENU", bg="white", anchor=CENTER, font="Arial 48 bold")
    main_menu.pack(pady=2)#pack the label onto the window with a bit of padding from the top

    #create all the clickable buttons which will execute specific functions when clicked via the command attribute
    armor_type_button = Button(main_frame, text="Sort by Armor Type", bg="white", font="Arial 26 bold", pady=5, command=typeMenu)
    armor_type_button.pack(pady=2)

    armor_slot_button = Button(main_frame, text="Sort by Armor Slot", bg="white", font="Arial 26 bold", pady=5, command=slotMenu)
    armor_slot_button.pack(pady=2)

    boss_button = Button(main_frame, text="Sort by Boss", bg="white", font="Arial 26 bold", pady=5, command=bossMenu)
    boss_button.pack(pady=2)

    id_button = Button(main_frame, text="Search by Unique ID", bg="white", font="Arial 26 bold", pady=5, command=idMenu)
    id_button.pack(pady=2)

    random_button = Button(main_frame, text="Display a Random Armor Piece", bg="white", font="Arial 26 bold", pady=5, command=displayRandom)
    random_button.pack(pady=2)

    exit_button = Button(main_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold",pady=25, command=root.quit)
    exit_button.pack(pady=2)

def typeMenu():

    '''Displays the armor type menu to the user'''
    #destroy the previous menu frame
    main_frame.destroy()
    #create new frame for current selection and display
    global type_frame#make this global so the frame can be deleted in other menus without having to pass it
    type_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    type_frame.pack(padx=25, pady=25)

    #create a header for the menu to be placed above the clickable buttons
    type_menu = Label(type_frame, text="ARMOR BY TYPE", bg="white", anchor=CENTER, font="Arial 48 bold")
    type_menu.pack(pady=2)#pack the label onto the window with a bit of padding from the top

    #create all the clickable buttons which will execute specific functions when clicked via the command attribute
    plate_button = Button(type_frame, text="Display all Plate", bg="white", font="Arial 26 bold", pady=2, command=displayPlate)
    plate_button.pack(pady=2)

    mail_button = Button(type_frame, text="Display all Mail", bg="white", font="Arial 26 bold", pady=2, command=displayMail)
    mail_button.pack(pady=2)

    cloth_button = Button(type_frame, text="Display all Cloth", bg="white", font="Arial 26 bold", pady=2, command=displayCloth)
    cloth_button.pack(pady=2)

    leather_button = Button(type_frame, text="Display all Leather", bg="white", font="Arial 26 bold", pady=2, command=displayLeather)
    leather_button.pack(pady=2)

    exit_button = Button(type_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=25, command=root.quit)
    exit_button.pack(pady=2)

def slotMenu():

    '''Displays the armor slot menu to the user'''
    #destroy the previous menu frame
    main_frame.destroy()
    #create new frame for current selection and display
    global slot_frame#make this global so the frame can be deleted in other menus without having to pass it
    slot_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    slot_frame.pack(padx=25, pady=25)

    #create a header for the menu to be placed above the clickable buttons
    slot_menu = Label(slot_frame, text="ARMOR BY SLOT", bg="white", anchor=CENTER, font="Arial 48 bold")
    slot_menu.pack(pady=5)#pack the label onto the window with a bit of padding from the top

    #create all the clickable buttons which will execute specific functions when clicked via the command attribute
    head_button = Button(slot_frame, text="Display all Head Armor", bg="white", font="Arial 26 bold", pady=2, command=displayHead)
    head_button.pack(pady=2)

    shoulders_button = Button(slot_frame, text="Display all Shoulder Armor", bg="white", font="Arial 26 bold", pady=2, command=displayShoulders)
    shoulders_button.pack(pady=2)

    chest_button = Button(slot_frame, text="Display all Chest Armor", bg="white", font="Arial 26 bold", pady=2, command=displayChest)
    chest_button.pack(pady=2)

    belt_button = Button(slot_frame, text="Display all Belt Armor", bg="white", font="Arial 26 bold", pady=2, command=displayBelt)
    belt_button.pack(pady=2)

    bracers_button = Button(slot_frame, text="Display all Bracer Armor", bg="white", font="Arial 26 bold", pady=2, command=displayBracers)
    bracers_button.pack(pady=2)

    hands_button = Button(slot_frame, text="Display all Hand Armor", bg="white", font="Arial 26 bold", pady=2, command=displayHands)
    hands_button.pack(pady=2)

    legs_button = Button(slot_frame, text="Display all Leg Armor", bg="white", font="Arial 26 bold", pady=2, command=displayLegs)
    legs_button.pack(pady=2)

    boots_button = Button(slot_frame, text="Display all Boot Armor", bg="white", font="Arial 26 bold", pady=2, command=displayBoots)
    boots_button.pack(pady=2)

    exit_button = Button(slot_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=25, command=root.quit)
    exit_button.pack(pady=5)

def bossMenu():

    '''Displays the boss menu to the user'''
    #destroy the previous menu frame
    main_frame.destroy()
    #create new frame for current selection and display
    global boss_frame#make this global so the frame can be deleted in other menus without having to pass it
    boss_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    boss_frame.pack(padx=25, pady=25)

    #create a header for the menu to be placed above the clickable buttons
    slot_menu = Label(boss_frame, text="ARMOR BY BOSS", bg="white", anchor=CENTER, font="Arial 48 bold")
    slot_menu.pack(pady=5)#pack the label onto the window with a bit of padding from the top

    #create all the clickable buttons which will execute specific functions when clicked via the command attribute
    tarragrue_button = Button(boss_frame, text="The Tarragrue", bg="white", font="Arial 26 bold", pady=2, command=displayTarragrue)
    tarragrue_button.pack(pady=2)

    eye_button = Button(boss_frame, text="The Eye of the Jailer", bg="white", font="Arial 26 bold", pady=2, command=displayEye)
    eye_button.pack(pady=2)

    nine_button = Button(boss_frame, text="The Nine", bg="white", font="Arial 26 bold", pady=2, command=displayNine)
    nine_button.pack(pady=2)

    remnant_button = Button(boss_frame, text="Remnant of Ner'zhul", bg="white", font="Arial 26 bold", pady=2, command=displayRemnant)
    remnant_button.pack(pady=2)

    soulrender_button = Button(boss_frame, text="Soulrender Dormazain", bg="white", font="Arial 26 bold", pady=2, command=displaySoulrender)
    soulrender_button.pack(pady=2)

    painsmith_button = Button(boss_frame, text="Painsmith Raznal", bg="white", font="Arial 26 bold", pady=2, command=displayPainsmith)
    painsmith_button.pack(pady=2)

    guardian_button = Button(boss_frame, text="Guardian of the First Ones", bg="white", font="Arial 26 bold", pady=2, command=displayGuardian)
    guardian_button.pack(pady=2)

    fatescribe_button = Button(boss_frame, text="Fatescribe Roh-Kalo", bg="white", font="Arial 26 bold", pady=2, command=displayFatescribe)
    fatescribe_button.pack(pady=2)

    kt_button = Button(boss_frame, text="Kel'Thuzad", bg="white", font="Arial 26 bold", pady=2, command=displayKT)
    kt_button.pack(pady=2)

    sylvanas_button = Button(boss_frame, text="Sylvanas Windrunner", bg="white", font="Arial 26 bold", pady=2, command=displaySylvanas)
    sylvanas_button.pack(pady=2)

    exit_button = Button(boss_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=25, command=root.quit)
    exit_button.pack(pady=5)

def idMenu():

    '''Display an Armor Piece based on a Unique ID entered by User'''
    
    #destroy the previous menu frame
    main_frame.destroy()
    #create new frame for current selection and display
    global id_frame#make this global so the frame can be deleted in other menus without having to pass it
    id_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    id_frame.pack(padx=25, pady=25)

    #display a title for the frame
    id_header = Label(id_frame, text="UNIQUE ID SEARCH", bg="white", anchor=CENTER, font="Arial 48 bold")
    id_header.pack(pady=5)

    #create an entry widget with a label
    entry_label = Label(id_frame, text="Enter a Unique ID from 10000 up to 100067", padx=5, pady=5, bg="white", font="Arial 22")
    entry_label.pack(padx=25, pady=25)
    e = Entry(id_frame, width=5, borderwidth=5, font="Arial 20")
    e.pack()
    
    #create a button to submit the search                                 #GETS the input from the user and sends to displayId
    search_button = Button(id_frame, text="Submit ID", font="Arial 26", command=lambda: displayId(e.get()))
    search_button.pack(pady=5)
    
def displayHeaders(frame_name):
    
    '''Displays the headers for the armor'''

    header_type = Label(frame_name, text="TYPE", font=("Arial 24"), bg="white")
    header_type.grid(row=1, column=0)
    header_slot = Label(frame_name, text="SLOT", font=("Arial 24"), bg="white")
    header_slot.grid(row=1, column=1)
    header_name = Label(frame_name, text="ARMOR NAME", font=("Arial 24"), bg="white")
    header_name.grid(row=1, column=2)
    header_boss = Label(frame_name, text="BOSS", font=("Arial 24"), bg="white")
    header_boss.grid(row=1, column=3)
    header_ilvl = Label(frame_name, text="ILVL", font=("Arial 24"), bg="white")
    header_ilvl.grid(row=1, column=4)

def displayPlate():
    
    '''Displays all Plate Armor to User'''

    #destroy the previous menu frame
    type_frame.destroy()
    #create new frame for current selection and display
    plate_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    plate_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    plate_header = Label(plate_frame, text="PLATE ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    plate_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(plate_frame)
              
    for i in range(0, len(boss)):

        if armorType[i] == "Plate":

            #create and display the armor selected // headers are at row 1, so this starts at i + 1 (row 2)    
            armor_type = Label(plate_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(plate_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(plate_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(plate_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(plate_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(plate_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(plate_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(plate_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom    

def displayMail():
    
    '''Displays all Mail Armor to User'''

    #destroy the previous menu frame
    type_frame.destroy()
    #create new frame for current selection and display
    mail_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    mail_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    mail_header = Label(mail_frame, text="MAIL ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    mail_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(mail_frame)
            
    for i in range(0, len(boss)):

        if armorType[i] == "Mail":

            #create and display the armor selected     
            armor_type = Label(mail_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(mail_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(mail_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(mail_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(mail_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(mail_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(mail_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(mail_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayCloth():
    
    '''Displays all Cloth Armor to User'''

    #destroy the previous menu frame
    type_frame.destroy()
    #create new frame for current selection and display
    cloth_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    cloth_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    cloth_header = Label(cloth_frame, text="CLOTH ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    cloth_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(cloth_frame)
               
    for i in range(0, len(boss)):

        if armorType[i] == "Cloth":

            #create and display the armor selected     
            armor_type = Label(cloth_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(cloth_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(cloth_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(cloth_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(cloth_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(cloth_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(cloth_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(cloth_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayLeather():
    
    '''Displays all Leather Armor to User'''

    #destroy the previous menu frame
    type_frame.destroy()
    #create new frame for current selection and display
    leather_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    leather_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    leather_header = Label(leather_frame, text="LEATHER ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    leather_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(leather_frame)
            
    for i in range(0, len(boss)):

        if armorType[i] == "Leather":

            #create and display the armor selected     
            armor_type = Label(leather_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(leather_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(leather_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(leather_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(leather_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(leather_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(leather_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(leather_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayHead():
    
    '''Displays all Head Armor to User'''

    #destroy the previous menu frame
    slot_frame.destroy()
    #create new frame for current selection and display
    head_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    head_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    head_header = Label(head_frame, text="HEAD ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    head_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(head_frame)
              
    for i in range(0, len(boss)):

        if armorSlot[i] == "Head":

            #create and display the armor selected     
            armor_type = Label(head_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(head_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(head_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(head_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(head_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(head_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(head_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(head_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom    

def displayShoulders():
    
    '''Displays all Shoulder Armor to User'''

    #destroy the previous menu frame
    slot_frame.destroy()
    #create new frame for current selection and display
    shoulder_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    shoulder_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    shoulder_header = Label(shoulder_frame, text="SHOULDER ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    shoulder_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(shoulder_frame)
              
    for i in range(0, len(boss)):

        if armorSlot[i] == "Shoulders":

            #create and display the armor selected     
            armor_type = Label(shoulder_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(shoulder_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(shoulder_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(shoulder_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(shoulder_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(shoulder_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(shoulder_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(shoulder_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom 

def displayChest():
    
    '''Displays all Chest Armor to User'''

    #destroy the previous menu frame
    slot_frame.destroy()
    #create new frame for current selection and display
    chest_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    chest_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    chest_header = Label(chest_frame, text="CHEST ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    chest_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(chest_frame)
              
    for i in range(0, len(boss)):

        if armorSlot[i] == "Chest":

            #create and display the armor selected     
            armor_type = Label(chest_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(chest_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(chest_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(chest_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(chest_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(chest_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(chest_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(chest_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom 

def displayBelt():
    
    '''Displays all Belt Armor to User'''

    #destroy the previous menu frame
    slot_frame.destroy()
    #create new frame for current selection and display
    belt_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    belt_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    belt_header = Label(belt_frame, text="BELT ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    belt_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(belt_frame)
              
    for i in range(0, len(boss)):

        if armorSlot[i] == "Belt":

            #create and display the armor selected     
            armor_type = Label(belt_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(belt_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(belt_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(belt_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(belt_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(belt_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(belt_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(belt_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom 

def displayBracers():
    
    '''Displays all Bracer Armor to User'''

    #destroy the previous menu frame
    slot_frame.destroy()
    #create new frame for current selection and display
    bracers_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    bracers_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    bracers_header = Label(bracers_frame, text="BRACER ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    bracers_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(bracers_frame)
              
    for i in range(0, len(boss)):

        if armorSlot[i] == "Bracers":

            #create and display the armor selected     
            armor_type = Label(bracers_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(bracers_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(bracers_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(bracers_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(bracers_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(bracers_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(bracers_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(bracers_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayHands():
    
    '''Displays all Hand Armor to User'''

    #destroy the previous menu frame
    slot_frame.destroy()
    #create new frame for current selection and display
    hands_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    hands_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    hands_header = Label(hands_frame, text="HAND ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    hands_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(hands_frame)
              
    for i in range(0, len(boss)):

        if armorSlot[i] == "Hands":

            #create and display the armor selected     
            armor_type = Label(hands_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(hands_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(hands_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(hands_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(hands_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(hands_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(hands_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(hands_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayLegs():
    
    '''Displays all Leg Armor to User'''

    #destroy the previous menu frame
    slot_frame.destroy()
    #create new frame for current selection and display
    legs_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    legs_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    legs_header = Label(legs_frame, text="LEG ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    legs_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(legs_frame)
              
    for i in range(0, len(boss)):

        if armorSlot[i] == "Legs":

            #create and display the armor selected     
            armor_type = Label(legs_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(legs_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(legs_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(legs_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(legs_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(legs_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(legs_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(legs_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayBoots():
    
    '''Displays all Boot Armor to User'''

    #destroy the previous menu frame
    slot_frame.destroy()
    #create new frame for current selection and display
    boots_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    boots_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    boots_header = Label(boots_frame, text="BOOT ARMOR DROPS", font=("Arial 36"), bg="white", pady=25)
    boots_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(boots_frame)
              
    for i in range(0, len(boss)):

        if armorSlot[i] == "Boots":

            #create and display the armor selected     
            armor_type = Label(boots_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(boots_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(boots_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(boots_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(boots_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(boots_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(boots_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(boots_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayTarragrue():
    
    '''Displays all Tarragrue Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    tarragrue_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    tarragrue_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    tarragrue_header = Label(tarragrue_frame, text="THE TARRAGRUE DROPS", font=("Arial 36"), bg="white", pady=25)
    tarragrue_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(tarragrue_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "The Tarragrue":

            #create and display the armor selected     
            armor_type = Label(tarragrue_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(tarragrue_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(tarragrue_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(tarragrue_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(tarragrue_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(tarragrue_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(tarragrue_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(tarragrue_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayEye():
    
    '''Displays all Eye of the Jailer Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    eye_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    eye_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    eye_header = Label(eye_frame, text="EYE OF THE JAILER DROPS", font=("Arial 36"), bg="white", pady=25)
    eye_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(eye_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "The Eye of the Jailer":

            #create and display the armor selected     
            armor_type = Label(eye_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(eye_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(eye_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(eye_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(eye_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(eye_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(eye_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(eye_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayNine():
    
    '''Displays all The Nine Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    nine_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    nine_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    nine_header = Label(nine_frame, text="THE NINE DROPS", font=("Arial 36"), bg="white", pady=25)
    nine_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(nine_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "The Nine":

            #create and display the armor selected     
            armor_type = Label(nine_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(nine_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(nine_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(nine_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(nine_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(nine_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(nine_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(nine_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayRemnant():
    
    '''Displays all Remnant of Ner'zhul Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    remnant_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    remnant_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    remnant_header = Label(remnant_frame, text="REMNANT OF NER'ZHUL DROPS", font=("Arial 36"), bg="white", pady=25)
    remnant_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(remnant_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "Remnant of Ner'zhul":

            #create and display the armor selected     
            armor_type = Label(remnant_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(remnant_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(remnant_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(remnant_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(remnant_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(remnant_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(remnant_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(remnant_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displaySoulrender():
    
    '''Displays all Soulrender Dormazain Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    soulrender_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    soulrender_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    soulrender_header = Label(soulrender_frame, text="SOULRENDER DORMAZAIN DROPS", font=("Arial 36"), bg="white", pady=25)
    soulrender_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(soulrender_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "Soulrender Dormazain":

            #create and display the armor selected     
            armor_type = Label(soulrender_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(soulrender_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(soulrender_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(soulrender_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(soulrender_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(soulrender_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(soulrender_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(soulrender_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayPainsmith():
    
    '''Displays all Painsmith Raznal Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    painsmith_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    painsmith_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    painsmith_header = Label(painsmith_frame, text="PAINSMITH RAZNAL DROPS", font=("Arial 36"), bg="white", pady=25)
    painsmith_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(painsmith_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "Painsmith Raznal":

            #create and display the armor selected     
            armor_type = Label(painsmith_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(painsmith_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(painsmith_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(painsmith_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(painsmith_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(painsmith_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(painsmith_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(painsmith_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayGuardian():
   
    '''Displays all Guardian of the First Ones Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    guardian_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    guardian_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    guardian_header = Label(guardian_frame, text="GUARDIAN OF THE FIRST ONES DROPS", font=("Arial 36"), bg="white", pady=25)
    guardian_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(guardian_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "Guardian of the First Ones":

            #create and display the armor selected     
            armor_type = Label(guardian_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(guardian_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(guardian_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(guardian_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(guardian_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(guardian_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(guardian_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(guardian_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayFatescribe():
    
    '''Displays all Fatescribe Roh-Kalo Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    fatescribe_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    fatescribe_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    fatescribe_header = Label(fatescribe_frame, text="FATESCRIBE ROH-KALO DROPS", font=("Arial 36"), bg="white", pady=25)
    fatescribe_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(fatescribe_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "Fatescribe Roh-Kalo":

            #create and display the armor selected     
            armor_type = Label(fatescribe_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(fatescribe_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(fatescribe_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(fatescribe_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(fatescribe_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(fatescribe_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(fatescribe_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(fatescribe_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayKT():
    
    '''Displays all Kel'Thuzad Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    kt_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    kt_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    kt_header = Label(kt_frame, text="KEL'THUZAD DROPS", font=("Arial 36"), bg="white", pady=25)
    kt_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(kt_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "Kel'Thuzad":

            #create and display the armor selected     
            armor_type = Label(kt_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(kt_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(kt_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(kt_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(kt_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(kt_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(kt_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(kt_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displaySylvanas():
    
    '''Displays all Sylvanas Windrunner Armor to User'''

    #destroy the previous menu frame
    boss_frame.destroy()
    #create new frame for current selection and display
    sylvanas_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    sylvanas_frame.pack(padx=25, pady=25)
    
    #bubble sort by boss order
    bubble(order)

    #display the header for the window
    sylvanas_header = Label(sylvanas_frame, text="SYLVANAS WINDRUNNER DROPS", font=("Arial 36"), bg="white", pady=25)
    sylvanas_header.grid(row=0, column=0, columnspan=5)
    
    #display the armor headers
    displayHeaders(sylvanas_frame)
              
    for i in range(0, len(boss)):

        if boss[i] == "Sylvanas Windrunner":

            #create and display the armor selected     
            armor_type = Label(sylvanas_frame, text=f"{armorType[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_type.grid(row=i + 1, column=0)
            armor_slot = Label(sylvanas_frame, text=f"{armorSlot[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_slot.grid(row=i + 1, column=1)
            armor_name = Label(sylvanas_frame, text=f"{armorName[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_name.grid(row=i + 1, column=2)
            armor_boss = Label(sylvanas_frame, text=f"{boss[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_boss.grid(row=i + 1, column=3)
            armor_ilvl = Label(sylvanas_frame, text=f"{ilvl[i]}", font=("Arial 24"), bg="white", padx=25)
            armor_ilvl.grid(row=i + 1, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(sylvanas_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(sylvanas_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(sylvanas_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

def displayId(search):

    #destroy the previous menu frame
    id_frame.destroy()
    #create new frame for current selection and display
    idDisplay_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    idDisplay_frame.pack(padx=25, pady=25)

    #display the header for the window
    idDisplay_header = Label(idDisplay_frame, text="UNIQUE ID SEARCH RESULTS", font=("Arial 36"), bg="white", pady=25)
    idDisplay_header.grid(row=0, column=0, columnspan=5)

    #display the armor headers
    displayHeaders(idDisplay_frame)#displayed in row 1

    #implement binary search alogorithm
    #bubble sort by id
    bubble(_id)

    min = 0
    max = len(_id) - 1
    guess = (min + max) // 2

    while (min < max and search != str(_id[guess])): #cast to STRING to match data types

        if search < str(_id[guess]):

            max = guess - 1 #search is less than middle point, so no need to consider high half of list

        else:

            min = guess + 1 #search is greater than middle point, so no need to consider low half of list

        guess = (min + max) // 2 #make sure this is not nested in if/else portion

    if search == str(_id[guess]):

        #create and display the armor selected     
        armor_type = Label(idDisplay_frame, text=f"{armorType[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_type.grid(row=2, column=0)
        armor_slot = Label(idDisplay_frame, text=f"{armorSlot[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_slot.grid(row=2, column=1)
        armor_name = Label(idDisplay_frame, text=f"{armorName[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_name.grid(row=2, column=2)
        armor_boss = Label(idDisplay_frame, text=f"{boss[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_boss.grid(row=2, column=3)
        armor_ilvl = Label(idDisplay_frame, text=f"{ilvl[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_ilvl.grid(row=2, column=4)
    
    else:
        
        failed_search = Label(idDisplay_frame, text=f"Your search for {search} was *NOT FOUND*! \nPlease verify you entered a number between 10000 and 10067 and try again.", font=("Arial 24"), bg="white")
        failed_search.grid(row=2, column=0, columnspan=5)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(idDisplay_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(idDisplay_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(idDisplay_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom
           
def displayRandom():

    '''Displays a random piece of armor based on unique ID and random.choice()'''

    #destroy the previous menu frame
    main_frame.destroy()
    #create new frame for current selection and display
    random_frame = LabelFrame(root, text="", padx=5, pady=5, bg="white")
    random_frame.pack(padx=25, pady=25)

    #get a random item based of the unique ID list
    randomChoice = random.choice(_id)

    #locate the random item using the binary search with the randomChoice as the search parameter 
    #bubble sort by id
    bubble(_id)

    min = 0
    max = len(_id) - 1
    guess = (min + max) // 2

    while (min < max and randomChoice != (_id[guess])): #randomChoice is the search paramater in this instance


        if randomChoice < (_id[guess]):

            max = guess - 1 #search is less than middle point, so no need to consider high half of list

        else:

            min = guess + 1 #search is greater than middle point, so no need to consider low half of list

        guess = (min + max) // 2 #make sure this is not nested in if/else portion

    if randomChoice == (_id[guess]):#this will ALWAYS be found as it was plucked directly from the list

        #display the header for the window
        random_header = Label(random_frame, text="RANDOM ARMOR PIECE", font=("Arial 36"), bg="white", pady=25)
        random_header.grid(row=0, column=0, columnspan=5)
        
        #display the armor headers
        displayHeaders(random_frame)#displayed in row 1

        #create and display the armor selected     
        armor_type = Label(random_frame, text=f"{armorType[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_type.grid(row=2, column=0)
        armor_slot = Label(random_frame, text=f"{armorSlot[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_slot.grid(row=2, column=1)
        armor_name = Label(random_frame, text=f"{armorName[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_name.grid(row=2, column=2)
        armor_boss = Label(random_frame, text=f"{boss[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_boss.grid(row=2, column=3)
        armor_ilvl = Label(random_frame, text=f"{ilvl[guess]}", font=("Arial 24"), bg="white", padx=25)
        armor_ilvl.grid(row=2, column=4)

    #create and display the buttons to return to main menu or exit program
    menu_button = Button(random_frame, text="Main Menu", bg="white", font="Arial 24 bold", pady=5, command=lambda: menu(random_frame))
    menu_button.grid(row=99, column=1, pady=25)#set to 99 to force to bottom
    
    exit_button = Button(random_frame, text="Exit Program", fg="red", bg="white", font="Arial 24 bold", pady=5, command=root.quit)
    exit_button.grid(row=99, column=3, pady=25)#set to 99 to force to bottom

#--MAIN EXECUTING CODE--#

#initialize empty lists

armorType = []
armorSlot = []
armorName = []
boss = []
ilvl = []
order = []
_id = []

#connect to file and extract data into respective lists
with open("Final/drops.csv") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file:

        armorType.append(rec[0])
        armorSlot.append(rec[1])
        armorName.append(rec[2])
        boss.append(rec[3])
        #print(rec)

#disconnect from the file

#determine the ilvl of the loot based on the boss who drops it

for i in range(0, len(boss)):

    if boss[i] == "Kel'Thuzad" or boss[i] == "Sylvanas Windrunner":

        ilvl.append("259")
    
    else:

        ilvl.append("252")
#print(ilvl)    

#determine the order of the boss appearance and append to list

for i in range(0, len(boss)):

    if boss[i] == "The Tarragrue":

        order.append(1)
    
    elif boss[i] == "The Eye of the Jailer":

        order.append(2)
    
    elif boss[i] == "The Nine":

        order.append(3)

    elif boss[i] == "Remnant of Ner'zhul":

        order.append(4)

    elif boss[i] == "Soulrender Dormazain":

        order.append(5)

    elif boss[i] == "Painsmith Raznal":

        order.append(6)

    elif boss[i] == "Guardian of the First Ones":

        order.append(7)

    elif boss[i] == "Fatescribe Roh-Kalo":

        order.append(8)
        
    elif boss[i] == "Kel'Thuzad":

        order.append(9)

    else:

        order.append(10)
#print(order)

#append a unique id to each item for use in a binary search
startID = 10000

for i in range(0, len(armorName)):

    _id.append(startID)
    startID += 1
#print(_id)

#create my GUI Window
root = Tk()
#set window size
root.geometry("1600x1200")
#set window color
root.configure(bg='black')
#set the title and the icon
root.title("Sanctum of Domination Armor Drops")
root.iconbitmap('Final/images/wow.ico')

#initiate the first main menu before the mainloop with "start" so that it isn't immediately destroyed by the function
menu("start")

#start the main loop
root.mainloop()