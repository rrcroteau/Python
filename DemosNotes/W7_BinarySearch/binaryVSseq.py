#W7D2 - Sequential Search vs Binary Search

import csv

id_ = []
name = []
age = []
color = []

records = 0

with open("DemosNotes/W7_BinarySearch/binary.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        id_.append(rec[0])
        name.append(rec[1])
        age.append(rec[2])
        color.append(rec[3])

#disconnected from file
# print(f"{'ID#':5}\t{'NAME':10}\t{'AGE':5}\t{'COLOR'}")

# for i in range(0,records):

#     print(f"{id_[i]:5}\t{name[i]:10}\t{age[i]:5}\t{color[i]}")

answer = "y"

while answer == "y":

    #get search term

    search = input("Enter the NAME of the user you are looking for: ")

    #SEQUENTIAL SEARCH
    found = -1

    search_count = 0

    print("\n\t\t\tSequential Search")
    for i in range(0,records):
        
        search_count += 1
        
        if search == name[i]:

            found = i
            #when searching for multiples, you could put the print inside the if or you can append i value to new list

    if found != -1:

        print(f"Your search for {search} was FOUND in {search_count} loops!")
        print(f"{'ID#':5}\t{'NAME':10}\t{'AGE':5}\t{'COLOR'}")
        print(f"{id_[found]:5}\t{name[found]:10}\t{age[found]:5}\t{color[found]}")

    else:
        print(f"Your search for {search} was *NOT FOUND* in {search_count} loops!")
        print("Please check your spelling and capitalization and try again.")

    #BINARY SEARCH
    #requires ORDERED lists (Ascending or Descending)

    min = 0
    max = records - 1
    guess = (min + max) // 2 #or int((min + max) / 2)

    search_count = 0

    #search with binary
    print("\n\t\t\tBinary Search")

    while (min < max and search != name[guess]):

        search_count += 1

        if search < name[guess]:

            max = guess -1 #search is less than middle point, so no need to consider high half of list

        else:

            min = guess + 1 #search is greater than middle point, so no need to consider low half of list

        guess = (min + max) // 2 #make sure this is not nested in if/else portion

    if search == name[guess]:

        print(f"Your search for {search} was FOUND in {search_count} loops!")
        print(f"{'ID#':5}\t{'NAME':10}\t{'AGE':5}\t{'COLOR'}")
        print(f"{id_[found]:5}\t{name[found]:10}\t{age[found]:5}\t{color[found]}")
    
    else:
        
        print(f"Your search for {search} was *NOT FOUND* in {search_count} loops!")
        print("Please check your spelling and capitalization and try again.")


    #allow the user to search multiple times
    answer = input("\n\nWould you like to search again? [y/n]: ").lower()
