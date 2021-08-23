#WEEK 6 DAY 1: Sequential Search

#Sequential Search: Sequential search means to search through an entire list (array), starting at the first record and looking through every one until the last, when looking for something. 

 

#For Loops --> allow us to process every record in an list (for index in range(0, records) --> this applies to every record in the list)

#If Statements --> allow us to "search": compare a value in the list we are looking through against the value(s) we are looking for. 

#we are utilizing binary.txt for this demo
#       FIELD0     FIELD1     FIELD2      FIELD3
#       ID nums    Names      Age         Color  

#VARIABLE DICTIONARY





#BASE PROGRAM CODE--------------------------------------------------------------------

import csv

#prep empty lists for storage of data from file
id = []
name = []
age = []
color = []

#initialize counters
records = 0 #holds the total number of records in file/each list

search_count = 0 #holds the count of how many search loops were used to find the name/item we are looking for (how many times we go through the sequential search loop)

with open("DemosNotes/W6D1_SeqSearch/binary.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #print(rec)
        records += 1

        #store file data to lists
        id.append(rec[0])
        name.append(rec[1])
        age.append(rec[2])
        color.append(rec[3])
#DISCONNECTING FILE LOCATION----------------------------------
print("Finished Processing file.\n\n\n")

#print the populated lists to check the storage (make sure it's been done correctly)
for i in range(0, records):

    print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i], age[i], color[i]))

print("\n\n\n")#empty print lines to separate out the console


answer = "y"

while answer == "y":

    #SEQUENTIAL SEARCH
    #sequential --> specified order (in sequence) in searching: top to bottom (data in file, first record first, last record last)

    #gather earch item data -- NECESSARY
    search = input("Enter the FULL LAST NAME of the record you are looking for: ")

    found = -1  #starting value of -1 because INDEX values are not negative
                #will hold searched-for location if search is completed and item is found

    for i in range(0, records):

        #this for loop allows us to look at an entire list from top to bottom
        #it is responsible for the "sequential"
        #starts with the first record and iterates through the last record

        #count the number of times this loop runs. this is the search count
        search_count += 1

        #look for the searched for item
        if search == name[i]: 
            #SEARCHED ITEM HAS BEEN FOUND

            found = i #the searched-for item is found at this location point along with the rest of their data

            #if statement runs the "search"
            #compares what you are looking for (search) against every possible option (each value stored in the specific searched-through list)

            #when this if statement is TRUE: we've FOUND what we're looking for
            #print("We have FOUND ", search, " at INDEX: ", i)

            #print entire record of searched item's info
            #print("\t\t\t{1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i], age[i], color[i]))

        #else:
            #print("Your search for ", search, " has NOT BEEN FOUND.")

    print("\n\nSequential Search complete.\n\n\n")

    if found >= 0 :

        #when this if statement is TRUE: we've FOUND what we're looking for
        print("We have FOUND ", search, " at INDEX: ", found)
        
        #print entire record of searched item's info
        print("\t\t\t{0:10} \t {1:10} \t {2:10} \t {3:10}".format(id[found], name[found], age[found], color[found]))

    else:
        print("Your search for ", search, " has NOT BEEN FOUND.")
        print("cHeCk YoUr SpElLiNg and try again!")


    print("\n\nLOOPS PERFORMED FOR THIS SEARCH: ", search_count)

    search_count = 0 #resets the counter for the next search

    answer = input("\n\n Would you like to search again? [y/n]: ")
    
    answer = answer.lower() #finds lowercase equivalent of object before '.'

    while answer != "y" and answer != "n":
        print("**INVALID ENTRY**")
        answer = input("\n\n Would you like to search again? [y/n]: ")
    
        answer = answer.lower() #finds lowercase equivalent of object before '.'

print("\n\n\nThank you for using KT's FINDERS KEEPERS search program. Goodbye.\n\n\n")