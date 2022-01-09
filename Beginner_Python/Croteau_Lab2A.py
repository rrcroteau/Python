#Name Ron Croteau
#Lab 2A
#April 18, 2021
#SE116.01
#PROGRAM PROMPT: This is the same as Lab 1B except instead of using assignment statements for hours worked and hourly rate, use the input statement to assign values to variables. Once you have this information, you want to display the user’s Gross Pay, Uncle Sam’s Share, and the User’s Net Pay.  All calculations should be limited to run once, rather than numerous times. Include in both your pseudocode and flowchart the use of variables and print statements. Use 20% for the tax rate.

#VARIABLE DICTIONARY:
#hourly_rate --> hourly pay
#hrs_wk1 --> hours worked in week 1 of pay period
#hrs_wk2 --> hours worked in week 2 of pay period
#tax_rate --> the amount of taxes applied to the pay
#total_hrs --> total of hours for pay period(week 1 and week2)
#gross_pay --> hourly rate times total hours worked
#tax_amount --> gross pay times the tax amount (i.e. taxes paid)
#net_pay --> gross pay minus the taxes
#NOTES: DON'T FORGET YOUR GOODBYE STATEMENT!!!
#----------------------------------------------------
#welcome message
print("Welcome to the Croteau Pay Calculator\n\n")
#initialize variables
#per 2A requirements, solicit input for hours worked, hourly rate, and tax rate
#hourly_rate = 14.50
#hrs_wk1 = 32
#hrs_wk2 = 32
#tax_rate = .2
hourly_rate = float(input("Enter your hourly wage rate: $"))
hrs_wk1 = float(input("Enter number of hours worked in the first week of the pay period: "))
hrs_wk2 = float(input("Enter number of hours worked in the second week of the pay period: "))
tax_rate = float(input("Enter the current tax rate percentage (i.e. 20 or 12.5): ")) / 100
total_hrs = hrs_wk1 + hrs_wk2
gross_pay = hourly_rate * total_hrs
tax_amount = gross_pay * tax_rate
net_pay = gross_pay - tax_amount


print("\n\n")
#output the gross pay
print("Gross Pay:\t\t ${0:8.2f}".format(gross_pay))

#output the taxes
print("Tax Amount:\t\t-${0:8.2f}".format(tax_amount))

#visual line added to seperate gross and net pay figures
print("--------------------------")

#output net pay
print("Net Pay:\t\t ${0:8.2f}".format(net_pay))

print("\n\n")
#goodbye statement
print("Thank you for using the Croteau Pay Calculator, goodbye!\n\n")