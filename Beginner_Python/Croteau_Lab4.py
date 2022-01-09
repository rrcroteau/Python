#Name Ron Croteau
#Lab 4
#May 7, 2021
#SE116.01
#PROGRAM PROMPT: Write a program that will determine the change a user will receive based on the total cost of all items they want to purchase. The user should be able to enter as many items as they want. After a user enters an item’s cost, also ask them if this item will be taxed. If the item will be taxed, calculate the taxable amount. The user should be able to use either a y or a Y to re-enter the loop and add another item cost as well as to signal that the current item they have entered is taxable. When the user has finished entering all of their items the program should display: the total number of items purchased, the total cost of all items, the total taxable amount of taxed items, and the final total due (cost + tax). Once all of the values are printed, prompt the user for the amount tendered (money they are paying with). Then, redisplay the final total cost of all items, the amount tendered, and the change the user will receive. All monetary values must be formatted to display to the 2nd decimal place and all decimals should align on top of one another when displayed (following the format of a physical receipt). 

#VARIABLE DICTIONARY:
#sub_total --> a counter for the total price of all items entered (without tax added)
#total_tax --> a counter for the total tax of all items that are taxable
#total_items --> a counter for the total number of items entered by the user
#item_price --> a price for the item entered
#total_price --> the total the customer plays - sub_total + total_tax
#amount_tendered--> the amount of money the user will pay with
#change --> the change the user will get back (amount_tendered - total_price)
#answer --> a variable to contain the answer of the user and control the while loop

#NOTES: Ensure loop/if statement accepts 'y' or 'Y'
        #use 7% for the tax
#----------------------------------------------------#

#welcome message
print("Welcome to the Croteau Shopping Receipt Simulator\n\n")
#initialize variables
sub_total = 0 #a counter for the total price of all items entered
total_tax = 0 #a counter for the total tax of all items that are taxable
total_items = 0 #a counter for the total number of items entered by the user
answer = "y" #used to enter/control flow of while loop

#enter the while loop
while answer == "y" or answer == "Y": #allows user to use upper or lower case
        
    #solicit price of item from user
    item_price = float(input("Enter the price of the item: $"))

    #increment total_items
    total_items += 1

    #increment total_price 
    sub_total += item_price

    print() #for spacing

    #solicit whether item is taxable
    taxable = input("Is this item taxable? [y/n]: ")

    #if loop which adds tax if the item is taxable
    if taxable == "y" or taxable == "Y":
        total_tax += item_price * .07

    print() #for spacing
    
    #solicit whether the user wants to enter another item
    answer = input("Would you like to enter another item? [y/n]: ")
    
    print() #for spacing

#output total_items to user
print(f"\n\nTotal items purchased: {total_items}\n")

#output sub_total to user
print(f"Sub-total:\t\t\t ${sub_total:8.2f}")

#output total_tax to user
print(f"Total Tax:\t\t\t+${total_tax:8.2f}")

total_price = sub_total + total_tax #calculates the total amount owed

#output total price to user
print("------------------------------")
print(f"Total Cost:\t\t\t ${total_price:8.2f}")

#solicit amount tendered from user
amount_tendered = float(input("\nHow much money will you give the cashier? $"))
change = amount_tendered - total_price
#redisplay the final total cost of all items, the amount tendered, and the change the user will receive
print("\n\n")
print(f"Amount tendered:\t ${amount_tendered:8.2f}")
print(f"Total Cost:\t\t\t-${total_price:8.2f}")
print("------------------------------")
print(f"Change:\t\t\t\t ${change:8.2f}")#just trying some new techniques

#goodbye statement
print()
print("\nThank you for using the Croteau Shopping Receipt Simulator, goodbye!\n\n")