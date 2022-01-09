#Ron Croteau
#Lab 3A
#August 2, 2021

#PROGRAM PROMPT: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2B) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

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
#old_dtop = number of desktops from year 16 and earlier (need replacing)
#old_ltop = number of desktops from year 16 and earlier (need replacing)
#csvfile - lab3a.csv file containing computer information
#file = local variable csvfile is saved to with .reader method

#--IMPORTS--#
import csv

#--FUNCTIONS--#

#--MAIN EXECUTING CODE--#
total = 0

#create empty lists to store csv values
c_type = []
brand = []
cpu = []
ram = []
disk1 = []
numHDD = []
disk2 = []
opsys = []
yr = []



#print headers
print(f"{'Type':10}{'Brand':10}{'CPU':8}{'RAM':5}{'1st Disk':10}{'No HDD':10}{'2nd Disk':10}{'OS':5}{'YR':5}")
print("----------------------------------------------------------------------")

#connect to file location
with open("Week3_Labs/lab3a.csv") as csvfile:

    #use the reader method to save to local variable
    file = csv.reader(csvfile)

    #use a for loop to iterate through file
    for rec in file:
        
        #increment counting var
        total += 1
        #initialize field names from rec (using logic where necessary)
        if rec[0] == "D":
            
            c_type.append("Desktop")

        else:

            c_type.append("Laptop")

        if rec[1] == "DL":

            brand.append("Dell")

        elif rec[1] == "GW":

            brand.append("Gateway")

        else:

            brand.append(rec[1]) 
        
        cpu.append(rec[2])
        
        ram.append(rec[3])
        
        disk1.append(rec[4])
      
        numHDD.append(rec[5])
        
        #logic based on whether there are 1 or 2 HDD in the computer
        if rec[5] == "1":

            disk2.append(" ")
            opsys.append(rec[6])
            yr.append(int(rec[7]))

        else:
            
            disk2.append(rec[6])
            opsys.append(rec[7])
            yr.append(int(rec[8]))

for i in range(0, total):

    print(f"{c_type[i]:10}{brand[i]:10}{cpu[i]:8}{ram[i]:5}{disk1[i]:10}{numHDD[i]:10}{disk2[i]:10}{opsys[i]:5}{yr[i]:<5}")

print(f"\n\nThe total number of computers is {total}") 


#create variables to store number of computers that need replacing(yr<=16)
old_dtop = 0
old_ltop = 0

#process list to find out which computers need to be replaced
for i in range(0, total):

    if c_type[i] == "Desktop" and yr[i] <= 16:

        old_dtop += 1

    elif c_type[i] == "Laptop" and yr[i] <= 16:

        old_ltop += 1

#print(old_dtop, old_ltop)

#output the number of each to be replaced and the $ amount
print(f"\n\n\t{old_dtop} desktops must be replaced at a cost of ${(old_dtop * 2000):,.2f}")

print(f"\t{old_ltop} laptops must be replaced at a cost of ${(old_ltop * 1500):,.2f}")

input("\n\nPress any key to continue . . . ")

    
           



        





