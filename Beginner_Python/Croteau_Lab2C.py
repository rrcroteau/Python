#Name Ron Croteau
#Lab 2C
#April 18, 2021
#SE116.01
#PROGRAM PROMPT: Rewrite Lab 2B but use input statements for: the available storage of the NAS in TB,number of videos weekly, average size of each video in GB.

#Prompt from 2B:  You are currently working for a small start-up company that produces short “How-to” videos.  The company is currently producing videos for customers who need to know how to fix common networking problems. You oversee the company’s network and the owner of the company has just informed you that the company will also be producing “How-to”videos on how to install, configure and manage a Linux OS.  You need to let the owner of the company know if you will have enough storage on your current NAS (Network Attached Storage). You currently have 250 videos stored on your NAS which occupy 1.4 TB of disk space. Your NAS has 8 TB of storage.  The company is currently producing 15 videos a week with an average file size of 5.6GB.  The company expects to triple that average once they start producing videos for the OS.  If the average file size ​of each video​ is 5.6 GB how long will it be before you run out of storage space?  Tell the user how many days left of storage are available just by making their current How-To videos, as well as how many days are left if they started their How-To videos ​today​ (which increases the videos being produced weekly3x) Every output value should be format rounded to the 1​st​ decimal place.

#VARIABLE DICTIONARY:
####total_NAS --> total Network Attached Storage (NAS) in TB -->not used in 2C
#####used_NAS --> amount of NAS already used in TB -->not used in 2C
#rem_NAS --> amount of NAS remaining in TB (input)
#num_videos --> average number of videos saved weekly (input)
#avg_video_size --> average size of the videos saved in GB (input)
#rem_NAS_GB --> remaining NAS converted from TB to GB
#weeks_rem --> the number of weeks remaining at current storage rates
#days_rem --> the number of days remaining at current storage rates
#acc_days_rem --> the accelerated number of days remaining (3x the current usage)

#title/welcome
print("\n\n\t\tWelcome to the Network Attached Storage (NAS) Usage Calculator\n\n")

#total_NAS = 8  #total Network Attached Storage in TB
#used_NAS = 1.4  #used Network Attached Storage in TB
#remaining Network Attached Storage in TB from user input (was 6.6 in 2B)
rem_NAS = float(input("How much storage is remaining on the NAS (in TB): "))
#average number of videos saved weekly from user input (was 15 in 2B)
num_videos = float(input("How many videos do you save weekly to the NAS: "))
#size of average video saved to NAS in GB from user input (was 5.6 in 2B)
avg_video_size = float(input("What is the average size of the videos saved (in GB): "))   
weekly_usage = num_videos * avg_video_size  #determine the weekly usage in GB
rem_NAS_GB = rem_NAS * 1000  #convert remaining storage from TB to GB
weeks_rem = rem_NAS_GB / weekly_usage  #determine the number of weeks of storage remaining
days_rem = weeks_rem * 7 #determine the number of days of storage remaining at current usage rate 
acc_days_rem = days_rem / 3 #determine the number of days of storage remaining at triple usage rate

print("\n\n")
#output days_rem and acc_days_rem to user rounded to one decimal(should be 550.0)
print("           The number of storage days remaining at current usage is: {:.1f}".format(days_rem))
print("The number of storage days remaining at triple the current usage is: {:.1f}".format(acc_days_rem))

print("\n\n")
