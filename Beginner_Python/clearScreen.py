#This program builds and calls a clear screen function named clear.  Lines 4 - 18 are necessary code, and lines 20-30 are demonstrating the code

# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

 #DEMO CODE---------------------------------------------------
print("clear() is a function we just wrote in our solution file.")
sleep(5) #forces console to pause for 5 seconds before reading next line
print("\n\n if you are seeing this message, you have waited 5 seconds ... ")

sleep(3) #add sleep call before clear() call to pause console for user to read
clear() #calls the clear(), clears the screen
print("The clear function was just called. It will be called again in another ... ")
print("5 seconds ... ")
sleep(2)
print("\t 3 seconds ... ")
sleep(2)
print("\t\t 1 second ... ")
sleep(1)
clear()
