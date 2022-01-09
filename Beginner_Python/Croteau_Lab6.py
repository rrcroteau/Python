#Name Ron Croteau
#Lab 6
#May 24, 2021
#SE116.01
#PROGRAM PROMPT: Write a program that gives the user the following options:
#My Basic Calculator
# 1.   Add two numbers
# 2.   Subtract two numbers
# 3.   Multiply two numbers
# 4.   Divide two numbers
# 5.   Exit
# You must have a function for the following:
# A function for option 1
#   oThis function should return an integer.
#   oThe function should ask the user for the two integers that are to be added and return the answer to the main code.
# A function for option 2
#   oThis function should return an integer.
#   oThe function should ask the user for the two integers that are to be subtracted and return the answer to main.
# A function for option 3
#   oThis function should not have a return value.
#   oThe function should be sent the two integers to be multiplied.
#   oThe function should display the answer
# A function for option 4
#   oThis function should return a float
#   oThe function should ask the user for the two integers that are to be divided and return the answer to main
# The program must not end until the user selects option 5. 
# When designing your program assume that the user will always enter the correct menu choice. 

#VARIABLE DICTIONARY:
#answer --> controls the loop for the calculator
#num1 --> holds the first integer supplied by the use for mathematical processing
#num2 --> holds the first integer supplied by the use for mathematical processing
#choice --> the menu choice the user made

#NOTES: ***Extra Credit +5:  Build a function that displays the menu to the user and returns the user's choice to the main program.
#----------------------------------------------------#

#IMPORTS---------------------------------------------#
from os import system, name

#FUNCTIONS-------------------------------------------#
 
def clear(): 
    '''Clears the output screen'''
    #for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    #for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def menu():
    '''Presents the menu to the user'''
    print("\n\n\t\t\tMy Basic Calculator: ")
    print("\n\t1. Add two numbers")
    print("\n\t2. Subtract two numbers")
    print("\n\t3. Multiply two numbers")
    print("\n\t4. Divide two numbers")
    print("\n\t5. Exit")
    
    #solicit user choice to return to main program
    choice = input("\nPlease enter either 1, 2, 3, 4, or 5: > ")
    clear()
    return choice

def add():
    '''Finds and returns the sum of two integers'''
    num1 = int(input("\n\tEnter the first number to add to: > "))
    num2 = int(input("\n\tEnter the second number: > "))
    sum_ = num1 + num2

    return sum_

def sub():
    '''Finds and returns the difference of two integers'''
    num1 = int(input("\n\tEnter the first number to subtract from: > "))
    num2 = int(input("\n\tEnter the second number: > "))
    diff= num1 - num2

    return diff

def mult(n1, n2):
    '''Finds the product of two integer arguments and outputs product to user'''
    print(f"\nThe product of your numbers is {n1 * n2}")

def div():
    '''Finds the quotient of two integers and returns a float'''
    num1 = int(input("\n\tEnter the first number to divide from: > "))
    num2 = int(input("\n\tEnter the second number (*Note -- this cannot be a 0): > "))
    
    #avoids ZeroDivisionError from stopping the program
    try:

        quotient= num1 / num2
        return quotient

    except ZeroDivisionError:
        print("\nYou cannot divide by 0")
    

#initialize starting variables
answer = "y"

while answer == "y":

    choice = menu()

    if choice == "1":

        sum_ = add()
        print(f"\nThe sum of your numbers is: {sum_}")

    elif choice == "2":

        diff = sub()
        print(f"\nThe difference of your numbers is: {diff}")

    elif choice == "3":
        
        num1 = int(input("\n\tEnter the first number to multiply: > "))
        num2 = int(input("\n\tEnter the second number: > "))
        mult(num1, num2)


    elif choice == "4":
        
        quotient = div()
        
        #avoids printing quotient when user enters 0 as divisor and exception is handled
        if quotient != None:

            print(f"\nThe quotient of your numbers is: {quotient}")

    else:
        answer = "n"

print("\n\n\n\t\t\t\t\tThank you and goodbye!")

