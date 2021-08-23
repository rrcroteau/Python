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
#bday - LIST, STR, contains the birthdays
#search - STR, contains the search parameter as input by the user
#searches - INT, contains the number of searches conducted by the sequential search 

#--IMPORTS--#

#for text file handling
import csv

#--FUNCTIONS--#

#--MAIN EXECUTING CODE--#

#create empty lists to store data from file
lname = []
fname = []
color = []

#initialize counters
records = 0 
search_count = 0