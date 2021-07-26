#FUNCTION PRACTICE

#PROMPT: Edit the program below to utilize the multi() anywhere you are multiplying two numbers. Solution will be available W2D2

#FUNCTIONS---------------------------------------------------------------------------

def multi(x,y):

    product = x * y

    return product

#BASE PROGRAM CODE-------------------------------------------------------------------

tax = .28
total_gross = 0
total_employees = 0

answer = "y"

while answer == "y" or answer == "Y":

    hrly_rate = float(input("\nEnter your hourly rate: "))
    hours = float(input("\nEnter your hours worked: "))

    #calculate gross pay; all other values are dependent on it
    #gross = hrly_rate * hours
    gross = multi(hrly_rate, hours)
    
    #updates total_gross & total_employees
    total_gross += gross
    total_employees += 1

    #calculate tax_amount this pay period
    #tax_amount = gross * tax
    tax_amount = multi(gross, tax)

    #calculate net pay
    net = gross - tax_amount

    #print to user
    print("\nEMPLOYEE #{0} \tGROSS ${1:.2f} \tTAXES ${2:.2f} \tNET ${3:.2f}".format(total_employees, gross, tax_amount, net))

    answer = input("\nWould you like to enter another employee? [y/n]: ")
   

print("\n\n----------------------------------------------------")

print("TOTAL EMPLOYEES: {0} | TOTAL GROSS PAY ${1:.2f}".format(total_employees, total_gross))