#Name Ron Croteau
#Final Project
#June 3, 2021
#SE116.01
#PROGRAM PROMPT: I am making a 30-room maze with functions for each room entered. User will have to accomplish things before progress can be made in certain rooms, such as finding a key to open a lock or completing a puzzle. There will be a timer running that starts after user reads the rules and ends at completion of the maze.   

#VARIABLE DICTIONARY:
#user_name --> holds the user's name
#success --> used to determine what goodbye message displays at the end(changes to "y" if the maze is successfully completed)
#inv --> holds the contents of user's inventory, starts as empty list []
#curr_loc --> use to hold the number of the room user came from for a customized first sentence in each room
#choice --> used to store the user's choice from various menus
#timer --> holds how long the countdown timer will last, in seconds_converter
#running_time --> the start/running time for the maze, begins after user accepts rules
#completion_time --> the difference of the running_time and when the user finishes the maze
#fusebox --> holds a boolean determining if the fusebox has been fixed

#IMPORTS---------------------------------------------#

#import system and name to create a clear screen function (clear())
from os import system, name 
  
#import time and sleep from time to be used for countdown and time elapsed 
from time import time, sleep

#FUNCTIONS-------------------------------------------#

def clear(): 
    
    '''Clears the output/screen'''

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def seconds_converter(secs):
    
    '''Converts seconds into minutes and seconds to return the maze completion time to be called later in the goodbye function'''

    minutes = int(secs // 60)
    seconds = int(secs - minutes * 60)

    result = ("\t{0} minute{1}".format(minutes, "s" if minutes != 1 else "") if minutes else "") + (" {0} second{1}".format(seconds, "s" if seconds != 1 else ""))

    return result

def goodbye(running_time, success):
    
    '''Prints a custom goodbye message based on success/failure, total time taken, and quits program'''
    
    if success:

        completion_time = (time() - running_time)
        clear()
        print("\n\n\nCongratulations on your epic feat! You escaped the maze!!")
        print("\nThe total time it took for you to complete the maze is:\n")
        print(seconds_converter(completion_time))
        print("\nTry to beat this the next time through the maze!")
        print("\nThanks for playing! Goodbye!")

    else:
        
        completion_time = (time() - running_time)
        clear()
        print("\n\n\nUnfortunately, you were unable to escape the maze!")
        print("\nThe total time you spent getting lost in the maze is:\n")
        print(seconds_converter(completion_time))
        print("\nBetter luck next time! Goodbye!")

def yes_no_choice(choice):

    '''This validates that a user enters a 'y' or 'n' when give the choice of [y/n]'''
    
    while choice.lower() != "y" and choice.lower() != "n":

        print("\n\nInput Error: Please only answer only with a 'y' or 'n'")
        choice = input("\nPlease choose a valid answer: [y/n] > ")
    
    return choice.lower()

def room1(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 1 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 2: 

        print("\n\nYou enter the room from the east.\n")

    #update location
    curr_loc = 6

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is closed door on the east side of the room")
    print("\tThere is a small item in the northeast corner of the room")
    
    #present options
    print("\n\n1. Examine the closed door to the east")
    print("2. Examine the small item in the northeast corner of the room")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Examine the closed door to the east")
        print("2. Examine the small item in the northeast corner of the room")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        print("\n\nAs you approach the heavy wooden door, you notice a wolf engraved on the escutcheon, just above the door handle. You jiggle the handle to find out it is locked.\n\n")    
        print("It seems the key you found with the wolf engraved on the bow would be the perfect fit for this door.")
        print("\nYou slide the key into the lock and turn until the deadbolt releases and the door opens.")
        print("\nYou push through the door and ensure you take your key with you.")
        input("\n\nPress Enter to continue: >")
        clear()
        room2(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":
            
        if "candle" not in inv:

            print("\n\nYou examine the item and it appears to be a long paper box. You open it up to see what's inside")
            choice = input("\nUpon examination you find a candle inside the box.\nDo you wish to take it? [y/n] > ")

            #run it through the validation
            choice = yes_no_choice(choice)

            if choice == "y":
                
                #add candle to inventory
                inv.append("candle")
                #print(inv)
                print("\nYou take the candle and toss the paper box back in the corner.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room1(curr_loc, inv, lever, running_time, fusebox)

            else:

                print("\nYou leave the candle and toss the small box back in the corner.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room1(curr_loc, inv, lever, running_time, fusebox)

        else:

            print("\n\nYou examine the item and it appears to be a long paper box. You open it up to see what's inside.")
            print("\nThe box appears to be empty inside, so you toss it back in the corner.")
            print("\nYou take a moment to reassess your surroundings.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room1(curr_loc, inv, lever, running_time, fusebox)
                                    
    else:
        success = False
        goodbye(running_time, success)

def room2(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 2 of the maze'''
    
    #customize first line for room based on where the user is coming from
    if curr_loc == 3: 

        print("\n\nYou enter the room from the east.\n")

    else:

        print("\n\nYou enter the room from the west.\n")

    #update location
    curr_loc = 2
    #inv.append("wolf key") #for testing
    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is a closed door on the west side of the room")
        
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Examine the closed door to the west")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Examine the closed door to the west")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":
        
        clear()
        room3(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":

        print("\n\nAs you approach the heavy wooden door, you notice a wolf engraved on the escutcheon, just above the door handle. You jiggle the handle to find out it is locked.\n\n")
        
        if "wolf key" not in inv:

            print("\nIt appears you don't have the right key for this door.")
            print("\nYou better take a look at your surroundings.")
            input("\n\nPress ENTER to continue: >")
            clear()
            room2(curr_loc, inv, lever, running_time, fusebox)

        else:

            print("It seems the key you found with the wolf engraved on the bow would be the perfect fit for this door.")
            print("\nYou slide the key into the lock and turn until the deadbolt releases and the door opens.")
            print("\nYou push through the door and ensure you take your key with you.")
            input("\n\nPress Enter to continue: >")
            clear()
            room1(curr_loc, inv, lever, running_time, fusebox)
            
    else:
        success = False
        goodbye(running_time, success) 

def room3(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 3 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 2: 

        print("\n\nYou enter the room from the west.\n")

    else:

        print("\n\nYou enter the room from the south.\n")
        
    #update location
    curr_loc = 3

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the west side of the room")
    print("\tThere is an open door on the south side of the room")
    
    #present options
    print("\n\n1. Go through the door to the west")
    print("2. Go through the door to the south")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Go through the door to the south")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        clear()    
        room2(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":
        
        clear()
        room8(curr_loc, inv, lever, running_time, fusebox)
    
    else:

        success = False
        goodbye(running_time, success) 

def room4(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 4 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 9: 

        print("\n\nYou enter the room from the south.\n")

    #update location
    curr_loc = 4

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the south side of the room")
    print("\tThere is a small wooden chest in the southeast")
    
    #present options
    print("\n\n1. Go through the door to the south")
    print("2. Examine the small wooden chest in the southeast")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the south")
        print("2. Examine the small wooden chest in the southeast")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":
            
        clear()
        room9(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":
            
        if "wolf key" not in inv:

            print("\n\nYou examine the small wooden chest.  It is not locked, so you open it.")
            choice = input("\nUpon examination you find a key with an engraving of a wolf on the bow inside the box.\nDo you wish to take it? [y/n] > ")

            #run it through the validation
            choice = yes_no_choice(choice)

            if choice == "y":
                
                #add eagle key to inventory
                inv.append("wolf key")
                #print(inv)
                print("\nYou take the wolf key and close the chest.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room4(curr_loc, inv, lever, running_time, fusebox)

            else:

                print("\nYou leave the wolf key and close the chest.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room4(curr_loc, inv, lever, running_time, fusebox)

        else:

            print("\n\nYou examine the small wooden chest.  It is not locked, so you open it.")
            print("\nThe chest appears to be empty inside, so you close the chest back up.")
            print("\nYou take a moment to reassess your surroundings.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room4(curr_loc, inv, lever, running_time, fusebox)
                        
    else:
        success = False
        goodbye(running_time, success) 

def room5(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 5 of the maze'''

    answer = True

    print("\n\nWalking through the magical wall leads you down a long corridor.")
    print("\nAt the end of the corridor there is a solid metal door with a keypad next to it.")
    print("You think to yourself, 'kind of weird it would from a magical threshold to a door with technology', but alas, here we are...")

    while answer:

        print("\nOn the door is a piece of paper which reads:\n\n\t\t\t'I am the smallest even number you can form with 6 unique numbers, what am I?'")
        choice = input("\nWhat number do you enter into the keypad?  >")

        if choice == "102346":
            
            print("\n\nYou hear the door unlatch and the door swings open before you...")
            input("\n\nPress ENTER to continue: >")
            answer = False
            success = True
            goodbye(running_time, success)

        else:

            print("\n\nThe keypad beeps twice and reads 'Incorrect'")

def room6(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 6 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 7: 

        print("\n\nYou enter the room from the east.\n")

    #update location
    curr_loc = 6

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is closed door on the east side of the room")
    print("\tThere is a massive ornate chest in the northwest corner of the room")
    
    #present options
    print("\n\n1. Examine the closed door to the east")
    print("2. Examine the massive ornate chest in the northwest corner of the room")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Examine the closed door to the east")
        print("2. Examine the massive ornate chest in the northwest corner of the room")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        print("\n\nAs you approach the heavy wooden door, you notice an bear engraved on the escutcheon, just above the door handle. You jiggle the handle to find out it is locked.\n\n")    
        print("It seems the key you found with the bear engraved on the bow would be the perfect fit for this door.")
        print("\nYou slide the key into the lock and turn until the deadbolt releases and the door opens.")
        print("\nYou push through the door and ensure you take your key with you.")
        input("\n\nPress Enter to continue: >")
        clear()
        room7(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":
            
        if "skeleton key" in inv:

            if "lighter" not in inv:

                print("\n\nYou examine the massive ornate chest and notice it has an old fashioned locking mechanism that a skeleton key would fit.  You insert the skeleton key you found earlier and unlock the chest")
                print("\nWith such a massive chest, you can only imagine what you might find inside!")
                choice = input("\nUpon examination you find a lighter inside the box. Well, that seems quite underwhelming!\nDo you wish to take it? [y/n] > ")

                #run it through the validation
                choice = yes_no_choice(choice)

                if choice == "y":
                    
                    #add lighter to inventory
                    inv.append("lighter")
                    #print(inv)
                    print("\nYou take the lighter and close the chest back up.")
                    print("\nYou take a moment to reassess your surroundings.")
                    input("\n\nPress ENTER to continue: > ")
                    clear()
                    room6(curr_loc, inv, lever, running_time, fusebox)

                else:

                    print("\nYou leave the lighter and close the chest back up.")
                    print("\nYou take a moment to reassess your surroundings.")
                    input("\n\nPress ENTER to continue: > ")
                    clear()
                    room6(curr_loc, inv, lever, running_time, fusebox)

            else:

                print("\n\nYou examine the massive ornate chest and notice it has an old fashioned locking mechanism that a skeleton key would fit.  You insert the skeleton key you found earlier and unlock the chest")
                print("\nThe chest appears to be empty inside, so you close the chest back up.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room6(curr_loc, inv, lever, running_time, fusebox)
    
        else:

            print("\n\nYou examine the massive ornate chest and notice it has an old fashioned locking mechanism that a skeleton key would fit.")
            print("\nYou don't seem to have the key to unlock it at this time, so you again observe your environment.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room6(curr_loc, inv, lever, running_time, fusebox)
                        
    else:
        success = False
        goodbye(running_time, success) 

def room7(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 7 of the maze'''
    
    #customize first line for room based on where the user is coming from
    if curr_loc == 6: 

        print("\n\nYou enter the room from the west.\n")

    else:

        print("\n\nYou enter the room from the south.\n")

    #update location
    curr_loc = 7
    #inv.append("bear key") #for testing
    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the south side of the room")
    print("\tThere is a closed door on the west side of the room")
        
    #present options
    print("\n\n1. Go through the door to the south")
    print("2. Examine the closed door to the west")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the south")
        print("2. Examine the closed door to the west")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":
        
        clear()
        room12(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":

        print("\n\nAs you approach the heavy wooden door, you notice a bear engraved on the escutcheon, just above the door handle. You jiggle the handle to find out it is locked.\n\n")
        
        if "bear key" not in inv:

            print("\nIt appears you don't have the right key for this door.")
            print("\nYou better take a look at your surroundings.")
            input("\n\nPress ENTER to continue: >")
            clear()
            room7(curr_loc, inv, lever, running_time, fusebox)

        else:

            print("It seems the key you found with the bear engraved on the bow would be the perfect fit for this door.")
            print("\nYou slide the key into the lock and turn until the deadbolt releases and the door opens.")
            print("\nYou push through the door and ensure you take your key with you.")
            input("\n\nPress Enter to continue: >")
            clear()
            room6(curr_loc, inv, lever, running_time, fusebox)
            
    else:
        success = False
        goodbye(running_time, success) 

def room8(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 8 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 3: 

        print("\n\nYou enter the room from the north.\n")

    elif curr_loc == 13:

        print("\n\nYou enter the room from the south.\n")

    else:

        print("\n\nYou enter the room from the east.\n")
        
    #update location
    curr_loc = 8

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is an open door on the north side of the room")
    print("\tThere is an open door on the south side of the room")
    
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Go through the door to the north")
    print("3. Go through the door to the south")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Go through the door to the north")
        print("3. Go through the door to the south")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    if choice == "1":
        
        clear()
        room9(curr_loc, inv, lever, running_time, fusebox)
       
    elif choice == "2":
        
        clear()
        room3(curr_loc, inv, lever, running_time, fusebox)

    elif choice == "3":
        
        clear()
        room13(curr_loc, inv, lever, running_time, fusebox)
    
    else:
        success = False
        goodbye(running_time, success) 

def room9(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 9 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 4: 

        print("\n\nYou enter the room from the north.\n")

    elif curr_loc == 8:

        print("\n\nYou enter the room from the west.\n")

    elif curr_loc == 10:

        print("\n\nYou enter the room from the east.\n")
        
    #update location
    curr_loc = 9

    if lever == 0:

        #give desc of room and options
        print("After getting a good look around, you notice the following:\n")
        print("\tThere is an open door on the west side of the room")
        print("\tThere is a large lever in the center of the room")

        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Examine the lever in the center of the room")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

        #create user trap to ensure proper input
        while choice != "1" and choice != "2" and choice.upper() != "Q":

            print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
            #present options
            print("\n\n1. Go through the door to the west")
            print("2. Examine the lever in the center of the room")
            choice = input("\nEnter your selection: 1, 2, or Q > ")

        if choice == "1":
        
            clear()
            room8(curr_loc, inv, lever, running_time, fusebox)
        
        elif choice == "2":
        
            print("You examine the lever. It is currently in the western position, but it appears you can move it between three positions: western, central, and eastern.")
                        
            #present options
            print("\n\n1. Keep the lever in the western position")
            print("2. Move the lever to the central position")
            print("3. Move the lever to the eastern position")
            choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

            #create user trap to ensure proper input
            while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

                print("\n\n1. Keep the lever in the western position")
                print("2. Move the lever to the central position")
                print("3. Move the lever to the eastern position")
                choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

            if choice == "1":
                
                print("You take a step back and observe your surroundings.")
                clear()
                room9(curr_loc, inv, lever, running_time, fusebox)

            elif choice == "2":

                print("\nYou move the lever to the central position.")
                print("\nThe room starts to rumble a bit.")
                print("\nA large concrete slap rises from the ground and blocks off access to the door to the west.")
                print("\nSimultaneously, a large concrete slab sinks into the ground on the northern wall, leaving an opening to pass through.")
                lever = 1
                input("\n\nPress ENTER to coninue: >")
                clear()
                room9(curr_loc, inv, lever, running_time, fusebox)

            elif choice == "3":

                print("\nYou move the lever to the eastern position.")
                print("\nThe room starts to rumble a bit.")
                print("\nA large concrete slap rises from the ground and blocks off access to the door to the west.")
                print("\nSimultaneously, a large concrete slab sinks into the ground on the eastern wall, leaving an opening to pass through.")
                lever = 2
                input("\n\nPress ENTER to coninue: >")
                clear()
                room9(curr_loc, inv, lever, running_time, fusebox)

            else:
                success = False
                goodbye(running_time, success) 

        else:
            success = False
            goodbye(running_time, success)

    elif lever == 1:

        #give desc of room and options
        print("After getting a good look around, you notice the following:\n")
        print("\tThere is an open door on the north side of the room")
        print("\tThere is a large lever in the center of the room")

        #present options
        print("\n\n1. Go through the door to the north")
        print("2. Examine the lever in the center of the room")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

        #create user trap to ensure proper input
        while choice != "1" and choice != "2" and choice.upper() != "Q":

            print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
            #present options
            print("\n\n1. Go through the door to the north")
            print("2. Examine the lever in the center of the room")
            choice = input("\nEnter your selection: 1, 2, or Q > ")

        if choice == "1":
        
            clear()
            room4(curr_loc, inv, lever, running_time, fusebox)
        
        elif choice == "2":
        
            print("You examine the lever. It is currently in the central position, but it appears you can move it between three positions: western, central, and eastern.")
                        
            #present options
            print("\n\n1. Move the lever to the western position")
            print("2. Keep the lever in the central position")
            print("3. Move the lever to the eastern position")
            choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

            #create user trap to ensure proper input
            while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

                print("\n\n1. Move the lever to the western position")
                print("2. Keep the lever in the central position")
                print("3. Move the lever to the eastern position")
                choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

            if choice == "1":
                
                print("\nYou move the lever to the western position.")
                print("\nThe room starts to rumble a bit.")
                print("\nA large concrete slap rises from the ground and blocks off access to the door to the north.")
                print("\nSimultaneously, a large concrete slab sinks into the ground on the western wall, leaving an opening to pass through.")
                lever = 0
                input("\n\nPress ENTER to coninue: >")
                clear()
                room9(curr_loc, inv, lever, running_time, fusebox)
                

            elif choice == "2":

                print("You take a step back and observe your surroundings.")
                clear()
                room9(curr_loc, inv, lever, running_time, fusebox)

            elif choice == "3":

                print("\nYou move the lever to the eastern position.")
                print("\nThe room starts to rumble a bit.")
                print("\nA large concrete slap rises from the ground and blocks off access to the door to the north.")
                print("\nSimultaneously, a large concrete slab sinks into the ground on the eastern wall, leaving an opening to pass through.")
                lever = 2
                input("\n\nPress ENTER to coninue: >")
                clear()
                room9(curr_loc, inv, lever, running_time, fusebox)

            else:
                success = False
                goodbye(running_time, success) 

        else:
            success = False
            goodbye(running_time, success)

    else:

        #give desc of room and options
        print("After getting a good look around, you notice the following:\n")
        print("\tThere is an open door on the east side of the room")
        print("\tThere is a large lever in the center of the room")

        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Examine the lever in the center of the room")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

        #create user trap to ensure proper input
        while choice != "1" and choice != "2" and choice.upper() != "Q":

            print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
            #present options
            print("\n\n1. Go through the door to the east")
            print("2. Examine the lever in the center of the room")
            choice = input("\nEnter your selection: 1, 2, or Q > ")

        if choice == "1":
        
            clear()
            room10(curr_loc, inv, lever, running_time, fusebox)
        
        elif choice == "2":
        
            print("You examine the lever. It is currently in the eastern position, but it appears you can move it between three positions: western, central, and eastern.")
                        
            #present options
            print("\n\n1. Move the lever to the western position")
            print("2. Move the lever to the central position")
            print("3. Keep the lever in the eastern position")
            choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

            #create user trap to ensure proper input
            while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

                print("\n\n1. Move the lever to the western position")
                print("2. Move the lever to the central position")
                print("3. Keep the lever in the eastern position")
                choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

            if choice == "1":
                
                print("\nYou move the lever to the western position.")
                print("\nThe room starts to rumble a bit.")
                print("\nA large concrete slap rises from the ground and blocks off access to the door in the east.")
                print("\nSimultaneously, a large concrete slab sinks into the ground on the western wall, leaving an opening to pass through.")
                lever = 0
                input("\n\nPress ENTER to coninue: >")
                clear()
                room9(curr_loc, inv, lever, running_time, fusebox)
                

            elif choice == "2":

                print("\nYou move the lever to the central position.")
                print("\nThe room starts to rumble a bit.")
                print("\nA large concrete slap rises from the ground and blocks off access to the door in the east.")
                print("\nSimultaneously, a large concrete slab sinks into the ground on the northern wall, leaving an opening to pass through.")
                lever = 1
                input("\n\nPress ENTER to coninue: >")
                clear()
                room9(curr_loc, inv, lever, running_time, fusebox)  

            elif choice == "3":

                print("You take a step back and observe your surroundings.")
                clear()
                room9(curr_loc, inv, lever, running_time, fusebox)

            else:
                success = False
                goodbye(running_time, success) 

        else:
            success = False
            goodbye(running_time, success)  

def room10(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 10 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 9: 

        print("\n\nYou enter the room from the west.\n")

    #update location
    curr_loc = 10

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the west side of the room")
    print("\tThere is a small wooden chest in the southeast")
    print("\tThere is a sconce a few feet off center on the northern wall")
    
    #present options
    print("\n\n1. Go through the door to the west")
    print("2. Examine the small wooden chest in the southeast")
    print("3. Examine the sconce on the northern wall")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Examine the small wooden chest in the southeast")
        print("3. Examine the sconce on the northern wall")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    if choice == "1":
            
        clear()
        room9(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":
            
        if "bear key" not in inv:

            print("\n\nYou examine the small wooden chest.  It is not locked, so you open it.")
            choice = input("\nUpon examination you find a key with an engraving of a bear on the bow inside the box.\nDo you wish to take it? [y/n] > ")

            #run it through the validation
            choice = yes_no_choice(choice)

            if choice == "y":
                
                #add bear key to inventory
                inv.append("bear key")
                #print(inv)
                print("\nYou take the bear key and close the chest.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room10(curr_loc, inv, lever, running_time, fusebox)

            else:

                print("\nYou leave the bear key and close the chest.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room10(curr_loc, inv, lever, running_time, fusebox)

        else:

            print("\n\nYou examine the small wooden chest.  It is not locked, so you open it.")
            print("\nThe chest appears to be empty inside, so you close the chest back up.")
            print("\nYou take a moment to reassess your surroundings.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room10(curr_loc, inv, lever, running_time, fusebox)

    elif choice == "3":
            
        if "placed candle" not in inv: #used candle represents the candle being already placed in the sconce, rather than having a candle in inv

            print("\n\nYou examine the ornate sconce on the northern wall.  You wonder why there is no candle in the sconce.")

            if "candle" not in inv:

                print("\nMaybe you can find a candle somewhere else in the maze.")
                print("\nThere doesn't seem to be much else you can do with the sconce at this time.")
                input("\n\nPress Enter to continue: >")
                clear()
                room10(curr_loc, inv, lever, running_time, fusebox)

            else: 

                choice = input("\nWould you like to place the candle you found in the sconce? [y/n] > ")

                #run it through the validation
                choice = yes_no_choice(choice)

                if choice == "y":
                    
                    #remove candle from inv and add placed candle to inventory
                    inv.remove("candle")
                    inv.append("placed candle")
                    #print(inv)
                    print("\nYou place the candle in the sconce and it seems to fit perfectly.")
                    print("\nAlthough it fit, it didn't seem to have any special effect. \nMaybe if you could light the candle.")

                    if "lighter" in inv:
                        
                        print("\nIt just so happens you found that lighter in the ornate chest earlier")
                        print("\nYou light the candle and you start to hear some rumbling again.")
                        print("\nYou can't believe your eyes as pieces of the wall in front of you start seperating, brick by brick, opening a hole in the wall large enough for you to pass through.")
                        print("\nAlmost as if by magical force, you are compelled to walk into the next room. As you cross the threshold, the wall reconstructs itself behind you.")
                        input("Press Enter to continue: >")
                        clear()
                        room5(curr_loc, inv, lever, running_time, fusebox)
                    
                    else:
                        
                        print("\nYou don't have a means to light the candle at this time.\nThere doesn't seem to be much else you can do with the sconce at this time.")
                        print("\nYou take a moment to reassess your surroundings.")
                        input("\n\nPress ENTER to continue: > ")
                        clear()
                        room10(curr_loc, inv, lever, running_time, fusebox)

                else:

                    print("\nYou decide not to place the candle and take a few steps back.")
                    print("\nYou take a moment to reassess your surroundings.")
                    input("\n\nPress ENTER to continue: > ")
                    clear()
                    room10(curr_loc, inv, lever, running_time, fusebox)

        elif "lighter" in inv:
                        
            print("\nYou've come back prepared now that you found that lighter in the ornate chest earlier")
            print("\nYou light the candle and you start to hear some rumbling again.")
            print("\nYou can't believe your eyes as pieces of the wall in front of you start seperating, brick by brick, opening a hole in the wall large enough for you to pass through.")
            print("\nAlmost as if by magical force, you are compelled to walk into the next room. As you cross the threshold, the wall reconstructs itself behind you.")
            input("\n\nPress Enter to continue: >")
            clear()
            room5(curr_loc, inv, lever, running_time, fusebox)
                    
        else:
            
            print("\nThe sconce still has the candle in it that you placed earlier.")
            print("\nYou still don't have a means to light the candle at this time.\nThere doesn't seem to be much else you can do with the sconce at this time.")
            print("\nYou take a moment to reassess your surroundings.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room10(curr_loc, inv, lever, running_time, fusebox)

    else:
        success = False
        goodbye(running_time, success)  

def room11(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 11 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 16: 

        print("\n\nYou enter the room from the south.\n")

    #update location
    curr_loc = 11

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the south side of the room")
    print("\tThere is a small chest in the northeast corner of the room")
    
    #present options
    print("\n\n1. Go through the door to the south")
    print("2. Examine the small chest in the northeast corner of the room")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the south")
        print("2. Examine the small chest in the northeast corner of the room")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":
            
        clear()
        room16(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":
            
        print("\n\nYou examine the small chest, which is not locked and opens easily.")
        print("\nThe chest appears to be empty inside, so you close the chest back up.")
        print("\nYou take a moment to reassess your surroundings.")
        input("\n\nPress ENTER to continue: > ")
        clear()
        room11(curr_loc, inv, lever, running_time, fusebox)
                        
    else:
        success = False
        goodbye(running_time, success) 

def room12(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 12 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 7: 

        print("\n\nYou enter the room from the north.\n")

    elif curr_loc == 17:

        print("\n\nYou enter the room from the south.\n")

    else:

        print("\n\nYou enter the room from the east.\n")
        
    #update location
    curr_loc = 12

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is an open door on the north side of the room")
    print("\tThere is an open door on the south side of the room")
    
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Go through the door to the north")
    print("3. Go through the door to the south")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Go through the door to the north")
        print("3. Go through the door to the south")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    if choice == "1":
        
        clear()
        room13(curr_loc, inv, lever, running_time, fusebox)
       
    elif choice == "2":
        
        clear()
        room7(curr_loc, inv, lever, running_time, fusebox)

    elif choice == "3":
        
        clear()
        room17(curr_loc, inv, lever, running_time, fusebox)
    
    else:
        success = False
        goodbye(running_time, success) 

def room13(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 13 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 12: 

        print("\n\nYou enter the room from the west.\n")

    else:

        print("\n\nYou enter the room from the north.\n")
        
    #update location
    curr_loc = 13

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the west side of the room")
    print("\tThere is an open door on the north side of the room")
    
    #present options
    print("\n\n1. Go through the door to the west")
    print("2. Go through the door to the north")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Go through the door to the north")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        clear()    
        room12(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":
        
        clear()
        room8(curr_loc, inv, lever, running_time, fusebox)
    
    else:

        success = False
        goodbye(running_time, success) 

def room14(curr_loc, inv, lever, running_time, fusebox):

    '''Room 14 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 15: 

        print("\n\nYou enter the room from the east.\n")

    else:

        print("\n\nYou enter the room from the south.\n")
        
    #update location
    curr_loc = 14

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is an open door on the south side of the room")
    
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Go through the door to the south")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Go through the door to the south")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        clear()    
        room15(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":
        
        clear()
        room19(curr_loc, inv, lever, running_time, fusebox)
    
    else:

        success = False
        goodbye(running_time, success)

def room15(curr_loc, inv, lever, running_time, fusebox):

    '''Room 15 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 14: 

        print("\n\nYou enter the room from the west.\n")

    #update location
    curr_loc = 15

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the west side of the room")
    print("\tThere is chest in the southeast corner of the room")
    
    #present options
    print("\n\n1. Go through the door to the west")
    print("2. Examine the chest in the southeast corner of the room")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Examine the chest in the southeast corner of the room")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":
            
        clear()
        room14(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":
            
        if "small key" in inv:

            if "fuse" not in inv:

                print("\n\nYou examine the chest and notice that it is locked. A small key you found earlier appears to fit and you manage to unlock the chest.")
                choice = input("\nUpon examination you find a fuse inside the box.\nDo you wish to take it? [y/n] > ")

                #run it through the validation
                choice = yes_no_choice(choice)

                if choice == "y":
                    
                    #add fuse to inventory
                    inv.append("fuse")
                    #print(inv)
                    print("\nYou take the fuse and lock the chest.")
                    print("\nYou take a moment to reassess your surroundings.")
                    input("\n\nPress ENTER to continue: > ")
                    clear()
                    room15(curr_loc, inv, lever, running_time, fusebox)

                else:

                    print("\nYou leave the fuse and close the chest.")
                    print("\nYou take a moment to reassess your surroundings.")
                    input("\n\nPress ENTER to continue: > ")
                    clear()
                    room15(curr_loc, inv, lever, running_time, fusebox)

            else:

                print("\n\nYou examine the chest and notice that it is locked. A small key you found earlier appears to fit and you manage to unlock the chest.")
                print("\nThe chest appears to be empty inside, so you close the chest back up.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room15(curr_loc, inv, lever, running_time, fusebox)
    
        else:

            print("\n\nYou examine the chest and see that it is locked. The lock appears to be quite small.")
            print("\nYou don't seem to have the key to unlock it at this time, so you again observe your environment.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room15(curr_loc, inv, lever, running_time, fusebox)
            
    else:
        success = False
        goodbye(running_time, success) 

def room16(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 16 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 11: 

        print("\n\nYou enter the room from the north.\n")

    elif curr_loc == 21:

        print("\n\nYou enter the room from the south.\n")

    else:

        print("\n\nYou enter the room from the east.\n")
        
    #update location
    curr_loc = 16

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is an open door on the north side of the room")
    print("\tThere is an open door on the south side of the room")
    
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Go through the door to the north")
    print("3. Go through the door to the south")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Go through the door to the north")
        print("3. Go through the door to the south")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    if choice == "1":
        
        clear()
        room17(curr_loc, inv, lever, running_time, fusebox)
       
    elif choice == "2":
        
        clear()
        room11(curr_loc, inv, lever, running_time, fusebox)

    elif choice == "3":
        
        clear()
        room21(curr_loc, inv, lever, running_time, fusebox)
    
    else:
        success = False
        goodbye(running_time, success) 

def room17(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 17 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 16: 

        print("\n\nYou enter the room from the west.\n")

    else:

        print("\n\nYou enter the room from the north.\n")
        
    #update location
    curr_loc = 17

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the west side of the room")
    print("\tThere is an open door on the north side of the room")
    
    #present options
    print("\n\n1. Go through the door to the west")
    print("2. Go through the door to the north")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Go through the door to the north")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        clear()    
        room16(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":
        
        clear()
        room12(curr_loc, inv, lever, running_time, fusebox)
    
    else:

        success = False
        goodbye(running_time, success) 

def room18(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 18 of the maze (Starting Room)'''
    
    #customize first line for room based on where the user is coming from
    if curr_loc == 0: 

        print("\n\nYou open your eyes and find yourself in the center of a room.\n")

    elif curr_loc == 19:

        print("\n\nYou enter the room from the east.\n")

    elif curr_loc == 23:

        print("\n\nYou enter the room from the south.\n")
        
    #update location
    curr_loc = 18

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is an open door on the south side of the room")
       
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Go through the door to the south")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Go through the door to the south")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":
                
        clear()
        room19(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":

        clear()
        room23(curr_loc, inv, lever, running_time, fusebox)
  
    else:
        success = False
        goodbye(running_time, success)

def room19(curr_loc, inv, lever, running_time, fusebox):

    '''Room 19 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 14: 

        print("\n\nYou enter the room from the north.\n")

    elif curr_loc == 18:

        print("\n\nYou enter the room from the west.\n")

    else:

        print("\n\nYou enter the room from the east.\n")
        
    #update location
    curr_loc = 19

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is an open door on the north side of the room")
    print("\tThere is an open door on the west side of the room")
    
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Go through the door to the north")
    print("3. Go through the door to the west")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Go through the door to the north")
        print("3. Go through the door to the west")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    if choice == "1":
        
        clear()
        room20(curr_loc, inv, lever, running_time, fusebox)
       
    elif choice == "2":
        
        clear()
        room14(curr_loc, inv, lever, running_time, fusebox)

    elif choice == "3":
        
        clear()
        room18(curr_loc, inv, lever, running_time, fusebox)
    
    else:
        success = False
        goodbye(running_time, success)
     
def room20(curr_loc, inv, lever, running_time, fusebox):

    '''Room 20 of the maze'''
    
    #customize first line for room based on where the user is coming from
    print("\n\nYou enter the room from the west.\n")

    #update location
    curr_loc = 20

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the west side of the room")
    print("\tThere is a small wooden chest in the northeast")
    
    #present options
    print("\n\n1. Go through the door to the west")
    print("2. Examine the small wooden chest in the northeast")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Examine the small wooden chest in the northeast")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":
            
        clear()
        room19(curr_loc, inv, lever, running_time, fusebox)

    elif choice == "2":

        if "small key" not in inv:

            print("\n\nYou pick pick up a small box and open the lid.")
            choice = input("\nThere is a small key inside the box. Do you wish to take it? [y/n] > ")

            #run it through the validation
            choice = yes_no_choice(choice)

            if choice == "y":
                
                #add key to inventory
                inv.append("small key")
                #print(inv)
                print("\nYou take the key and put the box back on the ground.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room20(curr_loc, inv, lever, running_time, fusebox)

            else:

                print("\nYou leave the key and put the box back on the ground.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room20(curr_loc, inv, lever, running_time, fusebox)
            
        else:

            print("\n\nYou pick pick up a small box and open the lid.")
            print("\nThe box appears to be empty, so you place it back down and observe your environment.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room20(curr_loc, inv, lever, running_time, fusebox)

def room21(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 21 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 16: 

        print("\n\nYou enter the room from the north.\n")

    else:

        print("\n\nYou enter the room from the south.\n")
        
    #update location
    curr_loc = 21

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is a closed metallic door on the south side of the room")
    print("\tThere is an open door on the north side of the room")
    
    #present options
    print("\n\n1. Examine the closed metallic door to the south")
    print("2. Go through the door to the north")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Examine the closed metallic door to the south")
        print("2. Go through the door to the north")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        print("\n\nAs you approach the metallic door, you notice there is button on the wall nearby. You press the button.\n\n")
        print("\nThe door slides apart from the middle and closes behind you as you pass through it.")
        input("\n\nPress Enter to continue: >")
        clear()
        room26(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":
        
        clear()
        room16(curr_loc, inv, lever, running_time, fusebox)
    
    else:

        success = False
        goodbye(running_time, success)

def room22(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 22 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 23: 

        print("\n\nYou enter the room from the east.\n")

    else:

        print("\n\nYou enter the room from the south.\n")
        
    #update location
    curr_loc = 22

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is a closed door on the east side of the room")
    print("\tThere is an open door on the south side of the room")
    
    #present options
    print("\n\n1. Examine the closed door to the east")
    print("2. Go through the door to the south")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Examine the closed door to the east")
        print("2. Go through the door to the south")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        print("\n\nAs you approach the heavy wooden door, you notice an eagle engraved on the escutcheon, just above the door handle. You jiggle the handle to find out it is locked.\n\n")    
        print("It seems the key you found with the eagle engraved on the bow would be the perfect fit for this door.")
        print("\nYou slide the key into the lock and turn until the deadbolt releases and the door opens.")
        print("\nYou push through the door and ensure you take your key with you.")
        input("\n\nPress Enter to continue: >")
        clear()
        room23(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":
        
        clear()
        room27(curr_loc, inv, lever, running_time, fusebox)
    
    else:

        success = False
        goodbye(running_time, success) 

def room23(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 23 of the maze'''
    
    #customize first line for room based on where the user is coming from
    if curr_loc == 18: 

        print("\n\nYou enter the room from the north.\n")

    elif curr_loc == 22:

        print("\n\nYou enter the room from the west.\n")

    elif curr_loc == 28:

        print("\n\nYou enter the room from the south.\n")

    elif curr_loc == 24:

        print("\n\nYou enter the room from the east.\n")
        
    #update location
    curr_loc = 23
    #inv.append("eagle key") #for testing
    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is an open door on the north side of the room")
    print("\tThere is a closed door on the west side of the room")
    print("\tThere is a closed door on the south side of the room")
    
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Go through the door to the north")
    print("3. Examine the closed door to the west")
    print("4. Examine the closed door to the south")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, 3, 4, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Go through the door to the north")
        print("3. Examine the closed door to the west")
        print("4. Examine the closed to the south")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, 3, 4, or Q > ")

    if choice == "1":
        
        clear()
        room24(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":

        clear()
        room18(curr_loc, inv, lever, running_time, fusebox)

    elif choice == "3":

        print("\n\nAs you approach the heavy wooden door, you notice an eagle engraved on the escutcheon, just above the door handle. You jiggle the handle to find out it is locked.\n\n")
        
        if "eagle key" not in inv:

            print("\nIt appears you don't have the right key for this door.")
            print("\nYou better take a look at your surroundings.")
            input("\n\nPress ENTER to continue: >")
            clear()
            room23(curr_loc, inv, lever, running_time, fusebox)

        else:

            print("It seems the key you found with the eagle engraved on the bow would be the perfect fit for this door.")
            print("\nYou slide the key into the lock and turn until the deadbolt releases and the door opens.")
            print("\nYou push through the door and ensure you take your key with you.")
            input("\n\nPress Enter to continue: >")
            clear()
            room22(curr_loc, inv, lever, running_time, fusebox)
            
    elif choice == "4": 

        print("\n\nAs you approach the heavy wooden door, you notice an eagle engraved on the escutcheon, just above the door handle. You jiggle the handle to find out it is locked.\n\n")

        if "eagle key" not in inv:

            print("\nIt appears you don't have the right key for this door.")
            print("\nYou better take a look at your surroundings.")
            input("\n\nPress ENTER to continue: >")
            clear()
            room23(curr_loc, inv, lever, running_time, fusebox)

        else:

            print("It seems the key you found with the eagle engraved on the bow would be the perfect fit for this door.")
            print("\nYou slide the key into the lock and turn until the deadbolt releases and the door opens.")
            print("\nYou push through the door and ensure you take your key with you.")
            input("\n\nPress Enter to continue: >")
            clear()
            room28(curr_loc, inv, lever, running_time, fusebox)
    
    else:
        success = False
        goodbye(running_time, success)

def room24(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 24 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 23: 

        print("\n\nYou enter the room from the west.\n")

    else:

        print("\n\nYou enter the room from the south.\n")
        
    #update location
    curr_loc = 24

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the west side of the room")
    print("\tThere is an open door on the south side of the room")
    
    #present options
    print("\n\n1. Go through the door to the west")
    print("2. Go through the door to the south")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Go through the door to the south")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        clear()    
        room23(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":
        
        clear()
        room29(curr_loc, inv, lever, running_time, fusebox)
    
    else:

        success = False
        goodbye(running_time, success) 

def room25(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 25 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 30: 

        print("\n\nYou enter the room from the south.\n")

    #update location
    curr_loc = 25

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the south side of the room")
    print("\tThere is a metallic chest in the northwest corner of the room")
    
    #present options
    print("\n\n1. Go through the door to the south")
    print("2. Examine the metallic chest in the northwest corner of the room")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the south")
        print("2. Examine the metallic chest in the northwest corner of the room")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":
            
        clear()
        room30(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":
            
        if "eagle key" not in inv:

            print("\n\nYou examine the metallic chest and notice there is a small switch on the lid. You toggle the switch and the lid opens.")
            choice = input("\nUpon examination you find a key with an engraving of an eagle on the bow inside the box.\nDo you wish to take it? [y/n] > ")

            #run it through the validation
            choice = yes_no_choice(choice)

            if choice == "y":
                
                #add eagle key to inventory
                inv.append("eagle key")
                #print(inv)
                print("\nYou take the eagle key and close the chest.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room25(curr_loc, inv, lever, running_time, fusebox)

            else:

                print("\nYou leave the eagle key and close the chest.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room25(curr_loc, inv, lever, running_time, fusebox)

        else:

            print("\n\nYou examine the metallic chest and notice there is a small switch on the lid. You toggle the switch and the lid opens.")
            print("\nThe chest appears to be empty inside, so you close the chest back up.")
            print("\nYou take a moment to reassess your surroundings.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room25(curr_loc, inv, lever, running_time, fusebox)
                        
    else:
        success = False
        goodbye(running_time, success) 

def room26(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 26 of the maze'''
    
    #customize first line for room based on where the user is coming from
    if curr_loc == 21: 

        print("\n\nYou enter the room from the north.\n")

    elif curr_loc == 27:

        print("\n\nYou enter the room from the east.\n")
        
    #update location
    curr_loc = 26
        
    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is closed metallic door on the north side of the room")
    print("\tThere is a small metallic panel in the northwest of the room")
    
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Examine the closed metallic door to the north")
    print("3. Examine the small metallic panel in the northwest of the room")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Examine the closed metallic door to the north")
        print("3. Examine the small metallic panel in the northwest of the room")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    if choice == "1":
                
        clear()
        room27(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":

        print("\n\nAs you approach the metallic door, you notice there is button on the wall nearby. You press the button.\n\n")
        
        if fusebox:

            print("It seems the fuse you put in the fusebox must have given power to the door.")
            print("\nThe door slides apart from the middle and closes behind you as you pass through it.")
            input("\n\nPress Enter to continue: >")
            clear()
            room21(curr_loc, inv, lever, running_time, fusebox)
        
        else:

            print("\nPressing the button doesn't seem to have any effect. Maybe the door is lacking power.")
            print("\nYou better take a look at your surroundings.")
            input("\n\nPress ENTER to continue: >")
            clear()
            room26(curr_loc, inv, lever, running_time, fusebox)
                    
    elif choice == "3":

        print("\n\nAs you approach the small metallic panel, it is slightly ajar and you notice it is a fusebox and you open it fully.\n\n")
        
        if fusebox:

            print("\nThis looks like the fuse box you inspected earlier and replaced the missing fuse. You should find out what it sent power to.")
            print("\nYou better take a look at your surroundings.")
            input("\n\nPress ENTER to continue: >")
            clear()
            room26(curr_loc, inv, lever, running_time, fusebox)
        
        elif "fuse" not in inv:

            print("\nThere appears to be a fuse missing from the box. Maybe you need to find a fuse somewhere to replace it.")
            print("\nYou better take a look at your surroundings.")
            input("\n\nPress ENTER to continue: >")
            clear()
            room26(curr_loc, inv, lever, running_time, fusebox)
 
        else:

            print("There appears to be a fuse missing from the box.")
            print("\nYou dig the fuse you found earlier out of your pocket and place it in the fusebox.")
            print("\nYou hear a small electric hum as if there was some power restored nearby.")
            fusebox = True
            inv.remove("fuse")
            input("\n\nPress Enter to continue: >")
            clear()
            room26(curr_loc, inv, lever, running_time, fusebox)
    
    else:
        success = False
        goodbye(running_time, success) 

def room27(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 27 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 26: 

        print("\n\nYou enter the room from the west.\n")

    else:

        print("\n\nYou enter the room from the north.\n")
        
    #update location
    curr_loc = 27

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the west side of the room")
    print("\tThere is an open door on the north side of the room")
    
    #present options
    print("\n\n1. Go through the door to the west")
    print("2. Go through the door to the north")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Go through the door to the north")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        clear()    
        room26(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":
        
        clear()
        room22(curr_loc, inv, lever, running_time, fusebox)
    
    else:

        success = False
        goodbye(running_time, success) 

def room28(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 28 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 23: 

        print("\n\nYou enter the room from the north.\n")

    #update location
    curr_loc = 28

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is closed door on the north side of the room")
    print("\tThere is a small stool in the southeast corner of the room")
    
    #present options
    print("\n\n1. Examine the closed door to the north")
    print("2. Examine the small stool in the southeast corner of the room")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Examine the closed door to the north")
        print("2. Examine the small stool in the southeast corner of the room")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        print("\n\nAs you approach the heavy wooden door, you notice an eagle engraved on the escutcheon, just above the door handle. You jiggle the handle to find out it is locked.\n\n")    
        print("It seems the key you found with the eagle engraved on the bow would be the perfect fit for this door.")
        print("\nYou slide the key into the lock and turn until the deadbolt releases and the door opens.")
        print("\nYou push through the door and ensure you take your key with you.")
        input("\n\nPress Enter to continue: >")
        clear()
        room23(curr_loc, inv, lever, running_time, fusebox)
    
    elif choice == "2":
            
        if "skeleton key" not in inv:

            choice = input("\nUpon examination of the small stool, you find a skeleton key on top of it.\nDo you wish to take it? [y/n] > ")

            #run it through the validation
            choice = yes_no_choice(choice)

            if choice == "y":
                
                #add skeleton key to inventory
                inv.append("skeleton key")
                #print(inv)
                print("\nYou take the skeleton key and back away from the table.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room28(curr_loc, inv, lever, running_time, fusebox)

            else:

                print("\nYou leave the skeleton key and back away from the table.")
                print("\nYou take a moment to reassess your surroundings.")
                input("\n\nPress ENTER to continue: > ")
                clear()
                room28(curr_loc, inv, lever, running_time, fusebox)

        else:

            print("\n\nYou examine the small stool and find nothing of significance.")
            print("\nYou take a moment to reassess your surroundings.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room28(curr_loc, inv, lever, running_time, fusebox)
                        
    else:
        success = False
        goodbye(running_time, success) 

def room29(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 29 of the maze'''
    
    #customize first line for room based on where the user is coming from
    if curr_loc == 24: 

        print("\n\nYou enter the room from the north.\n")

    elif curr_loc == 30:

        print("\n\nYou enter the room from the east.\n")
        
    #update location
    curr_loc = 29

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the east side of the room")
    print("\tThere is an open door on the north side of the room")
    print("\tThere is a small wooden chest in the northwest of the room")
    
    #present options
    print("\n\n1. Go through the door to the east")
    print("2. Go through the door to the north")
    print("3. Examine the small wooden chest in the northwest of the room")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice != "3" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the east")
        print("2. Go through the door to the north")
        print("3. Examine the small wooden chest in the northwest of the room")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, 3, or Q > ")

    if choice == "1":
                
        clear()
        room30(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":

        clear()
        room24(curr_loc, inv, lever, running_time, fusebox)
                    
    elif choice == "3":

            print("\n\nYou approach the small wooden chest and open the lid.")
            print("\nThe box appears to be empty, much to your chagrin, so you close it and observe your environment.")
            input("\n\nPress ENTER to continue: > ")
            clear()
            room29(curr_loc, inv, lever, running_time, fusebox)
    
    else:
        success = False
        goodbye(running_time, success)

def room30(curr_loc, inv, lever, running_time, fusebox):
    
    '''Room 30 of the maze'''

    #customize first line for room based on where the user is coming from
    if curr_loc == 29: 

        print("\n\nYou enter the room from the west.\n")

    else:

        print("\n\nYou enter the room from the north.\n")
        
    #update location
    curr_loc = 30

    #give desc of room and options
    print("After getting a good look around, you notice the following:\n")
    print("\tThere is an open door on the west side of the room")
    print("\tThere is an open door on the north side of the room")
    
    #present options
    print("\n\n1. Go through the door to the west")
    print("2. Go through the door to the north")
    print("Q. I've had enough, I'm calling it quits!")
    choice = input("\nEnter your selection: 1, 2, or Q > ")

    #create user trap to ensure proper input
    while choice != "1" and choice != "2" and choice.upper() != "Q":

        print("\n\nI don't understand what you want to do, please select a valid choice.\n\n")
        #present options
        print("\n\n1. Go through the door to the west")
        print("2. Go through the door to the north")
        print("Q. I've had enough, I'm calling it quits!")
        choice = input("\nEnter your selection: 1, 2, or Q > ")

    if choice == "1":

        clear()    
        room29(curr_loc, inv, lever, running_time, fusebox)
        
    elif choice == "2":
        
        clear()
        room25(curr_loc, inv, lever, running_time, fusebox)
    
    else:

        success = False
        goodbye(running_time, success)

#MAIN CODE----------------------------------# 

#initialize starting variables: 
curr_loc = 0
inv = []
lever = 0
fusebox = False

#welcome and rules
user_name = input("\n\nWhat is your name? ").title()
print(f"\n\nWelcome to the RC Adventure Maze, {user_name}!\n\n")
print("Rule 1: You will have to navigate a maze that has puzzles and pre-requisites to delve deeper into the maze.\n")
print("Rule 2: You will be timed on how long it takes you to finish the maze, so do your best to beat the fastest time!\n")
print("Rule 3: You will have the choice to exit the maze at many times, should you find it too difficult.\n")
print("Rule 4: You have a compass so you will know cardinal directions!\n\n")
input("When you press ENTER, a 5-second countdown will run and the maze will begin.\n\nHave fun in there!: > ")
clear()

#countdown from 5 to start the maze completion timer and begin the maze
timer = 5
while timer:

    print(f"Maze will begin in {timer}")
    sleep(1)
    timer -= 1

print("Begin!\n\n")

#start timer to later calc total time in maze
running_time = time()

#enter the maze (room 18 is the start point)
room18(curr_loc, inv, lever, running_time, fusebox)