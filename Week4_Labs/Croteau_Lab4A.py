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
#first_name --> LIST, STR, contains the first names of characters ( rec[0] )
#last_name --> LIST, STR, contains the last names of characters ( rec[1] )
#age --> LIST, INT, contains the ages of characters ( int(rec[2]) )
#nickname --> LIST, STR, contains the nicknames of characters ( rec[3] )
#house --> LIST, STR, contains the house allegiances of characters ( rec[4] )
#motto --> LIST, STR, contains the motto of characters based on house allegiances
#total_age --> INT, the total age of all the characters 
#avg_age --> INT, total_age / records
#stark --> INT, holds the tally of House Stark allegiance
#nights --> INT, holds the tally of Night's Watch allegiance
#tully --> INT, holds the tally of House Tully allegiance
#lannister --> INT, holds the tally of House Lannister allegiance
#baratheon --> INT, holds the tally of House Baratheon allegiance
#targaryen --> INT, holds the tally of House Targaryen allegiance

#--IMPORTS--#

#for text file handling
import csv

#--FUNCTIONS--#

#--MAIN EXECUTING CODE--#

#initialize counting variables and empty lists
records = 0
first_name = []
last_name = []
age = []
nickname = []
house = []
motto = []
total_age = 0
stark = 0
nights = 0
tully = 0
lannister = 0
baratheon = 0
targaryen = 0

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

#headers for original data
print(f"{'FIRST NAME':10}\t{'LAST NAME':10}\t{'AGE':4}\t{'NICKNAME':20}\t{'HOUSE':18}")
print("-------------------------------------------------------------------------------")

#process lists to print original data
for i in range(0, records):

    print(f"{first_name[i]:10}\t{last_name[i]:10}\t{age[i]:<4}\t{nickname[i]:20}\t{house[i]:18}")

#reprocess the lists to add the house motto [dependent on field 4, house allegiance] and print with mottos added

#headers for new data including mottos
print(f"\n\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'AGE':4}\t{'NICKNAME':20}\t{'HOUSE':18}\t{'MOTTO'}")
print("----------------------------------------------------------------------------------------------------------------")

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

    print(f"{first_name[i]:10}\t{last_name[i]:10}\t{age[i]:<4}\t{nickname[i]:20}\t{house[i]:18}\t{motto[i]}")


#reprocess the lists to find the average age then print total number of people on the list, average age, and tallies for each allegiance

for i in range(0, records):

    total_age += age[i]

    if house[i] == "House Stark":

        stark += 1

    elif house[i] == "House Baratheon":

        baratheon += 1

    elif house[i] == "House Tully":

        tully += 1

    elif house[i] == "Night's Watch":

        nights += 1

    elif house[i] == "House Lannister":

        lannister += 1

    elif house[i] == "House Targaryen":

        targaryen += 1

#determine average age
avg_age = total_age / records

print("\n\n")
print(f"THERE ARE {records} PEOPLE ON THE LIST")
print(f"THE AVERAGE AGE OF THE PEOPLE ON THE LIST IS: {avg_age:.1f}")
print(f"THE TALLIES FOR HOUSE ALLEGIANCE ARE:\n")
print(f"\tHOUSE STARK: {stark}")
print(f"\tHOUSE BARATHEON: {baratheon}")
print(f"\tHOUSE TULLY: {tully}")
print(f"\tNIGHT'S WATCH: {nights}")
print(f"\tHOUSE LANNISTER: {lannister}")
print(f"\tHOUSE TARGARYEN: {targaryen}")
