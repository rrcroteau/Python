#Ron Croteau
#Lab 2B
#July 28, 2021

#PROGRAM PROMPT: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output.  The last line should print the number of computers in the file.

#VARIABLE DICTIONARY
#total - total num of computers
#c_type - type of computer (desktop or laptop)
#brand - brand of computer
#cpu - computer CPU (central processing unit)
#ram - computer RAM (random access memory)
#disk1 - size of 1st HDD (hard disk drive)
#numHDD - number of computer HDD
#disk2 - size of 2nd HDD (if present)
#opsys - computer OS (operating system)
#yr - computer year
#csvfile - lab2b.csv file containing computer information
#file = local variable csvfile is saved to with .reader method

#--IMPORTS--#
import csv

#--FUNCTIONS--#

#--MAIN EXECUTING CODE--#
total = 0

#print headers
print(f"{'Type':10}{'Brand':10}{'CPU':8}{'RAM':5}{'1st Disk':10}{'No HDD':10}{'2nd Disk':10}{'OS':5}{'YR':5}")

#connect to file location
with open("Week2_Labs/lab2b.csv") as csvfile:

    #use the reader method to save to local variable
    file = csv.reader(csvfile)

    #use a for loop to iterate through file
    for rec in file:
        
        #increment counting var
        total += 1
        #initialize field names from rec (using logic where necessary)
        if rec[0] == "D":
            
            c_type = "Desktop"

        else:

            c_type = "Laptop"

        #print(f"{c_type}")

        if rec[1] == "DL":

            brand = "Dell"

        elif rec[1] == "GW":

            brand = "Gateway"

        else:

            brand = rec[1] 
        #print(f"{brand}")
        cpu = rec[2]
        #print(cpu)
        ram = rec[3]
        #print(ram)
        disk1 = rec[4]
        #print(disk1)
        numHDD = rec[5]
        #print(numHDD)

        #logic based on whether there are 1 or 2 HDD in the computer
        if numHDD == "1":

            disk2 = ""
            opsys = rec[6]
            yr = rec[7]

        else:
            
            disk2 = rec[6]
            opsys = rec[7]
            yr = rec[8]

        print(f"{c_type:10}{brand:10}{cpu:8}{ram:5}{disk1:10}{numHDD:10}{disk2:10}{opsys:5}{yr:5}")

print(f"\n\nThe total number of computers is {total}") 
    
           



        





