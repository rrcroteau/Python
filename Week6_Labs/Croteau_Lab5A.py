#Ron Croteau
#Lab 5A
#August 28, 2021
#SE126.02

#PROGRAM PROMPT: Write a Python program that reads the data from the file and stores all data into appropriate lists. The program should then prompt the user for the person’s last name they are searching for and display all available information on that person if they are found.  You must use the sequential search.  The program should allow the user to search for as many people as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#--VARIABLE DICTIONARY--#

#records --> INT, holds the number of records (people) processed
#csvfile --> shorthand name for file location, full file path
#file --> friendly name for file data, after it has been passed through csv.reader()
#rec --> LIST, an individual record from the file; only used when connected to file
#lname - LIST, STR, contains the last names
#fname - LIST, STR, contains the first names
#dob - LIST, STR, contains the date of birth
#answer - STR, used to control the search loop
#search - STR, contains the search parameter as input by the user
#found - INT, used for determining if a record has been found and then the index where found is set as the value
#search_count - INT, contains the number of searches conducted by the sequential search 

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
search_count = 0

#connect to the file
with open("Week6_Labs/lab5_updated.txt") as csvfile:

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

while answer.lower() == "y":

    search = input("Please enter the LAST NAME of the person you are searching for: ").title()

    found = -1 #used for future printing of failed search attempts

    for i in range(0, records):

        search_count += 1 #increment the number of records searched
    
        if search == lname[i]: #search found what it was looking for

            found = i #used for print statement based on success of search
    
    print("\n\nSequential Search complete.\n")
    print(f"The search looked through {search_count} records.\n\n")

    search_count = 0 #reset the search counter for future searches

    if found != -1:

        print(f"We have FOUND {search} at INDEX: {found}")
        print(f"\n\t{'LAST NAME':12}\t{'FIRST NAME':12}\t{'DOB':10}")
        print(f"\t{lname[found]:12}\t{fname[found]}\t\t{dob[found]}")

    else:

        print(f"Your search for {search} has NOT been found")

    answer = input("\n\nWould you like to search for another name? [y/n] > ")

print("\n\nThank you for using the program. Goodbye!")
