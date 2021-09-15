#Ron Croteau
#Final
#September 25, 2021
#SE126.02

#PROGRAM PROMPT: This program allows the user to determine which armor loot drops from the Sanctum of Domination raid bosses in the 9.1 World of Warcraft patch.  The user will be presented a menu(s) where the loot can be sorted by armor type, armor slot, boss which drops the loot, search by unique ID, print a random piece of armor, or print the full loot table. All sorted lists will present the armor in order of the appearance of the boss in the raid.

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
#choice --> STR, contains the choice the user made in a menu 
#randomChoice --> STR, contains a random number between 10000 and 10067 selected by using random.choice() on the _id list, used to display a random piece of armor to the user when desired

#--IMPORTS--#

#for text file handling
import csv
import random

#--FUNCTIONS--#

def menu():

    '''Displays a menu to the user. Validates the user's choice before returning the choice'''

    print("\t\tMENU")
    print("1. Sort by Armor Type")
    print("2. Sort by Armor Slot")
    print("3. Sort by Boss")
    print("4. Search for Armor by Specific ID Code")
    print("5. Display a Random Piece of Armor")
    print("6. Print Full Loot Table")
    print("7. EXIT")

    choice = input("\n\t\tPlease enter a choice from the list above >  ")

    #verify that the user input a digit (integer) so that the validation works properly
    while not choice.isdigit(): 

        print("\n\t**Input Error**")
        print("You may only enter integers (1-7)")
        choice = input("\n\t\tPlease enter a choice from the list above >  ")

    choice = int(choice)

    while choice < 1 or choice > 7:

            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice (1-7)> ")

            while not choice.isdigit(): 

                print("\n\t**Input Error**")
                print("You may only enter integers (1-7)")
                choice = input("\n\t\tPlease enter a choice from the list above >  ")

            choice = int(choice)

    return choice

def typeMenu():

    '''Displays a menu to the user for armor types. Validates the user's choice before returning the choice'''

    print("\n\t\tARMOR TYPES")
    print("1. Print all Plate")
    print("2. Print all Cloth")
    print("3. Print all Leather")
    print("4. Print all Mail")

    choice = input("\n\t\tPlease enter a choice from the list above >  ")

    #verify that the user input a digit (integer) so that the validation works properly
    while not choice.isdigit(): 

        print("\n\t**Input Error**")
        print("You may only enter integers (1-4)")
        choice = input("\n\t\tPlease enter a choice from the list above >  ")

    choice = int(choice)

    while choice < 1 or choice > 4:

            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice (1-4)> ")

            while not choice.isdigit(): 

                print("\n\t**Input Error**")
                print("You may only enter integers (1-4)")
                choice = input("\n\t\tPlease enter a choice from the list above >  ")

            choice = int(choice)

    return choice

def slotMenu():

    '''Displays a menu to the user for armor slots. Validates the user's choice before returning the choice'''

    print("\n\t\tARMOR SLOT")
    print("1. Print all Head")
    print("2. Print all Shoulders")
    print("3. Print all Chest")
    print("4. Print all Belt")
    print("5. Print all Bracers")
    print("6. Print all Hands")
    print("7. Print all Legs")
    print("8. Print all Boots")

    choice = input("\n\t\tPlease enter a choice from the list above >  ")

    #verify that the user input a digit (integer) so that the validation works properly
    while not choice.isdigit(): 

        print("\n\t**Input Error**")
        print("You may only enter integers (1-8)")
        choice = input("\n\t\tPlease enter a choice from the list above >  ")

    choice = int(choice)

    while choice < 1 or choice > 8:

            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice (1-8)> ")

            while not choice.isdigit(): 

                print("\n\t**Input Error**")
                print("You may only enter integers (1-8)")
                choice = input("\n\t\tPlease enter a choice from the list above >  ")

            choice = int(choice)

    return choice

def bossMenu():

    '''Displays a menu to the user for armor slots. Validates the user's choice before returning the choice'''

    print("\n\t\tBOSS")
    print(" 1. The Tarragrue")
    print(" 2. The Eye of the Jailer")
    print(" 3. The Nine")
    print(" 4. Remnant of Ner'zhul")
    print(" 5. Soulrender Dormazain")
    print(" 6. Painsmith Raznal")
    print(" 7. Guardian of the First Ones")
    print(" 8. Fatescribe Roh-Kalo")
    print(" 9. Kel'Thuzad")
    print("10. Sylvanas Windrunner")
        
    choice = input("\n\t\tPlease enter a choice from the list above >  ")

    #verify that the user input a digit (integer) so that the validation works properly
    while not choice.isdigit(): 

        print("\n\t**Input Error**")
        print("You may only enter integers (0-9)")
        choice = input("\n\t\tPlease enter a choice from the list above >  ")

    choice = int(choice)

    while choice < 1 or choice > 10:

            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice (1-10)> ")

            while not choice.isdigit(): 

                print("\n\t**Input Error**")
                print("You may only enter integers (0-9)")
                choice = input("\n\t\tPlease enter a choice from the list above >  ")

            choice = int(choice)

    return choice

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

def goodbye():

    '''Prints a goodbye message to the user'''

    print("\n\n\tThank you for using the program, goodbye!")

#--MAIN EXECUTING CODE--#

#initialize counting variables and empty lists

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

#present menu to user and store choice to variable for loop control
choice = menu()

while choice != 7:

    if choice == 1: #sort by armor type

        choice = typeMenu()
      
        if choice == 1: #plate

            #bubble sort by boss order
            bubble(order)
            
            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorType[i] == "Plate":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()           

        elif choice == 2: #cloth

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorType[i] == "Cloth":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")   
            choice = menu()              
            
        elif choice == 3: #leather

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorType[i] == "Leather":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n") 
            choice = menu()
            
        elif choice == 4: #mail

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorType[i] == "Mail":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

    elif choice == 2: #sort by armor slot

        choice = slotMenu()
        
        if choice == 1: #head

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Head":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 2: #shoulders

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Shoulders":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 3: #chest

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Chest":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 4: #belt

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Belt":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 5: #bracers

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Bracers":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 6: #hands

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Hands":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 7: #legs

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Legs":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 8: #boots

            #bubble sort by boss order
            bubble(order)

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Boots":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n") 
            choice = menu()         

    elif choice == 3: #sort by Boss

        choice = bossMenu()
        
        if choice == 1: #The Tarragrue

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "The Tarragrue":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 2: #The Eye of the Jailer

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "The Eye of the Jailer":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 3: #The Nine

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "The Nine":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 4: #Remnant of Ner'zhul

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "Remnant of Ner'zhul":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 5: #Soulrender Dormazain

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "Soulrender Dormazain":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 6: #Painsmith Raznal

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "Painsmith Raznal":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 7: #Guardian of the First Ones

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "Guardian of the First Ones":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 8: #Fatescribe Roh-Kalo

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "Fatescribe Roh-Kalo":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n") 
            choice = menu()

        elif choice == 9: #Kel'Thuzad

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "Kel'Thuzad":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n") 
            choice = menu()

        elif choice == 10: #Sylvanas Windrunner

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if boss[i] == "Sylvanas Windrunner":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n") 
            choice = menu()

    elif  choice == 4: #binary search for unique ID
        
        #bubble sort by id
        bubble(_id)

        search = input("Please enter the UNIQUE ID of the armor you are searching for: [10000 - 10067] >")

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

            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")
            print(f"{armorType[guess]:8}{armorSlot[guess]:10}{armorName[guess]:37}{boss[guess]:28}{ilvl[guess]:12} ")
        
        else:
            
            print(f"Your search for {search} was *NOT FOUND*!")
            print("Please verify you entered a number between 10000 and 10067 and try again.")

        print("\n\n") 
        choice = menu()

    elif  choice == 5: #print random armor piece
        
        #get a random item based of the unique ID list
        randomChoice = random.choice(_id)
        #print(randomChoice)

        #locate and print the random item using the binary search with the randomChoice as the search parameter (this will ALWAYS be found as it was plucked directly from the list)
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

        if randomChoice == (_id[guess]):

            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")
            print(f"{armorType[guess]:8}{armorSlot[guess]:10}{armorName[guess]:37}{boss[guess]:28}{ilvl[guess]:12} ")
        
        print("\n\n") 
        choice = menu()

    else: #print full list

        #bubble sort by boss order
        bubble(order)

        #headers for data
        print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
        print("---------------------------------------------------------------------------------------")

        for i in range(0, len(boss)):

            print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
        
        print("\n\n")
        choice = menu()   
  
goodbye()


