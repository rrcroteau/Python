#Name Ron Croteau
#Lab 7
#June 1, 2021
#SE116.01
#PROGRAM PROMPT: Write a program that allows the user to enter a person's first name, last name, hourly rate, hours worked, and number of dependents. The program should display the person’s full name using one variable, gross pay, net pay and amount of money that is deducted from their pay based on the number of dependents. The user should be allowed to enter as many employees as they want. Once the user has finished entering the data the program should display the total number of employees entered, total gross pay, total net pay and total amount of deductions.

#VARIABLE DICTIONARY:
#employees --> holds number of employees entered
#total_gross --> holds the total gross pay of all employees entered
#total_net --> holds the total net pay of all employees entered
#total_ded --> holds the total deductions of all employees entered
#fname --> first name of employee
#lname --> last name of employee
#hourly_rate --> hourly pay rate of employee
#hours --> hours worked by employee
#dep --> number of dependants the employee has
#name --> concatenation of fname and lname
#gross --> gross pay = hours worked * hourly pay rate
#deduction --> the amount of deductions taken from gross pay based on dependants
#net --> net pay = gross pay - deductions
#answer --> used to control the loop

#FUNCTIONS-------------------------------------------

def deduction_func(gp, dep):
    '''Employee gross pay and number of dependants are used to determine the pay deductions: returns deductions'''

    if dep == 0:

        ded_amt = gp * .1

    elif dep == 1:

        ded_amt = gp * .08

    elif dep == 2:

        ded_amt = gp * .06

    else:

        ded_amt = gp * .03

    return ded_amt 


#MAIN-----------------------------------------------------

#welcome msg
print("\n\t\t\t\tWelcome to the Payroll Calculator\n\n")

#initialize variables
employees = 0
total_gross = 0
total_net = 0
total_ded = 0
answer = "y"

#enter the loop
while answer == "y":

    #solicit employee data
    fname = input("\n\t\t\tEnter the employee's first name: > ").title()
    lname = input("\n\t\t\t Enter the employee's last name: > ").title()
    hourly_rate = float(input("\n\t\t   Enter the employee's hourly rate: > $"))
    hours = float(input("\n\t\t  Enter the employee's hours worked: > "))
    dep = int(input("\n\tEnter the number of employee dependants: > "))

    #process data
    name = f"{fname} {lname}"
    gross = hourly_rate * hours
    deduction = deduction_func(gross, dep)
    net = gross - deduction

    #increment counters
    employees += 1
    total_gross += gross
    total_net += net
    total_ded += deduction

    #output employee data
    print(f"\n\n\tName: {name} -- Gross Pay: ${gross:.2f} -- Net Pay: ${net:.2f} -- Deductions: ${deduction:.2f}")

    answer = input("\n\nDo you have another employee to enter? [y/n] > ").lower()    

#output final totals
print("\n\n\n")
print(f" Total employees entered: {employees:9}")
print(f"         Total gross pay: ${total_gross:8.2f}")
print(f"           Total net pay: ${total_net:8.2f}")
print(f"        Total deductions: ${total_ded:8.2f}")

#goodbye message
print("\n\n\tThank you for using the Payroll Calculator. Goodbye :]")







