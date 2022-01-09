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
#confirm --> STR, contains the value of user confirmation on seat choice
#choice --> STR, contain the choice in certain functions, used for validation purposes 


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
    for i in range(0, 7):

        print(f"|\t\t  Row {i + 1}\t\t{seatsA[i]} {seatsB[i]}  \t{seatsC[i]} {seatsD[i]}\t\t|")

    print("---------------------------------------------------------")

def yes_no_choice():

    '''This asks the user if they want to add another seat and validates that a user enters a 'y' or 'n' when given the choice of [y/n]'''
    
    answer = input("\nWould you like to select another seat? [y/n] > ").lower()
    
    while answer != "y" and answer != "n":

        print("\n\nInput Error: Please only answer only with a 'y' or 'n'")
        answer = input("\nPlease choose a valid answer: [y/n] > ").lower()
    
    return answer

def confirmation(choice):

    '''This validates that a user enters a 'Y' or 'X' when given the choice'''
    
    while choice != "Y" and choice != "X":

        print("\n\nInput Error: Please only answer only with a 'Y' or 'X'")
        choice = input("\nPlease choose a valid answer: [Y/X] > ").upper()
    
    return choice

def seatChoice():

    '''This get the row and seat the user wants to reserve and returns those values'''
    
    row = input("Please enter the row you would like to sit in [1-7] > ")
       
    #validate the row choice contains valid input
    while not row.isdigit():

        print("\n\t**Input Error**")
        print("\tYou may only valid row numbers [1-7]")
        row = input("\n\t\tPlease enter a valid row choice > ")

    row = int(row)

    while row < 1 or row > 7:

            print("\n\t**Input Error**")
            print("\tYou may only enter valid row numbers [1-7]")
            row = input("\n\t\tPlease enter a valid row choice > ")

            while not row.isdigit(): 

                print("\n\t**Input Error**")
                print("\tYou may only valid row numbers [1-7]")
                row = input("\n\t\tPlease enter a valid row choice > ")

            row = int(row)

    seat = input("\n\tEnter the seat you want to sit in [A-D] > ").upper()

    #validate the seat choice contains valid input
    while seat != "A" and seat != "B" and seat != "C" and seat != "D":

        print("\n\t**Input Error**")
        print("\tYou may only enter valid seat selections [A-D]")
        seat = input("\n\tEnter the seat you want to sit in [A-D] > ").upper()

    #confirm seat choice with user
    confirm = input(f"\n\nYou selected seat {row}{seat}.  Confirm with 'Y'. Cancel with 'X' > ").upper()

    confirm = confirmation(confirm)

    if confirm == "X":

        row, seat = seatChoice()#allows user to select a different seat
        return row, seat

    else:
        
        row = row - 1 #aligns the row with the index of the list (Row 1 is index 0 and so on)
        return row, seat


#--MAIN EXECUTING CODE--#

#create the lists for the seats
seatsA = ["A", "A", "A", "A", "A", "A", "A"]
seatsB = ["B", "B", "B", "B", "B", "B", "B"]
seatsC = ["C", "C", "C", "C", "C", "C", "C"]
seatsD = ["D", "D", "D", "D", "D", "D", "D"]
chosen = [] #will store data for Extra Credit of printing all seats chosen at end of session

answer = "y" #loop control variable

#create the loop allowing user to select as many seats as they want

while answer == "y":
    #display current seating chart to user
    seatingChart()

    #get the row and seat desired by the user
    row, seat = seatChoice()

    if seat == "A":

        if seatsA[row] == seat:#confirms the seat is available (i.e. not an "X")

            seatsA[row] = "X" #marks this seat as taken so it cannot be chosen again
            #append the confirmed available seat to the chosen list to print all seats confirmed for extra credit
            chosen.append(f"{row + 1}{seat}")
            #print(chosen)

        else:

            print("\n\tI'm sorry, but that seat is not currently available.")

    elif seat == "B":

        if seatsB[row] == seat:#confirms the seat is available (i.e. not an "X")

            seatsB[row] = "X"#marks this seat as taken so it cannot be chosen again
            #append the confirmed available seat to the chosen list to print all seats confirmed for extra credit
            chosen.append(f"{row + 1}{seat}")

        else:

            print("\n\tI'm sorry, but that seat is not currently available.")

    elif seat == "C":

        if seatsC[row] == seat:#confirms the seat is available (i.e. not an "X")

            seatsC[row] = "X"#marks this seat as taken so it cannot be chosen again
            #append the confirmed available seat to the chosen list to print all seats confirmed for extra credit
            chosen.append(f"{row + 1}{seat}")

        else:

            print("\n\tI'm sorry, but that seat is not currently available.")

    else:

        if seatsD[row] == seat:#confirms the seat is available (i.e. not an "X")

            seatsD[row] = "X"#marks this seat as taken so it cannot be chosen again
            #append the confirmed available seat to the chosen list to print all seats confirmed for extra credit
            chosen.append(f"{row + 1}{seat}")

        else:

            print("\n\tI'm sorry, but that seat is not currently available.")

    answer = yes_no_choice()#loop control

    clear() #clear the screen for a cleaner UI

#print the seats confirmed during the session to the user (Extra Credit)
seatingChart()#one final print out of the current seating chart
print("You reserved the followed seats during this session:\n")
for i in range(0,len(chosen)):

    print(f"\tSeat {i+1}: {chosen[i]}")

input("\n\n\nPlease press ENTER to continue . . .")

#goodbye
print("\n\tThank you for choosing Croteau Airways for all your travel needs!")
