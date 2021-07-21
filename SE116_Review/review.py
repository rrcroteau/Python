#Ron Croteau
#SE116 Review
#July 21, 2021

#PROGRAM PROMPT:  This is a temperature conversion program. It allows a user to enter as many Fahrenheit temps as they would like.  It then converts it to Celsius and displays it.  It also counts the number of temps entered and the average temps.

#VARIABLE DICTIONARY
#temp_count - holds the total count of temperatures added by the user
#temp_total - sum total of all temps entered
#avg_temp - avg of all temps entered (avg_temp = temp_total / temp_count)
#tempF - temp in Fahrenheit, entered by user
#tempC - temp in Celsius, calculated by program and displayed to user (tempF - 32 * (5 / 9))
#answer - loop control

#------IMPORTS--------------------------------------------------------------------------

#------FUNCTIONS------------------------------------------------------------------------

#------MAIN EXECUTING CODE--------------------------------------------------------------


temp_count = 0
temp_total = 0

answer = "y"

while answer == "y" or answer == "Y":

    tem
    pF = float(input("\n\n\t\tPlease enter the temperature in Fahrenheit: > "))

    tempC = (tempF - 32) * (5 / 9)

    temp_count += 1
    temp_total += tempF

    print(f"\n\t\tTEMP# {temp_count}\tTEMP {tempF:.1f}F = TEMP {tempC:.1f}C")

    answer = input("\n\n\t\tWould you like to enter another temperature? [y / n]")

avg_tempF = temp_total / temp_count

avg_tempC = (avg_tempF - 32) * (5 / 9)

print("\n\t\tHere is your final session information: ")
print("\t\tTOTAL TEMPS ENTERED: {0}".format(temp_count))
print("\t\tAVERAGE TEMP {0:.1f}F | {1:.1f}C".format(avg_tempF, avg_tempC))

print("\n\n\t\tThanks for using the program. Goodbye!\n\n")


