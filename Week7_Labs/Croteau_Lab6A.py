#Ron Croteau
#Lab 6A
#September 6, 2021
#SE126.02

#PROGRAM PROMPT: Write a Python program that reads the data from the file and stores all data into appropriate lists. The program should then prompt the user for the person’s last name they are searching for and display all available information on that person if they are found.  You must use the binary search method.  The program should allow the user to search for as many people as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#--VARIABLE DICTIONARY--#

#records --> INT, holds the number of records (people) processed
#csvfile --> shorthand name for file location, full file path
#file --> friendly name for file data, after it has been passed through csv.reader()
#rec --> LIST, an individual record from the file; only used when connected to file
#lname --> LIST, STR, contains the last names
#fname --> LIST, STR, contains the first names
#dob --> LIST, STR, contains the date of birth
#answer --> STR, used to control the search loop
#search --> STR, contains the search parameter as input by the user
#search_count --> INT, contains the number of search loops conducted by the binary search 
#min --> INT, the lowest value for the search, used to increment the binary search
#max --> INT, the highest value for the search, used to increment the binary search
#guess --> INT, the number that will be used to locate the index for the search (min + max) // 2 

#--IMPORTS--#

#for text file handling
import csv

#--FUNCTIONS--#

#--MAIN EXECUTING CODE--#

#create empty lists to store data from file
lname = []
fname = []
dob = []

#initialize counters
records = 0 

#connect to the file
with open("Week7_Labs/lab6.txt") as csvfile:

    file = csv.reader(csvfile)

    #extract data from file and append to lists
    for rec in file:

        records += 1 #increment count of records

        lname.append(rec[0])
        fname.append(rec[1])
        dob.append(rec[2])
       
#disconnected from file

#create a loop where the user can search for last names as many times as they want

answer = "y"

while answer == "y":

    search = input("Please enter the LAST NAME of the person you are searching for: ").title() #matches the case of the last name in txt file

    min = 0
    max = records - 1
    guess = (min + max) // 2

    search_count = 0

    while (min < max and search != lname[guess]):

        search_count += 1

        if search < lname[guess]:

            max = guess - 1 #search is less than middle point, so no need to consider high half of list

        else:

            min = guess + 1 #search is greater than middle point, so no need to consider low half of list

        guess = (min + max) // 2 #make sure this is not nested in if/else portion

    if search == lname[guess]:

        print(f"Your search for {search} was FOUND in {search_count} loops!")
        print(f"\n\t{'LAST NAME':12}\t{'FIRST NAME':12}\t{'DOB':10}")
        print(f"\t{lname[guess]:12}\t{fname[guess]}\t\t{dob[guess]}")
    
    else:
        
        print(f"Your search for {search} was *NOT FOUND* in {search_count} loops!")
        print("Please check your spelling and capitalization and try again.")


    #allow the user to search multiple times
    answer = input("\n\nWould you like to search again? [y/n]: ").lower()

print("\n\nThank you for using the program. Goodbye!")
