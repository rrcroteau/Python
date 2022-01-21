#Name Ron Croteau

#Jan 21, 2022
#PROGRAM PROMPT: Write a program that provides a menu which allows users to transform binary to decimal or decimal to binary:

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
    print("\n\n\t\tMenu")
    print("\n\t1. Decimal to Binary")
    print("\n\t2. Binary to Decimal")
    print("\n\t3. Quit")
    
    #solicit user choice to return to main program
    choice = input("\nPlease enter either 1, 2, or 3: > ")
    clear()
    return choice


#MAIN----------------------------------------------#
#initialize loop control
answer = "y"

while answer == "y":

    choice = menu()

    if choice == "1":

        
        dec = int(input("\tPlease enter the decimal number to be converted > "))

        #create an empty string with the hold the result
        bin = ""

        #save the decimal as a temp decimal to preserve the initial value for result output
        dec_temp = dec

        #create a loop to divide the decimal by 2 (because binary is a base-2 number system) to determine the appropriate bits
        while dec_temp > 0:

            #first, determine if the remainder is a 1 or 0 in order to add the appropriate bit
            if dec_temp % 2 == 1: #if there is a remainder of 1, that is the bit
                #add the bit to the string... place it first in the equation so it adds in to the left of the string, preserving what is already in the right most part of the string, if anything
                bin = "1" + bin 

            else: # the modulus would equal 0, so that is the bit
                bin = "0" + bin

            #do the actual division now to prep the decimal number for the next loop iteration
            dec_temp = int(dec_temp / 2) #cast it to an int to cut off any .5 that may result from dividing an odd number
            

        print(f"\nThe decimal {dec} converted to binary is: {bin}")
        input("\nPress enter to continue...")
        clear()

    elif choice == "2":

        bin = input("\tPlease enter the binary number to be converted > ")
        
        #strip all leading zeroes
        bin2 = bin.lstrip("0")

        #create a counting variable for the decimal
        dec = 0
        #start the bit value off at 1
        bit_value = 1
        
        #loop through the string to convert bits to decimal 
        while len(bin2) > 0:
            
            #convert to right most bit to an int and then mulitiply it by the bit value and add it to the decimal value
            dec += int(bin2[-1]) * bit_value

            #remove the right most bit off the string for the next iteration
            bin2 = bin2[:-1]

            #multiply the value of the bit by 2 (because binary is a base-2 number system)
            bit_value *= 2
        
        print(f"\n\t\tThe binary {bin} converted to decimal is: {dec:,d}") # the :,d adds the commas to the number for easier reading
        input("\nPress enter to continue...")
        clear()
    else:
        answer = "n"

print("\n\n\n\t\t\t\t\tThank you and goodbye!")