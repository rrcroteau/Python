#Ron Croteau
#Lab 4B
#August 9, 2021
#SE126.02

#PROGRAM PROMPT: 4B. After completing 4A, use it as a basis for 4B.  You should have the following lists for each person in the original file:   LIST0      LIST1       LIST2    LIST3       LIST4              LIST5
#       Firstname   Lastname   Age      Nickname    House Allegiance   House Motto
# Build a program, utilizing these lists, that allows a user to select options from a menu:
# MENU  1. Print all First, Last, and nicknames  2.Print Last names with House Allegiance and Motto 3. Print full records 4. EXIT
# Based on the user’s selection, print what they have requested.  They should immediately be returned to the menu unless they have chosen “4. EXIT” in which case they should see a Goodbye message.  Specifications: The menu should be printed from a function that returns the user’s selection to be utilized by the main/base program.  The function should not return unless the user has supplied 1, 2, 3, or 4 only. All printed data must be values stored in lists. The goodbye message must come from a function

#VARIABLE DICTIONARY:
#records --> holds the number of records (people) processed
#csvfile --> shorthand name for file location, full file path
#file --> friendly name for file data, after it has been passed through csv.reader()
#rec --> LIST, an individual record from the file; only used when connected to file
#first_name --> LIST, STR, contains the first names of characters ( rec[0] )
#last_name --> LIST, STR, contains the last names of characters ( rec[1] )
#age --> LIST, INT, contains the ages of characters ( int(rec[2]) )
#nickname --> LIST, STR, contains the nicknames of characters ( rec[3] )
#house --> LIST, STR, contains the house allegiances of characters ( rec[4] )
#motto --> LIST, STR, contains the motto of characters based on house allegiances
#choice --> STR, the choice returned from the menu the user is presented -- used to determine what to print or to exit the program


#--IMPORTS--#

#for text file handling
import csv

#--FUNCTIONS--#

def menu():

    '''Displays a menu to the user. Validates the user's choice before returning the choice'''

    print("\t\tMENU")
    print("1. Print all First, Last, and Nicknames")
    print("2. Print Last Names with House Allegiance and Motto")
    print("3. Print full records")
    print("4. EXIT")

    choice = input("\n\t\tPlease enter a choice from the list above: ")

    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice > ")

    return choice

def goodbye():

    '''Prints a goodbye message to the user'''

    print("\n\n\tThank you for using the program, goodbye!")

#--MAIN EXECUTING CODE--#

#initialize counting variables and empty lists
records = 0
first_name = []
last_name = []
age = []
nickname = []
house = []
motto = []


#connect to file and extract data into respective lists
with open("Week4_Labs/lab4A_GOT_NEW.txt") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file:

        records +=1

        first_name.append(rec[0])
        last_name.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        house.append(rec[4])

#disconnect from the file

#process the lists to add the house motto [dependent on field 4, house allegiance] 
for i in range(0, records):

    if house[i] == "House Stark":

        motto.append("Winter is Coming")

    elif house[i] == "House Baratheon":

        motto.append("Ours is the fury.")

    elif house[i] == "House Tully":

        motto.append("Family. Duty. Honor.")

    elif house[i] == "Night's Watch":

        motto.append("And now my watch begins.")

    elif house[i] == "House Lannister":

        motto.append("Hear me roar!")

    elif house[i] == "House Targaryen":

        motto.append("Fire & Blood")

choice = menu()

while choice != "4":

    if choice == "1": #print first, last, and nicknames

        print(f"{'FIRST NAME':10}\t{'LAST NAME':10}\t{'NICKNAME':20}")
        print("-------------------------------------------------------------")

        for i in range(0, records):

            print(f"{first_name[i]:10}\t{last_name[i]:10}\t{nickname[i]:20}")

        print("\n\n")

        choice = menu()

    elif choice == "2": #print last name, house allegiance, and motto

        print(f"{'LAST NAME':10}\t{'HOUSE':18}\t{'MOTTO'}")
        print("-------------------------------------------------------------------------------")

        for i in range(0, records):

            print(f"{last_name[i]:10}\t{house[i]:18}\t{motto[i]}")

        print("\n\n")

        choice = menu()

    else: #print the full records (choice == "3")

        print(f"\n\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'AGE':4}\t{'NICKNAME':20}\t{'HOUSE':18}\t{'MOTTO'}")
        print("----------------------------------------------------------------------------------------------------------------")

        for i in range(0, records):

             print(f"{first_name[i]:10}\t{last_name[i]:10}\t{age[i]:<4}\t{nickname[i]:20}\t{house[i]:18}\t{motto[i]}")

        print("\n\n")

        choice = menu()

goodbye()
