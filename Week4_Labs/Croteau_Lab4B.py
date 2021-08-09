#Ron Croteau
#Lab 4B
#August 9, 2021
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