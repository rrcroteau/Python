#Ron Croteau
#Lab 3B
#August 2, 2021
#SE126.02

#PROGRAM PROMPT: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective lists, and then process the lists to determine the 5 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 5 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 5 totals.

#VARIABLE DICTIONARY:
#no_elig --> counter for individuals not eligible to register (under 18 years old)
#no_reg --> counter for individuals old enough to register but have not registered
#no_vote --> counter for individuals who registered to vote but did not vote
#vote --> counter for individuals who voted (eligible, registered, voted)
#records --> counter for # of records entered
#id_num--> 4 character ID number for the record
#age --> the age of the indivual (used to determine eligibility, must be 18+) --used to increment those not eligble
#reg --> whether or not the person registered to vote - used to increment non-registered indivuals
#voted --> whether or no the person voted - used to increment either voted or not voted

#--IMPORTS--#
import csv

#--FUNCTIONS--#

#--MAIN EXECUTING CODE--#

#initialize counter variables and empty lists
no_elig = 0
no_reg = 0
no_vote = 0
vote = 0
records = 0
id_num = []
age = []
reg = []
voted = []

with open("Week3_Labs/voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1 #increment record count
        id_num.append(rec[0])
        age.append(int(rec[1]))
        reg.append(rec[2])
        voted.append(rec[3])
#disconnected from file    
    
#determine which category the record falls into and increment record count
for i in range(0, records):
    
    if age[i] < 18:
        no_elig += 1
    
    elif reg[i] == 'N':
        no_reg += 1
  
    elif voted[i] == 'N':
        no_vote += 1
    
    else:
        vote += 1

#output data totals to the user
print("\n\n\n")
print(f"Total non-eligible persons (under 18 years old): {no_elig}")
print(f"    Total eligible persons who did not register: {no_reg}")
print(f"       Total registered voters who did not vote: {no_vote}")
print(f"              Total registered voters who voted: {vote}")
print(f"                          Total records entered: {records}")
