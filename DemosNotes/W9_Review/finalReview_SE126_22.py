#WEEK 9: FINAL REVIEW

#This review demo will cover all major topics from SE126.  It utilizes: 'finalReview_text.txt'
#Documentation has been added post demo to enhance understandig of the code

#in this review program, you will:
#   1 - connect to a file and import its data into lists
#               1a - the lists are UNEVEN so a filter system must be used
#               1b - count the total number of people in the file
#   2 - process the lists to print the original data to the console
#   3 - process the lists to find:
#               3a - the youngest person in the list
#               3b - the oldest person in the list
#               3c - the average age of the people in the list
#   4 - a search option to search for id codes within the list
#           ** utilize menu '1. Sequential 2. Binary 3. Exit' that is printed from a function that returns the user's selection choice
#               4A - allow user to search multiple time
#               4a - sequential search will be performed w/ output to visualize search
#               4b - binary search will be performed w/ output to visualize search

#REC[INDEX]	    0	        1	        2	    3	    4	        5	6	    7*
#Field	        0	        1	        2	    3	    4	        5	6	    7*
#Description	idCode	lastName	firstName	age	    allegiance	num	color1	color2



#FUNCITONS-----------------------------------------------------------------------
def hello():

    print("Welcome to the SE126 FINAL REVIEW!")

def goodbye():

    print("Thank you for viewing the review. Now GO STUDY and kick some Finals butt!")


#a function that swaps values for bubble sorting
def swap(listname, position):

    temp = listname[position]
    listname[position] = listname[position + 1]
    listname[position + 1] = temp


    #this function could not return OR return TWO values ...
    #return listname[position], listname[position + 1]
    #         firstName[k],         firstName[k + 1]
    #call in base program --> firstName[k], firstName[k + 1] = swap(firstName, k)

#a function that allows a user to search by sequential search or binary search
def search_menu():

    print("1. Sequential Search")
    print("2. Binary Search")
    print("3. Exit")

    response = int(input("Please enter your choice [1 - 3]: "))

    while response != 1 and response != 2 and response != 3:

        print("*ERROR*ERROR*")
        response = int(input("Please enter your choice [1 - 3]: "))

    #this function should return the user's selection AFTER checking that it is a valid input()
    return response

#---------------------------------------------------------------------------------
import csv

hello()


num_rec = 0

#create empty lists in order to store file data
idCode = []
lastName = []
firstName = []
age = []
allegiance = []
num = [] #if == 1, no color2 value ... only when == 2 is there a color2 value
color1 = []
color2 = [] #only when num (rec[5] from file) is == 2 is there a color2 present

#1 - connect to a file and import its data into lists
with open("DemosNotes/W9_Review/finalReview_text.txt") as csvfile:

    file = csv.reader(csvfile)

        #when reading files, each record is treated as a list
        #each field of data (rec[#]) represents a new value
    for rec in file:

        #this for loop will run for as many records (rows) of data in the file
        

        #store data into lists --> .append()
        idCode.append(rec[0])
        lastName.append(rec[1])
        firstName.append(rec[2])
        age.append(int(rec[3])) #cast as int for easier numeric processing later in program
        allegiance.append(rec[4])
        num.append(rec[5]) #if rec[5] == 2 there are 2 colors (color1[], color2[]) if not only 1
        color1.append(rec[6])


        #1a - the lists are UNEVEN so a filter system must be used
        #(not all records in the file have a color2, so we must filter)
        if int(rec[5]) == 1:

            color2.append("-none-")

        elif int(rec[5]) == 2:
            color2.append(rec[7])

        else:
            color2.append("ERROR!")



        #1b - count the total number of people in the file
        #add one to total number of records, necessary for for loop processing
        num_rec += 1 

print("\n\nFinished storing data from file. Disconnecting from file now.\n\n")


#   2 - process the lists to print the original data to the console
for i in range(0, num_rec):

    #the for loop will start with 'i = 0'
    #for loop will +1 to value of 'i' through each pass through the loop
    #for loop will run for 'num_rec' times (for each record in the list)
    #wherever 'i' is present, replace with current loop integer value

    print("{0:15} {1:15} {2:15} {3:3} {4:35} {5:3} {6:7} {7:7}".format(idCode[i], lastName[i], firstName[i], age[i], allegiance[i], num[i], color1[i], color2[i]))




#   3 - process the lists to find:
#PROCESS = FOR LOOP! for loops were BUILT for list/array processing!

#Ask yourself: 
#If the AGE list were ordered in *increasing numeric* order, 
#where would you find:
# index 0           - the youngest person in the list
# index num_rec - 1 - the oldest person in the list

#BUBBLE SORT to ORDER THE AGES -- increasing numeric order
#after the bubble sort we can use info on lines 147 and 148 to find the youngest/oldest

for i in range(0, num_rec - 1):

    for k in range(0, num_rec - 1):

        if age[k] > age[k + 1]:

            #swap values
            ageswap = age[k]
            age[k] = age[k + 1]
            age[k + 1] = ageswap

            #swap all other values
            ageswap = idCode[k]
            idCode[k] = idCode[k + 1]
            idCode[k + 1] = ageswap

            ageswap = lastName[k]
            lastName[k] = lastName[k + 1]
            lastName[k + 1] = ageswap

            ageswap = firstName[k]
            firstName[k] = firstName[k + 1]
            firstName[k + 1] = ageswap

            ageswap = allegiance[k]
            allegiance[k] = allegiance[k + 1]
            allegiance[k + 1] = ageswap

            ageswap = num[k]
            num[k] = num[k + 1]
            num[k + 1] = ageswap

            ageswap = color1[k]
            color1[k] = color1[k + 1]
            color1[k + 1] = ageswap

            ageswap = color2[k]
            color2[k] = color2[k + 1]
            color2[k + 1] = ageswap

#print new swapped records and check values
print("\n\n\nSWAPPED --- AGE, INCREASING ORDER-------------------------------------------------")
for i in range(0, num_rec):

    print("{0:15} {1:15} {2:15} {3:3} {4:35} {5:3} {6:7} {7:7}".format(idCode[i], lastName[i], firstName[i], age[i], allegiance[i], num[i], color1[i], color2[i]))


#store the youngest/oldest into variables for their name and age
name_young = firstName[0] + " " + lastName[0]
age_young = age[0]

name_old = firstName[num_rec - 1] + " " + lastName[num_rec - 1]
age_old = age[num_rec - 1]

#Ask yourself:
#What do you need to find an average? 
#AVERAGE = sum total of items / count of items
#               3c - the average age of the people in the list

total_age = 0

for i in range(0, num_rec):

    total_age += age[i]


avg_age = total_age / num_rec #calculating average age

print("\n\n")
print("   YOUNGEST: {0:15}, {1}yo".format(name_young, age_young))
print("     OLDEST: {0:15}, {1}yo".format(name_old, age_old))
print("AVERAGE AGE: \t {0:.2f}".format(avg_age))

#   4 - a search option to search for id codes within the list
#           ** utilize menu '1. Sequential 2. Binary 3. Exit' that is printed from a function that returns the user's selection choice
#4A - allow user to search multiple time
#if the function has a RETURN we must store its return to use in our base program

answer = "y" #allows us to get in loop

while answer == "y":

    #call menu function so we have options from menu -- this function will be returning the user's selection and storing it into the var userChoice

    userChoice = search_menu()

    if userChoice == 1:
        #4a - sequential search will be performed w/ output to visualize search
        print("SEQUENTIAL SEARCH!")

        #ask for search query
        search = input("Enter the IDCODE you are looking for: ")

        #run sequential search
        found = -1

        for i in range(0, num_rec):

            if search == idCode[i]:
                #print("{0:10} \t {1:15} \t {2:15} \t {3:3} \t {4:35} \t {5:3} \t {6:7} \t {7:7}".format(idCode[i], lastName[i], firstName[i], age[i], allegiance[i], num[i], color1[i], color2[i]))
                found = i


        if found >= 0:

            print("Your search for ", search, " was FOUND in record: ", found)
            print("{0:15} \t {1:15} \t {2:15} \t {3:3} \t {4:35} \t {5:3} \t {6:7} \t {7:7}".format(idCode[found], lastName[found], firstName[found], age[found], allegiance[found], num[found], color1[found], color2[found]))

        else:

            print("Your search for ", search, " was *NOT* found!")
            print("Please check your spelling & capitalization and try again.")

        print("\n\n\n")

        #print results

    if userChoice == 2:

        #4b - binary search will be performed w/ output to visualize search
        #BINARY SEARCH CAN ONLY BE USED ON ORDERED LISTS
        print("BINARY SEARCH")

        #ask for search query
        search = input("Enter the FIRSTNAME of the person you are looking for: ")

        #sort list & linked data
        #sorted by FIRSTNAME in INCREASING ORDER
        for i in range(0, num_rec - 1):

            for k in range(0, num_rec - 1):

                if firstName[k] > firstName[k + 1]:

                    #swap!
                    swap(firstName, k)

                    #firstName[k], firstName[k + 1] = swap(firstName, k)
                    swap(idCode, k)
                    swap(lastName, k)
                    swap(age, k)
                    swap(allegiance, k)
                    swap(num, k)
                    swap(color1, k)
                    swap(color2, k)

        #check your swap and make sure it's accurate!
        #print("\n\n\nSWAPPED --- FirstName, INCREASING ORDER-------------------------------------------------")
        #for i in range(0, num_rec):

        #    print("{0:10} \t {1:15} \t {2:15} \t {3:3} \t {4:35} \t {5:3} \t {6:7} \t {7:7}".format(idCode[i], lastName[i], firstName[i], age[i], allegiance[i], num[i], color1[i], color2[i]))



        #binary search list
        min = 0
        max = num_rec - 1
        guess = int((min + max) / 2)


        while min < max and search != firstName[guess]:

            if search < firstName[guess]: #drop the higher end of the list
                max = guess - 1

            else: #drop the lower end of the list
                min = guess + 1

            guess = int((min + max) / 2)

        #print results
        if search == firstName[guess]:

            print("Your search for ", search, " was FOUND in record: ", guess)
            print("{0:15} \t {1:15} \t {2:15} \t {3:3} \t {4:35} \t {5:3} \t {6:7} \t {7:7}".format(idCode[guess], lastName[guess], firstName[guess], age[guess], allegiance[guess], num[guess], color1[guess], color2[guess]))

        else:

            print("Your search for ", search, " was *NOT* found!")
            print("Please check your spelling & capitalization and try again.")


    if userChoice == 3: 

        #EXIT PROGRAM
        print("EXIT")
        answer = "x"


    #which menu choices do NOT want to be asked if they want to run again?
    if userChoice == 1 or userChoice == 2:

        answer = input("\n\nWould you like to see the menu again? [y/n]: ")
        answer = answer.lower()

        while answer != "y" and answer != "n":

            print("**ERORR! ERROR!**")
            answer = input("Would you like to see the menu again? [y/n]: ")
            answer = answer.lower()

goodbye()