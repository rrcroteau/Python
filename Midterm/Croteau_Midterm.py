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

    while choice < "1" or choice > "5":
            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice > ")

    return choice

def typeMenu():

    '''Displays a menu to the user for armor types. Validates the user's choice before returning the choice'''

    print("\t\tARMOR TYPES")
    print("1. Print all Plate")
    print("2. Print all Cloth")
    print("3. Print all Leather")
    print("4. Print all Mail")
    print("5. EXIT")

    choice = input("\n\t\tPlease enter a choice from the list above >  ")

    while choice < "1" or choice > "5":
            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice > ")

    return choice

def slotMenu():

    '''Displays a menu to the user for armor slots. Validates the user's choice before returning the choice'''

    print("\t\tARMOR SLOT")
    print("1. Print all Head")
    print("2. Print all Shoulders")
    print("3. Print all Chest")
    print("4. Print all Belt")
    print("5. Print all Bracers")
    print("6. Print all Hands")
    print("7. Print all Legs")
    print("8. Print all Boots")
    print("9. EXIT")

    choice = input("\n\t\tPlease enter a choice from the list above >  ")

    while choice < "1" or choice > "9":
            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice > ")

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

while choice != "5":

    if choice == "1": #sort by armor type

        typeChoice = typeMenu()

        if typeChoice != "5":
        
            if typeChoice == "1": #plate

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorType[i] == "Plate":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")           

            elif typeChoice == "2": #cloth

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorType[i] == "Cloth":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")                 
                
            elif typeChoice == "3": #leather

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorType[i] == "Leather":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n") 
                
            else: #mail

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorType[i] == "Mail":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")  

        goodbye()

    elif choice == "2": #sort by armor slot

        choice = slotMenu()

        while choice != "9":
        
            if choice == "1": #head

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorSlot[i] == "Head":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")
                choice = menu()

            elif choice == "2": #shoulders

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorSlot[i] == "Shoulders":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")
                choice = menu()

            elif choice == "3": #chest

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorSlot[i] == "Chest":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")
                choice = menu()

            elif choice == "4": #belt

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorSlot[i] == "Belt":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")
                choice = menu()

            elif choice == "5": #bracers

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorSlot[i] == "Bracers":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")
                choice = menu()

            elif choice == "6": #hands

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorSlot[i] == "Hands":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")
                choice = menu()

            elif choice == "7": #legs

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorSlot[i] == "Legs":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")
                choice = menu()

            else: #boots

                #headers for data
                print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
                print("---------------------------------------------------------------------------------------")

                for i in range(0, len(boss)):

                    if armorSlot[i] == "Boots":

                        print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
                
                print("\n\n")
                choice = menu()

        goodbye()          

    elif choice == "3":

        pass

    else:

        #headers for data
        print(f"{'TYPE':8}{'SLOT':10}{'ARMOR NAME':37}{'BOSS':28}{'ILVL':4}")
        print("---------------------------------------------------------------------------------------")

        for i in range(0, len(boss)):

            print(f"{armorType[i]:8}{armorSlot[i]:10}{armorName[i]:37}{boss[i]:28}{ilvl[i]:12} ")
        
        print("\n\n")
    
    



goodbye()
# #headers for original data
# print(f"{'FIRST NAME':10}\t{'LAST NAME':10}\t{'AGE':4}\t{'NICKNAME':20}\t{'HOUSE':18}")
# print("-------------------------------------------------------------------------------")

# #process lists to print original data
# for i in range(0, records):

#     print(f"{first_name[i]:10}\t{last_name[i]:10}\t{age[i]:<4}\t{nickname[i]:20}\t{house[i]:18}")

