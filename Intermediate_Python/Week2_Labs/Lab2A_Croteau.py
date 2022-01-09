#Ron Croteau
#Lab 2A
#July 28, 2021

#PROGRAM PROMPT: The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event.  Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#VARIABLE DICTIONARY
#name - name of the room
#max_cap - max capacity of the room
#people - number of registered people attending
#diff - the difference between capacity and attendees (max_cap - attendees)
#total_records - total number of records processed
#rooms_over - total number of room over capacity
#csvfile - lab2a.csv file containing room information
#file = local variable csvfile is saved to with .reader method

#--IMPORTS--#
import csv

#--FUNCTIONS--#

#--MAIN EXECUTING CODE--#
total_records = 0
rooms_over = 0

#print headers
print(f"{'Room':20}\t{'Max':3}\t{'Min':3}\t{' Over':4}")

#connect to file location
with open("Week2_Labs/lab2a.csv") as csvfile:

    #use the reader method to save to local variable
    file = csv.reader(csvfile)

    #use a for loop to iterate through file
    for rec in file:

        #update totaling var
        total_records += 1

        #initialize field names from rec
        name = rec[0]
        max_cap = int(rec[1])
        people = int(rec[2])
        diff = max_cap - people

        #determine which rooms are over cap and output to terminal
        if diff <0:
            
            rooms_over += 1
            print(f"{name:20}\t{max_cap:3}\t{people:3}\t{abs(diff):4}")

#display totalling vars
print(f"\n\nProcessed {total_records} records")
print(f"There are {rooms_over} rooms over the limit")

input("\nPress any key to continue . . .")



