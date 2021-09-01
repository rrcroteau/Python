#Ron Croteau
#Lab 6B
#September 6, 2021
#SE126.02

#PROGRAM PROMPT: Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows.
# Row
#   1 A B  C D
#   2 A B  C D
#   3 A B  C D
#   4 A B  C D
#   5 A B  C D
#   6 A B  C D
#   7 A B  C D

# The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this:
# 
# Row
#   1 X B  C D
#   2 A X  C D
#   3 A B  C D
#   4 A B  C D
#   5 A B  C D
#   6 A B  C D
#   7 A B  C D
#After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.You must use functions that allows the user to enter the row and seat number.  The row should be asked for separately from the seat number (two inputs)
#All data displayed is correct. User is told how many iterations of the search loop were executed per search. User can search multiple times
#You must use a function that asks the user in they want to continue or stop. The function should only accept an uppercase or lowercase y or n.

#--VARIABLE DICTIONARY--#

#seatA --> LIST, STR contains all of seat A options for the rows
#seatB --> LIST, STR contains all of seat B options for the rows
#seatC --> LIST, STR contains all of seat C options for the rows
#seatD --> LIST, STR contains all of seat D options for the rows
#chosen --> LIST, STR contains all of seats the user reserved
#answer --> STR, contains the loop control answer
#row --> INT, contains the row the user wants to sit in
#seat --> STR, contains the seat the user wants to sit in


#--IMPORTS--#
#import system and name to create a clear screen function (clear())
from os import system, name 

#--FUNCTIONS--#

def clear(): 
    
    '''Clears the output/screen'''

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def seatingChart():

    '''Prints the current seating chart for the user'''

    print("\n\n\tCroteau Airways -- Flight 9021 PVD to BOS")
    print("---------------------------------------------------------")
    for i in range(len(seatA)):

        print(f"|\t\t  Row {i + 1}\t\t{seatA[i]} {seatB[i]}  \t{seatC[i]} {seatD[i]}\t\t|")

    print("---------------------------------------------------------")

def yes_no_choice(choice):

    '''This validates that a user enters a 'y' or 'n' when give the choice of [y/n]'''
    
    while choice.lower() != "y" and choice.lower() != "n":

        print("\n\nInput Error: Please only answer only with a 'y' or 'n'")
        choice = input("\nPlease choose a valid answer: [y/n] > ")
    
    return choice.lower()

def seatChoice():

    '''This get the row and seat the user wants to reserve and returns those values'''
    
    row = input("Please enter the row you would like to sit in [1-7] > ")
    
    while not row.isdigit() and (row < 1 or row > 7): 

        print("\n\t**Input Error**")
        print("\tYou may only valid row numbers [1-7]")
        row = input("\n\t\tPlease enter a valid row choice > ")

    row = (int(row) - 1) #this changes the row selection to match the list index for that row

    seat = input("\n\tEnter the seat you want to sit in [A-D] > ").upper()

    while seat != "A" and seat != "B" and seat != "C" and seat != "D":

        print("\n\t**Input Error**")
        print("\tYou may only valid seat selections [A-D]")
        seat = input("\n\tEnter the seat you want to sit in [A-D] > ").upper()


    return row, seat





#--MAIN EXECUTING CODE--#

#create the lists for the seats
seatA = ["A", "A", "A", "A", "A", "A", "A"]
seatB = ["B", "B", "B", "B", "B", "B", "B"]
seatC = ["C", "C", "C", "C", "C", "C", "C"]
seatD = ["D", "D", "D", "D", "D", "D", "D"]
chosen = [] #will store data for Extra Credit of printing all seats chosen at end of session

answer = "y" #loop control variable

#create the loop allowing user to select as many seats as they want

while answer == "y":
    #display current seating chart to user
    seatingChart()

    #get the row and seat desired by the user
    row, seat = seatChoice()


    answer = input("\nWould you like to select another seat? [y/n] > ")

    answer = yes_no_choice(answer)#validate input

    clear() #clear the screen for a cleaner UI










