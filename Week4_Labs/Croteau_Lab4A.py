#Ron Croteau
#Lab 4A
#August 9, 2021
#SE126.02

#PROGRAM PROMPT: In Python, process the text file “lab4A_GOT_NEW.txt” to store each field into its own corresponding list:
# FIELD0    FIELD1      FIELD2  FIELD3      FIELD4      
# Firstname Lastname    Age     Nickname    House Allegiance
# Then:Process the lists to print them as they appear in the fileRe-process the lists to add the House Motto (dependent on Field4/Allegiance)oRe-Process the lists to print each record fully with the House MottosRe-process the lists to find the average age within the list, then Print the total number of people in the listoPrint the average ageoPrint tallies for each allegiance (Field4)

#VARIABLE DICTIONARY:
#records --> holds the number of records (people) processed
#csvfile --> shorthand name for file location, full file path
#file --> friendly name for file data, after it has been passed through csv.reader()
#rec --> LIST, an individual record from the file; only used when connected to file
#first_name --> LIST, contains the first names of characters ( rec[0] )
#last_name --> LIST, contains the last names of characters ( rec[1] )
#age --> LIST, contains the ages of characters ( int(rec[2]) )
#nickname --> LIST, contains the nicknames of characters ( rec[3] )
#house --> LIST, contains the house allegiances of characters ( rec[4] )
#motto --> LIST, contains the motto of characters based on house allegiances
#total_age --> the total age of all the characters 
#avg_age --> total_age / records
#stark --> holds the tally of House Stark allegiance
#nights --> holds the tally of Night's Watch allegiance
#tully --> holds the tally of House Tully allegiance
#lannister --> holds the tally of House Lannister allegiance
#baratheon --> holds the tally of House Baratheon allegiance
#targaryen --> holds the tally of House Targaryen allegiance

#--IMPORTS--#
import csv

#--FUNCTIONS--#

#--MAIN EXECUTING CODE--#

