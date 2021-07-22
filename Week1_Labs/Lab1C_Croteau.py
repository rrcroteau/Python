#Ron Croteau
#Lab 1B
#July 21, 2021

#PROGRAM PROMPT:  Rewrite Lab #1A using functions.  You must have the following functions:A.  A function that asks the user for the maximum capacity of the rooms and returns that value.Use capacity for the name of the function.B.  A function that asks the user for the number of people (attendees) attending the conference and returns that value. Use attendees for the name of the function.C.  A function that accepts/is passed the values returned by the functions capacity and attendees and returns the difference between the room capacity and the attendees. Use register for the name of the function.D.  A function that prompts the user to see if they want to check anymore rooms. This function should only return if the user selects a lower/uppercase selects a lower/uppercase y or n.The main part of the program should determine whether the meeting can be held. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations.

#VARIABLE DICTIONARY
#max_cap - max capacity of the room
#people - number of registered attendees
#diff - the difference between capacity and attendees (max_cap - attendees)
#answer - loop control

#------IMPORTS--------------------------------------------------------------------------

def capacity():
   
    '''Asks the user for the maximum capacity of the rooms and returns that value'''

    cap = int(input("\n\tPlease enter the maximum capacity of the room > "))

    return cap

def attendees():
 
    '''Asks the user for the number of people (attendees) attending the conference and returns that value'''

    people = int(input("\n\tPlease enter the number of registered attendees > "))

    return people

def register(c, p):

    '''Passed the values returned by the functions capacity (c) and attendees (p) then returns the difference between the room capacity and the attendees'''

    diff = c - p #capacity and people attending

    return diff

def again():

    '''Prompts the user to see if they want to check anymore rooms. Only return if the user selects a lower/uppercase y or n'''

    answer = input("\n\nWould you like to validate another room? [y/n] ").lower() #forces the answer to lower

    #user trap to ensure only "y" or "n" is input by the user (It is already forced to lowercase due to the .lower() on the previous line)
    while answer != "y" and answer != "n":
        
        print("\n***INVALID ENTRY***")
        answer = input("\nWould you like to validate another room? [y/n] ").lower()

    return answer

#------FUNCTIONS------------------------------------------------------------------------

#------MAIN EXECUTING CODE--------------------------------------------------------------

answer = "y" 

print("\n\n\tWelcome to the Room Capacity Fire Code Validator")

#enter the loop
while answer == "y":

    #solicit capacity of room
    max_cap = capacity()
    
    #solicit number of registered attendees
    people = attendees()
    
    #determine the difference in the capacity and registered attendees
    diff = register(max_cap, people)

    #output whether more people can continue to register or if attendance must be curtailed based on a positive(even) or negative difference
    if diff >=0:

        print(f"\n\tThe meeting is able to be held in this room. {diff} more people are able to register for the meeting.")

    else:
        
        print(f"\n\tThe meeting is unable to be held in this room. {abs(diff)} people must be informed they cannot attend the event.")

    answer = again()
    

print("\n\t\t\tThank you for using the validator!")

