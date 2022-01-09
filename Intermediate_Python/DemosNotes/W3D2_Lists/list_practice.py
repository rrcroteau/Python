#W3D2 -- connect to/read from a file and store data into a lists for use throughout program

import csv #will also read .txt

#record counter
records = 0

#prep some empty lists to store data from file

name = []
age = []
color = []
animal = []
section = []

with open("DemosNotes/W3D2_Lists/classList_202140.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #everything in this loop happens to EACH record in file
        records += 1

        #store data into lists we prepared
        name.append(rec[0])
        age.append(int(rec[1]))
        color.append(rec[2])
        animal.append(rec[3])
        section.append("SE126.02")

#disconnected from the file
print("\n\tFinished reading file; {0} records processed\n\n".format(records))       

#list processing --> FOR LOOOOOOP!
for i in range(0, records): #for each inex starting at 0 and up to number of records

    print("INDEX: {0}  |  {1:7}{2:^4}{3:8}{4:10}{5}".format(i, name[i], age[i], color[i], animal[i], section[i]))

#process lists to find the average age
total_age = 0
for i in range(0, len(age)): #len() returns number of items

    total_age += age[i]

avg_age = total_age / len(age) #or divide by records

print("\n\tAVG AGE is {0:.1f}".format(avg_age))

#process the lists to count/tally favorite animals
crow = 0
elephant = 0
dog = 0
lion = 0
dolphin = 0
monkey = 0
wolf = 0

for i in range(0, records):

    if animal[i] == "crow":

        crow += 1

    elif animal[i] == "elephant":

        elephant += 1

    elif animal[i] == "dog":

        dog += 1

    elif animal[i] == "lion":

        lion += 1

    elif animal[i] == "dolphin":

        dolphin += 1

    elif animal[i] == "monkey":

        monkey += 1

    elif animal[i] == "wolf":

        wolf += 1

    else:

        print("***ERROR*** unexpected animal found in record: ", i)

print("\n\tFAVORITE ANIMAL TALLIES:")
print("\t\tCROW: ", crow)
print("\t\tELEPHANT: ", elephant)
print("\t\tDOG: ", dog)
print("\t\tLION: ", lion)
print("\t\tDOLPHIN: ", dolphin)
print("\t\tMONKEY: ", monkey)
print("\t\tWOLF: ", wolf)

    







