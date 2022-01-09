#Name Ron Croteau
#Lab 3A
#April 27, 2021
#SE116.01
#PROGRAM PROMPT: Write an employee wage program.  This program will be similar to lab 2A, but you will also include a loop and total counters.  This program should ask an employer (the user of the program) to enter an employee’s name, hours worked in a week, and hourly wage.  After this data has been input into the program, print to the user the employee’s name, gross pay for one week, taxes due for one week (use 20%), and this employee’s net pay.  Then, allow the user to enter a new employee’s information by asking if they would like to.  If the user does have another employee to enter, repeat the process above.  When the user decides they no longer have data to enter, print to them the total number of employees entered during the program session and the total gross pay for the week.  Also include the total tax amounts and the total net pay for all employees. All money should be format rounded to the second decimal place and clearly labeled.  All money should have decimals in alignment with one another. 

#VARIABLE DICTIONARY:
#employees --> a counter for the number of employees entered into program
#total_gross --> a counter for the total gross pay of all employees entered
#total_tax --> a counter for the total taxes paid by all of employees entered
#totel_net --> a counter for the total net pay of all employees entered
#answer --> a variable to contain the answer of the user and control the while loop
#emp_name --> name of the employee being currently entered
#hourly_rate --> hourly pay
#hrs--> hours worked in the week
#tax_rate --> the amount of taxes applied to the pay
#gross_pay --> hourly rate times total hours worked
#tax_amount --> gross pay times the tax amount (i.e. taxes paid)
#net_pay --> gross pay minus the taxes
#NOTES: Ensure to use a while loop
#----------------------------------------------------
#welcome message
print("Welcome to the Croteau Pay Calculator\n\n")
#initialize variables
tax_rate = .2 #20% as stated in the program prompt
employees = 0 #num of employees entered
total_gross = 0 #counter for gross pay
total_tax = 0 #counter for taxes paid
total_net = 0 #counter for net pay
answer = "y" #used to enter/control flow of while loop

#enter the while loop
while answer == "y":
    employees += 1 #increment the employee count
    
    #solicit name, hours, and hourly rate from user
    emp_name = input("Please enter the name of the employee: ").title()
    hrs = float(input("Enter number of hours worked for this employee: "))
    hourly_rate = float(input("Enter your hourly wage rate: $"))
    
    #calculate gross pay, taxes, net pay
    gross_pay = hourly_rate * hrs
    tax_amount = gross_pay * tax_rate
    net_pay = gross_pay - tax_amount
    
    #increment the counters needed for end of program output
    total_gross += gross_pay
    total_tax += tax_amount
    total_net += net_pay

    print() #for spacing
    #output the employee name, gross pay, taxes, and net pay
    print("Employee Name:\t",emp_name)
    print("Gross Pay:\t\t ${0:8.2f}".format(gross_pay))
    print("Tax Amount:\t\t-${0:8.2f}".format(tax_amount))
    #visual line added to seperate gross and net pay figures
    print("--------------------------")
    print("Net Pay:\t\t ${0:8.2f}".format(net_pay))

    print() #for spacing
    #solicit whether the user wants to enter another employee
    answer = input("Would you like to enter another employee [y/n]: ").lower()
    print() #for spacing

print("\nTotal number of employees:\t\t\t  {:10}".format(employees))
print("Total gross pay for the week:\t\t ${0:10.2f}".format(total_gross))
print("Total taxes paid for the week:\t\t ${0:10.2f}".format(total_tax))
print("Total net pay for the week:\t\t\t ${0:10.2f}".format(total_net))
print("\n\n")
#goodbye statement
print("Thank you for using the Croteau Pay Calculator, goodbye!\n\n")