#Name Ron Croteau
#Lab 3B
#April 27, 2021
#SE116.01
#PROGRAM PROMPT: Write a program that will determine the change a user will receive based on the total cost of all items purchased.  The user should be allowed to enter as many items as they want. When the user has finished entering all of their items the program should display the total amount then prompt the user for amount tendered.  Print out the total cost of all items, amount tendered and the change the user will receive. The total and change must be formatted to 2 decimal places.

#VARIABLE DICTIONARY:
#total_price --> a counter for the total price of all items entered
#item_price --> a price for the item entered
#amount_tendered--> the amount of money the user will pay with
#change --> the change the user will get back (amount_tendered - total_price)
#answer --> a variable to contain the answer of the user and control the while loop

#NOTES: Ensure to use a while loop
#----------------------------------------------------#

#welcome message
print("Welcome to the Croteau Total Price Calculator\n\n")
#initialize variables
total_price = 0 #a counter for the total price of all items entered
answer = "y" #used to enter/control flow of while loop

#enter the while loop
while answer == "y":
        
    #solicit price of item from user
    item_price = float(input("Enter the price of the item: $"))
        
    #calculate/increment total_price
    total_price += item_price

    print() #for spacing
    
    #solicit whether the user wants to enter another item
    answer = input("Would you like to enter another item? [y/n]: ").lower()
    print() #for spacing

#output total cost to user
print("Total total price of your items: ${:.2f}".format(total_price))

#solicit amount tendered from user
amount_tendered = float(input("\nHow much money will you give the cashier? $"))

#determine and output the change to the user
print("\nYour change is: ${0:.2f}".format((amount_tendered - total_price)))

#goodbye statement
print()
print("\nThank you for using the Croteau Total Price Calculator, goodbye!\n\n")