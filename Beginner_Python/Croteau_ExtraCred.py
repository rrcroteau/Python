#Name Ron Croteau
#Extra Credit
#June 3, 2021
#SE116.01
#PROGRAM PROMPT: Follow a flowchart to create a program which is used to calculate the average of grades.  The user will be presented a menu where the choices will be to add grades, average the grades entered, reset the grades entered, or exit.

#VARIABLE DICTIONARY:
#choice --> holds the user's choice from the menu
#answer --> controls the loop for the calculator
#grade --> grade entered by the user
#grade_total--> holds the total of all grades entered
#grade_num --> holds the number of grades entered


#FUNCTIONS-------------------------------------------
 
def menu():
    '''Presents the menu to the user and returns option to main program'''
    
    print("\n\t1. Add Grades")
    print("\n\t2. Find Average Grade")
    print("\n\t3. Reset Grades")
    print("\n\t4. EXIT")
    
    #solicit user choice to return to main program
    option = int(input("\nPlease enter either 1, 2, 3, or 4: > "))
    
    while option < 1 or option > 4:

        print("**ERROR**ERROR MENU**")
        option = int(input("\nPlease enter either 1, 2, 3, or 4: > "))
    
    return option

def gradeSum(gt, g):
    '''Totals the grades input by the user'''

    gt = gt + g

    return gt

def counter(num):
    '''Increments the number of grades entered and returns to main program'''

    num = num + 1

    return num

def averageFunc(total, num):
    '''Averages the grades and returns to main program'''

    avg = total / num

    return avg

def responseCheck():
    '''Asks if the user wants to use the calculator again, validates the response, then sends it to the main program'''

    ans = input("Would you like to use the calculator again? [y/n] > ")
    ans = ans.lower()

    while ans != "y" and ans != "n":

        print("**ERROR**ERROR**")
        ans = input("Would you like to continue using the grade calculator? [y/n] > ")
        ans = ans.lower()

    return ans

#MAIN-----------------------------------------------------

#welcome msg
print("\n\t\tWelcome to my Grade Calculator\n\n")

answer = input("\nWould you like to use the calculator? [y/n] > ").lower()

#initialize counting variables
grade_total = 0
grade_num = 0

#enter the loop
while answer == "y":

    choice = menu()

    #add grades
    if choice == 1:

        grade = int(input("\n\tPlease enter a numeric grade: > "))

        grade_num = counter(grade_num)

        grade_total = gradeSum(grade_total, grade)

    #find avg grade    
    elif choice == 2:

        print("\n\n\tGrade Average")

        if grade_num == 0:

            print("\nGrades must be entered before an average calculation can be made.")

        else:
            
            average = averageFunc(grade_total, grade_num)
            print(f"\nThe average of the {grade_num} grade(s) you entered is: {average}")

    #reset grades
    elif choice == 3:

        print("\n\tResetting Grades")
        grade_total = 0
        grade_num = 0
        print("\n\tGrades have been reset")

    #exit
    elif choice == 4:

        answer = "n"

    else: #this should actually never happen due to data validation in menu()

        print("\n**ERROR**! You must enter a valid response")

    #way out of loop
    if choice != 4:
        print("\n\n")
        answer = responseCheck()
#goodbye message
print("\n\n\tThank you for using my program. Goodbye :]")







