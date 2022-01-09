#Name Ron Croteau
#Lab 1B
#April 11, 2021
#SE116.01
#PROGRAM PROMPT: You want to develop a program that gathers the user’s hourly pay (use $14.50), hours worked (32/week),and tax rate for a two-week period. Once you have this information, you want to display the user’s Gross Pay, Uncle Sam’s Share, and the User’s Net Pay. All calculations should be limited to run once, rather than numerous times. Include in both your flowchart the use of variables and print statements. Use 20% for the tax rate.

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
#initialize variables
hourly_rate = 14.50
hrs_wk1 = 32
hrs_wk2 = 32
tax_rate = .2
total_hrs = hrs_wk1 + hrs_wk2
gross_pay = hourly_rate * total_hrs
tax_amount = gross_pay * tax_rate
net_pay = gross_pay - tax_amount

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
print("Thank you for using the Croteau Net Pay Calculator, goodbye!")