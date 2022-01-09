#Name Ron Croteau
#Lab 5A
#May 16, 2021
#SE116.01
#PROGRAM PROMPT: Construct a program that will analyze potential voters.The program should generate the following totals:
#1.Number of individuals not eligible to register.
#2.Number of individuals who are old enough to vote but have not registered. 
#3. Number of individuals who are eligible to vote but did not vote. 
#4. Number of individuals who did vote. 
#5. Number of records processed.The program must prompt the user for the ID number,age, if the person is registered to vote, andif the person voted. 
#You will also have to prompt to see if the user has more data to enter. All input() variables should be entered as string values. ID Number is 4 characters Age is a number Registered is either an N or a Y Votes is either anN or a Y 

#VARIABLE DICTIONARY:
#no_elig --> counter for individuals not eligible to register (under 18 years old)
#no_reg --> counter for individuals old enough to register but have not registered
#no_vote --> counter for individuals who registered to vote but did not vote
#vote --> counter for individuals who voted (eligible, registered, voted)
#records --> counter for # of records entered
#answer --> used for flow control
#id_num--> 4 character ID number for the record
#age --> the age of the indivual (used to determine eligibility, must be 18+) --used to increment those not eligble
#reg --> whether or not the person registered to vote - used to increment non-registered indivuals
#voted --> whether or no the person voted - used to increment either voted or not voted

#NOTES: validate user input
#----------------------------------------------------#

#initialize counter variables and initial loop control
no_elig = 0
no_reg = 0
no_vote = 0
vote = 0
records = 0
answer = "Y"

#welcome
print("\n\n\t\tWelcome to the Voter Records Input Module")

while answer == "Y":
    #get id number of record
    id_num = input("\nPlease enter the 4 digit ID Number of the record: > ") 
    #validate input
    while len(id_num) != 4:
        id_num = input("\nThe ID Number must be 4 digits long\nPlease check the data and enter the ID Number again: > ")

    #get age
    age = input("\nPlease enter the person's age: > ")
    #validate input
    while not age.isdigit():
        age = input("\nPlease only use numbers to indicate the age\nPlease enter the person's age: > ")

    #get whether registered or not
    reg = input("\nDid the person register to vote? [Y/N] > ")
    #validate input
    while reg != 'Y' and reg != 'N':
        reg = input("\nPlease enter only Y or N as your answer (capitalized)\nDid the person register vote? [Y/N] > ")

    #get whether voted or not
    voted = input("\nDid the person vote? [Y/N] > ")
    #validate input
    while voted != 'Y' and voted != 'N':
        voted = input("\nPlease enter only Y or N as your answer (capitalized)\nDid the person vote? [Y/N] > ")
    
    #determine which category the record falls into and increment record count
    age = int(age)
    if age < 18:
        no_elig += 1
        records += 1
    
    elif reg == 'N':
        no_reg += 1
        records += 1

    elif voted == 'N':
        no_vote += 1
        records += 1

    else:
        vote += 1
        records += 1 
    
    #determine if there is another record to enter
    answer = input("\nDo you have another record to enter? [Y/N] > ")
    #validate input
    while answer != 'Y' and answer != 'N':
        answer = input("\nPlease enter only Y or N as your answer (capitalized)\nDo you have another record to enter? [Y/N] > ")

#output data totals to the user
print("\n----------------------------------------------------------")
print(f"Total non-eligible persons (under 18 years old): {no_elig}")
print(f"    Total eligible persons who did not register: {no_reg}")
print(f"       Total registered voters who did not vote: {no_vote}")
print(f"              Total registered voters who voted: {vote}")
print(f"                          Total records entered: {records}")

#goodbye
print("\n\n\tThank you for using the Voter Records Input Module, thank you!\n")