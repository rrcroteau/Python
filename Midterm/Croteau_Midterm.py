#Ron Croteau
#Midterm
#August 18, 2021
#SE126.02

#PROGRAM PROMPT: This program allows the user to determine which armor loot drops from the Sanctum of Domination raid bosses in the 9.2 World of Warcraft patch.  The user will be presented a menu(s) where the loot can be sorted by armor type, armor slot, or boss which drops the loot.


#VARIABLE DICTIONARY:

#csvfile --> shorthand name for file location, full file path
#file --> friendly name for file data, after it has been passed through csv.reader()
#rec --> LIST, an individual record from the file; only used when connected to file
#armorType--> LIST, STR, contains the armor type (eg. Plate) ( rec[0] )
#armorSlot --> LIST, STR, contains the slot the armor is worn (eg. Head) ( rec[1] )
#armorName --> LIST, STR, contains the name of the armor piece (eg. Shadowsteel Facecage) ( rec[2] )
#boss --> LIST, STR, contains the name of the boss that drops the armor piece (eg. The Tarragrue) ( rec[3] )
#ilvl --> LIST, STR, contains the item level of the armor, which is dependant on the boss ( rec[3] that drops the armor
#choice --> STR, contains the choice the user made in a menu 

#--IMPORTS--#

#for text file handling
import csv

#--FUNCTIONS--#

def menu():

    '''Displays a menu to the user. Validates the user's choice before returning the choice'''

    print("\t\tMENU")
    print("1. Sort by Armor Type")
    print("2. Sort by Armor Slot")
    print("3. Sort by Boss")
    print("4. Print Full Loot Table")
    print("5. EXIT")

    choice = input("\n\t\tPlease enter a choice from the list above >  ")

    #verify that the user input a digit (integer) so that the validation works properly
    while not choice.isdigit(): 

        print("\n\t**Input Error**")
        print("You may only enter integers (0-9)")
        choice = input("\n\t\tPlease enter a choice from the list above >  ")

    choice = int(choice)

    while choice < 1 or choice > 5:

            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice (1-5)> ")

            while not choice.isdigit(): 

                print("\n\t**Input Error**")
                print("You may only enter integers (0-9)")
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
        print("You may only enter integers (0-9)")
        choice = input("\n\t\tPlease enter a choice from the list above >  ")

    choice = int(choice)

    while choice < 1 or choice > 4:

            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice (1-4)> ")

            while not choice.isdigit(): 

                print("\n\t**Input Error**")
                print("You may only enter integers (0-9)")
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
        print("You may only enter integers (0-9)")
        choice = input("\n\t\tPlease enter a choice from the list above >  ")

    choice = int(choice)

    while choice < 1 or choice > 8:

            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice (1-8)> ")

            while not choice.isdigit(): 

                print("\n\t**Input Error**")
                print("You may only enter integers (0-9)")
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

#connect to file and extract data into respective lists
with open("Midterm/drops.csv") as csvfile:
    
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

#present menu to user and store choice to variable for loop control
choice = menu()

while choice != 5:

    if choice == 1: #sort by armor type

        choice = typeMenu()
      
        if choice == 1: #plate

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorType[i] == "Plate":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()           

        elif choice == 2: #cloth

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorType[i] == "Cloth":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")   
            choice = menu()              
            
        elif choice == 3: #leather

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorType[i] == "Leather":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n") 
            choice = menu()
            
        elif choice == 4: #mail

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

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Head":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 2: #shoulders

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Shoulders":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 3: #chest

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Chest":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 4: #belt

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Belt":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 5: #bracers

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Bracers":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 6: #hands

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Hands":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 7: #legs

            #headers for data
            print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
            print("---------------------------------------------------------------------------------------")

            for i in range(0, len(boss)):

                if armorSlot[i] == "Legs":

                    print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
            
            print("\n\n")
            choice = menu()

        elif choice == 8: #boots

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

    else:

        #headers for data
        print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
        print("---------------------------------------------------------------------------------------")

        for i in range(0, len(boss)):

            print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
        
        print("\n\n")
        choice = menu()   
  
goodbye()


