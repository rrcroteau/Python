#WEEK 8: Bubble Sort

#Binary Search can only be performed on ORDERED LISTS
#Lists can be ordered numerically or alphabetically, in increasing or decreasing order


#FUNCTIONS---------------------------------------------
def swap(n, j):

    t = n[j]
    n[j]= n[j + 1]
    n[j + 1] = t

#MAIN PROGRAM------------------------------------------

name = ["Mary", "Cathy", "Tom", "Whitney", "Adam", "Sam", "Betty", "Ed"]
age = [21, 33, 24, 28, 30, 31, 40, 68]

number_of_elements = len(name)

print("BEFORE SORTING-----------------------------")
for i in range(0, number_of_elements):
    print("INDEX: {0} \t {1:10} \t {2}".format(i, name[i], age[i]))

#BUBBLE SORT----------------------------------------
for i in range(0, number_of_elements - 1):#outer loop
    print("OUTER LOOP! i = ", i)

    for index in range(0, number_of_elements - 1):#inner loop
        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing
        if(name[index] > name[index + 1]):
            print("\t\t SWAP! ", name[index], "<-->", name[index + 1])
            #if above is true, swap places!
            #temp = name[index]
            #name[index] = name[index + 1]
            #name[index + 1] = temp
            swap(name, index)

            #swap all other values
            #temp = age[index]
            #age[index] = age[index + 1]
            #age[index + 1] = temp
            swap(age, index)

          


print("End of Bubble Sorting \n\n\n")

for i in range(0, number_of_elements):
    print("INDEX: {0} \t {1:10} \t {2}".format(i, name[i], age[i]))

print("Program complete.")