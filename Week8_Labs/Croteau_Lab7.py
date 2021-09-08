#Ron Croteau
#Lab 7
#September 11, 2021
#SE126.02

#PROGRAM PROMPT: Write a program that gives the user a menu of options to search through the file.  
# The menu should be:
#            SEARCH MENU
# 1.   Search by FIRST NAME
# 2.   Search by ID CODE
# 3.   Search by LAST NAME
# 4.   Search by ALLEGIANCE
# 5.   EXIT
# Depending on how the user wants to search, you may need to sort the searched-through list before performing Binary Search.  Binary Search should be used for Menu Options 1 (First Name) and 2 (ID codes)  and the full record for the individual searched should be included if found (the user should be alerted if the person cannot be found).  If the user chooses options 3 or 4, you must print a list of everyone and their full record that fits the searched item (think: sequential search!) that has that Last Name or Allegiance.  Use the GOT_bubble_sort_7.txt file (you may change the name if you wish but you may NOT edit the text file outside of checking for and deleting empty end records).  The user should be able to search as many times as they would like.  If the user enters an option that does not exist, the program must tell them this before asking if the user would like to search for a new record
# Other stipulations of lab:
# The menu should be printed from a function that returns the user’s search selection
# A function must be used to swap values for bubble sort. 
# A function must be used to ask the user if they would like to search again. 
# o    This function should only accept the following values from the user: Y, y, N, n. Any other values will prompt the user to reenter.  The function should return the user’s input once it meets the criteria.
# A function to print a goodbye message when the user decides to exit.o    10pt BONUS: Add something GOT related to your goodbye message.  This could be a quote, a picture ... get creative (sliding scale bonus points so 1 – 10 based on what you do :] )
# The console screen should clear before each new search.

#--VARIABLE DICTIONARY--#

#records --> INT, holds the number of records (people) processed
#csvfile --> shorthand name for file location, full file path
#file --> friendly name for file data, after it has been passed through csv.reader()
#rec --> LIST, an individual record from the file; only used when connected to file
#code --> LIST, STR contains unique ID codes 
#lname --> LIST, STR, contains the last names
#fname --> LIST, STR, contains the first names
#age --> LIST, STR, contains the ages
#allegiance --> LIST, STR, contains house allegiances
#answer --> STR, used to control the search loop
#choice --> INT, the menu choice the user selected
#search --> STR, contains the search parameter as input by the user 
#min --> INT, the lowest value for the search, used to increment the binary search
#max --> INT, the highest value for the search, used to increment the binary search
#guess --> INT, the number that will be used to locate the index for the search (min + max) // 2 
#found --> INT, used to determine whether a sequential search was successful or not

#--IMPORTS--#

#for text file handling
import csv
#import system and name to create a clear screen function (clear())
from os import system, name 
#to randomize the goodbye message
from random import randrange

#--FUNCTIONS--#
def clear(): 
    
    '''Clears the output/screen'''

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def menu():

    '''Displays a menu to the user. Validates the user's choice before returning the choice'''

    print("\t\t SEARCH MENU")
    print("1. Search by FIRST NAME")
    print("2. Search by ID CODE")
    print("3. Search by LAST NAME")
    print("4. Search by ALLEGIANCE")
    print("5. EXIT")

    choice = input("\n\t\tPlease enter a choice from the list above >  ")

    #verify that the user input a digit (integer) so that the validation works properly
    while not choice.isdigit(): 

        print("\n\t**Input Error**")
        print("You may only enter integers (1-5)")
        choice = input("\n\t\tPlease enter a choice from the list above >  ")

    choice = int(choice)

    while choice < 1 or choice > 5:

            print("\n\t**Input Error**")
            choice = input("\nPlease enter a valid choice (1-5)> ")

            while not choice.isdigit(): 

                print("\n\t**Input Error**")
                print("You may only enter integers (1-5)")
                choice = input("\n\t\tPlease enter a choice from the list above >  ")

            choice = int(choice)

    return choice

def loop_answer():

    '''This asks the user if they want to search again and validates that a user enters a 'y' or 'n' when given the choice of [y/n]'''
    
    answer = input("\nWould you like to conduct another search? [y/n] > ").lower()
    
    while answer != "y" and answer != "n":

        print("\n\nInput Error: Please only answer only with a 'y' or 'n'")
        answer = input("\nPlease choose a valid answer: [y/n] > ").lower()
    
    return answer

def swap(n, j):

    '''This function is used for bubble sorting, n is name of list and j is the index'''

    t = n[j] #t is a temp variable used for the swap only
    n[j]= n[j + 1]
    n[j + 1] = t


def goodbye():

    '''This function prints a custom goodbye message to the user'''
    
    quotes = ["'Winter is coming.' — Ned Stark", "'You know nothing Jon Snow.' — Ygritte", "'Fear cuts deeper than swords.' — Arya Stark", "'Everything before the word \'but\' is horseshit.' — Jon Snow", "'A lion doesn’t concern himself with the opinions of a sheep.' — Tywin Lannister"]
    #will customize this later for the extra credit

    print("Goodbye")

#--MAIN EXECUTING CODE--#

#create empty lists to store data from file
code = []
lname = []
fname = []
age = []
allegiance = []

#connect to the file
with open("Week8_Labs/GOT.txt") as csvfile:

    file = csv.reader(csvfile)

    #extract data from file and append to lists
    for rec in file:

        code.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        age.append(rec[3])
        allegiance.append(rec[4])
       
#disconnected from file

#create a loop where the user can search as many times as they want

answer = "y"

while answer == "y":

    choice = menu()

    if choice == 1:#search by FIRST NAME (Bubble Sort and Binary Search)

        #bubble sort first
        for i in range(0, len(fname) - 1):#outer loop

            for index in range(0, len(fname) - 1):#inner loop

                #below if statement determines the sort
                #list used is the list being sorted
                # > is for increasing order, < for decreasing
                if(fname[index] > fname[index + 1]):
                    
                    swap(fname, index)

                    #swap all other values
                    swap(code, index)
                    swap(lname, index)
                    swap(age, index)
                    swap(allegiance, index)

        #binary search
        search = input("Please enter the FIRST NAME of the person you are searching for: ").title() 

        min = 0
        max = len(fname) - 1
        guess = (min + max) // 2

        while (min < max and search != fname[guess]):

            if search < fname[guess]:

                max = guess - 1 #search is less than middle point, so no need to consider high half of list

            else:

                min = guess + 1 #search is greater than middle point, so no need to consider low half of list

            guess = (min + max) // 2 #make sure this is not nested in if/else portion

        if search == fname[guess]:

            print(f"Your search for {search} was FOUND!")
            print(f"\n\t{'ID CODE':16}{'LAST NAME':12}\t{'FIRST NAME':12}\t{'AGE':3}\t{'ALLEGIANCE':35}")
            print(f"\t{code[guess]:16}{lname[guess]:12}\t{fname[guess]}\t\t{age[guess]:3}\t{allegiance[guess]:35}")
        
        else:
            
            print(f"Your search for {search} was *NOT FOUND*!")
            print("Please check your spelling and capitalization and try again.")

    elif choice == 2:#search by CODE (Bubble Sort and Binary Search)

        #bubble sort first
        for i in range(0, len(code) - 1):#outer loop

            for index in range(0, len(code) - 1):#inner loop

                #below if statement determines the sort
                #list used is the list being sorted
                # > is for increasing order, < for decreasing
                if(code[index] > code[index + 1]):
                    
                    swap(code, index)

                    #swap all other values
                    swap(fname, index)
                    swap(lname, index)
                    swap(age, index)
                    swap(allegiance, index)

        #binary search
        search = input("Please enter the ID CODE of the person you are searching for: ") 

        min = 0
        max = len(code) - 1
        guess = (min + max) // 2

        while (min < max and search != code[guess]):

            if search < code[guess]:

                max = guess - 1 #search is less than middle point, so no need to consider high half of list

            else:

                min = guess + 1 #search is greater than middle point, so no need to consider low half of list

            guess = (min + max) // 2 #make sure this is not nested in if/else portion

        if search == code[guess]:

            print(f"Your search for {search} was FOUND!")
            print(f"\n\t{'ID CODE':16}{'LAST NAME':12}\t{'FIRST NAME':12}\t{'AGE':3}\t{'ALLEGIANCE':35}")
            print(f"\t{code[guess]:16}{lname[guess]:12}\t{fname[guess]}\t\t{age[guess]:3}\t{allegiance[guess]:35}")
        
        else:
            
            print(f"Your search for {search} was *NOT FOUND*!")
            print("Please check your spelling and capitalization and try again.")

    elif choice == 3:#search by LAST NAME (Sequential Search)

        search = input("Please enter the LAST NAME of the person you are searching for: ").title()

        found = -1 #used for future printing of failed search attempts

        for i in range(0, len(lname)):
        
            if search == lname[i]: #search found what it was looking for

                found = i #used for print statement based on success of search
                print(f"\t{'ID CODE':16}{'LAST NAME':12}\t{'FIRST NAME':12}\t{'AGE':3}\t{'ALLEGIANCE':35}")
                print(f"\t{code[found]:16}{lname[found]:12}\t{fname[found]}\t\t{age[found]:3}\t{allegiance[found]:35}\n")

        if found == -1:

            print(f"Your search for {search} was *NOT FOUND*!")
            print("Please check your spelling and capitalization and try again.")

    elif choice == 4:#search by ALLEGIANCE (Sequential Search)

        search = input("Please enter the ALLEGIANCE of the person you are searching for: ")

        found = -1 #used for future printing of failed search attempts

        for i in range(0, len(allegiance)):
        
            if search == allegiance[i]: #search found what it was looking for

                found = i #used for print statement based on success of search
                print(f"\t{'ID CODE':16}{'LAST NAME':12}\t{'FIRST NAME':12}\t{'AGE':3}\t{'ALLEGIANCE':35}")
                print(f"\t{code[found]:16}{lname[found]:12}\t{fname[found]}\t\t{age[found]:3}\t{allegiance[found]:35}\n")

        if found == -1:

            print(f"Your search for {search} was *NOT FOUND*!")
            print("Please check your spelling and capitalization and try again.")

    else:

        answer = "n"

    if choice != 5:
            
        #allow the user to search multiple times
        answer = loop_answer()

    clear()

goodbye()