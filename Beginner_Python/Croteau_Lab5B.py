#Name Ron Croteau
#Lab 5B
#May 16, 2021
#SE116.01
#PROGRAM PROMPT: All end devices on a network require an IP address. IP addresses are classified as Class A,Class B Class C, Class D, or Class E. For the most part network administrators work with Class A, B,and C. Each IP address consists of 4 octets. The first octet determines the class. 
#Example:Class A address first octet is in the range of 1–127 Class B address first octet is in the range of 128–191 Class C address first octet is in the range of 192-223
#The IP address 190.1.65.35 is a Class B because the first octet is between 128 and 191.The IP address 192.192.5.6 is a Class C because the first octet is between 192 and 223
#Write a program that will allow the user to enter as many IP addresses that they want (loop!) and print out the IP address and its class. See KT’s notes on .split() (posted in W7 “Notes”) on how to break the IP address into its 4 octets. The IP address, when printed,should appear exactly as it did when entered by the user. If the IP address is nota Class A,B, or C, the user should also be alerted and the IP address should still be reprinted. The user should be able to enter either a y or Y to continue the loop.

#VARIABLE DICTIONARY:
#ip_addr --> the ip address entered by the user
#ip_addr_split --> the list of ip address octets created with .split('.')
#first_octet --> first set of digits before the first period (1-255 [223 for scope])
#second_octet --> second set of digits, between first and second period (1-255)
#third_octet --> third set of digits, between second and third period (1-255)
#fourth_octet --> final set of digits, after the third period (1-255)
#answer --> used for flow control


#NOTES: validate user input, valid input numbers are 1 through 255. The scope of this program is from Class A - Class C (1 through 223).
#----------------------------------------------------#

#initialize initial loop control
answer = "y"

#welcome message and instructions
print("\n\n\t\tWelcome to the Croteau Network Class Identifier Program\n\n")
print("\tScope: This program is designed to identify networks Class A - Class C")
print("\tIP Addresses have 4 octets (numbers from 1-255, seperated by a period)")
print("\tClass A - Class C have a first octet ranging from 1 - 223")
print("\tExample of valid input for program is: 8.255.255.117\n\n")

#enter loop
while answer == 'y':
    
    ip_addr = input("\nPlease enter a valid IP address: > ")
    #print(ip_addr)
    
    #split the ip address into the four octets
    ip_addr_split = ip_addr.split('.')
    #print(ip_addr_split)

    #data validation to ensure 4 octets
    while len(ip_addr_split) != 4:
        print(f"\n\tThe IP address you entered is: {ip_addr}")
        print("\tPlease ensure you have 4 numbers, 1-255, separated by a period (ex: 8.8.8.8)\n\n")
        ip_addr = input("Please enter a valid IP address: > ")
        ip_addr_split = ip_addr.split('.') #must be split again for revalidation

    #cast octets from list into integers for mathmatical ops
    first_octet = int(ip_addr_split[0])
    second_octet = int(ip_addr_split[1])
    third_octet = int(ip_addr_split[2])
    fourth_octet = int(ip_addr_split[3])
    #print(first_octet, second_octet, third_octet, fourth_octet)

    #data validation to ensure octets are valid (1-255)
    while (first_octet < 1 or first_octet > 255) or (second_octet < 1 or second_octet > 255) or (third_octet < 1 or third_octet > 255) or (fourth_octet < 1 or fourth_octet > 255):
        print(f"\n\tThe IP address you entered is: {ip_addr}")
        print("\tPlease ensure you have 4 numbers, 1-255, separated by a period (ex: 1.128.255.255)\n\n")
        ip_addr = input("Please enter a valid IP address: > ")
        #split/assign again for revalidation
        ip_addr_split = ip_addr.split('.')

        while len(ip_addr_split) != 4:
            print(f"\n\tThe IP address you entered is: {ip_addr}")
            print("\tPlease ensure you have 4 numbers, 1-255, separated by a period (ex: 8.8.8.8)\n\n")
            ip_addr = input("Please enter a valid IP address: > ")
            ip_addr_split = ip_addr.split('.')

        first_octet = int(ip_addr_split[0])
        second_octet = int(ip_addr_split[1])
        third_octet = int(ip_addr_split[2])
        fourth_octet = int(ip_addr_split[3])

    #output network class based on valid data passed through if/elif statements
    if first_octet > 223:
        print(f"\n\tThe IP address you entered is: {ip_addr}")
        print("\tThis network class is outside the scope of this program.\n\tThis program once again is designed for networks with a first octet of 1-223")
    elif first_octet < 128:
        print(f"\n\tThe IP address you entered is: {ip_addr}")
        print("\tThis IP address is on a Class A network")
    elif first_octet > 191:
        print(f"\n\tThe IP address you entered is: {ip_addr}")
        print("\tThis IP address is on a Class C network")
    else:
        print(f"\n\tThe IP address you entered is: {ip_addr}")
        print("\tThis IP address is on a Class B network")

    #way out of loop
    answer = input("\nWould you like to check another IP address? [y/n] > ").lower()

print("\n\n\tThank you for using the Croteau Network Class Identifier Program, goodbye\n")
