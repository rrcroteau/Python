#Ron Croteau
#Lab 1A
#July 21, 2021

#PROGRAM PROMPT:  Write a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend.  If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations.  The user should be allowed to enter as many rooms as the want. 

#VARIABLE DICTIONARY
#max_cap - max capacity of the room
#attendees - number of registered attendees
#diff - the difference between capacity and attendees (max_cap - attendees)
#answer - loop control

#------IMPORTS--------------------------------------------------------------------------

#------FUNCTIONS------------------------------------------------------------------------

#------MAIN EXECUTING CODE--------------------------------------------------------------

answer = "y" 

print("\n\n\tWelcome to the Room Capacity Fire Code Validator")

#enter the loop
while answer == "y":

    #solicit capacity of room
    max_cap = int(input("\n\tPlease enter the maximum capacity of the room > "))
    
    #solicity number of registered attendees
    attendees = int(input("\n\tPlease enter the number of registered attendees > "))
    
    #determine the difference in the capacity and registered attendees
    diff = max_cap - attendees

    #output whether more people can continue to register or if attendance must be curtailed based on a positive(even) or negative difference
    if diff >=0:

        print(f"\n\tThe meeting is able to be held in this room. {diff} more people are able to register for the meeting.")

    else:
        
        print(f"\n\tThe meeting is unable to be held in this room. {abs(diff)} people must be informed they cannot attend the event.")





    answer = input("\n\nWould you like to validate another room? [y/n] ")

print("\n\t\t\tThank you for using the validator!")

