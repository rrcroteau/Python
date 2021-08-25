#Ron Croteau
#Lab 5B
#August 28, 2021
#SE126.02

#PROGRAM PROMPT: Re-write lab 5A but instead of searching for a person’s name, search for their birthday.  If the person is found, reprint their entire record to the console.  The program should allow the user to search for as many birthdays as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#Extra Credit +10 points: print the user the found person, their data, along with their current age. 

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
#curr_month - INT, contains the current month
#curr_day - INT, contains the current day
#curr_year - INT, contains the current year
#split_dob - LIST, contains the dob split into day, month, and year
#birth_month - INT, contains the birth month
#birth_day - INT, contains the birth day of month 
#birth_year - INT, contains the year of birth  
#age - INT, the current age of the person searched  

#--IMPORTS--#

#for text file handling
import csv

#--FUNCTIONS--#

#--MAIN EXECUTING CODE--#

#create empty lists to store data from file
lname = []
fname = []
dob = []

#set the current day of the year for age determination (extra credit)
curr_month = 8
curr_day = 28
curr_year = 2021

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

    search = input("Please enter the DATE OF BIRTH of the person you are searching for: MM/DD/YYYY >")

    found = -1 #used for future printing of failed search attempts

    for i in range(0, records):

        search_count += 1 #increment the number of records searched
    
        if search == dob[i]: #search found what it was looking for

            found = i #used for print statement based on success of search
    
    print("\n\nSequential Search complete.\n")
    print(f"The search looked through {search_count} records.\n\n")

    search_count = 0 #reset the search counter for future searches

    if found != -1:

        #determine age for extra credit    
        split_dob = dob[found].split("/") #splits DOB in month/day/year

        birth_month = int(split_dob[0])
        birth_day = int(split_dob[1])
        birth_year = int(split_dob[2])

        if birth_month < curr_month or (birth_month == curr_month and birth_day <= curr_day):

            age = curr_year - birth_year

        else:

            age = (curr_year - birth_year) - 1
        
        print(f"We have FOUND {search} at INDEX: {found}")
        print(f"\n\t{'LAST NAME':12}\t{'FIRST NAME':12}\t{'DOB':10}\t{'AGE'}")
        print(f"\t{lname[found]:12}\t{fname[found]}\t\t{dob[found]}\t{age}")

    else:

        print(f"Your search for {search} has NOT been found")

    answer = input("\n\nWould you like to search for another date of birth? [y/n] > ")

print("\n\nThank you for using the program. Goodbye!")
