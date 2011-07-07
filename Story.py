import time
import os

#Persistant (Global?) variables
#Computer "My Computer"
#   Specs:"Intel Celeron D @ 1.3 Ghz
#          RAM: 256 MB 
#          OS: MyCustomOS"
#   Files:"CoreOSFiles.bndl - Unable to read file.
#		   coreImgFiles.bndl - Unable to read file.
#		   coreScript.bndl - Unable to read file.
#		   sesCrk.txt - Pandora's (i is sqrt of: ?)
#          ses.png - Encrypted(box, -1) - 256kb image file retrieved from (http://www.elcachondo.net/"
#		   errorLog.txt - "Damn send function, I'll write it later, not like I need it to evesdrop on conversations..."
#
#currentComputer = currently logged on computer.
#currentStage = currently loaded stage.

#----------------------------------------------------------------------------------
# im(numOfSecToWait, stringToPrint)
#	So I don't have to keep typing time.sleep()
# ---------------------------------------------------------------------------------
def say(num, str):
	time.sleep(num)
	print(str)
	
#----------------------------------------------------------------------------------
# Clears the console
#----------------------------------------------------------------------------------
def clear():
	os.system(['clear', 'cls'][os.name=='nt'])

#----------------------------------------------------------------------------------
# The start of the game. Allows the user to input a password or not.
#----------------------------------------------------------------------------------
print("MyCustomOS")
time.sleep(0.4)
print("Loading CoreOSFiles")
say(0.2, "Connecting to the network")
say(0.4, "Connected")
say(0.2, "Initializing myCustomChat")
say(0.6, "Error! Send function not initialized")
say(0.2, "No friends online")
say(0.2, "Reading from USB")
say(0.4, "Now executing")
clear()

# Still don't know what the passwords will show. Will work on it later.
# if he typed a correct password
#		currentStage = whatever.
#		print("Loading DiaryFile.")
#		time.sleep(1)
#		print("Loading Complete.")
# else raw_input("Error! Please try again or press Enter")
# elif pressed enter:
#		print("No Password Detected.")
#		time.sleep(1)
#		print("Loading Complete.")
#Clear the screen somehow.

#==================================================================================
# Stage 1
#----------------------------------------------------------------------------------
# Very early in the morning.
# This takes place in the offices of Pheonixeon Corp.
# The protagonist is just starting his new job as a security consultant.
# He enters an empty room. He then inserts a USB flash drive into his computer as
# he was instructed by his manager over the phone.
#----------------------------------------------------------------------------------
#
# Computer:"Steve Waller Security Consultant" - Password Protected: password, sword
#    Specs:"Intel i7 Extreme 8 cores @ 3.4 GHz
#           RAM: 8GB
#           OS: Windows8"
#    Files: savedFile.xtr - Encrypted(really long random text, no hints)
#			employLst.lst - Encrypted(password, 8) - "No employees registered"
#			mail.hist - "From: Sally Stark
#						Hey, do you remember the encryption code for our employee
#						files?
#						
#						To: Sally Stark
#						Why do you want to know? And hey, how about dinner tonight?
#
#						From: Sally Stark
#						I told you, Steve! We're over! Now just tell me the code!!
#
#						To: Sally Stark
#						It's against policy to say! You're a receptionist! why the
#						hell would you want to know the code?!
#
#						From: Sally Stark
#						It's to help a cute new employee! I want to look smart so
#						I can ride him!! Cuz i know he'll be better than you!! Now
#						if you don't tell me I'LL TELL EVERYONE ABOUT YOUR FETISH!!
#
#						To: Sally Stark
#						FUUUCK! OKay bitch! I can't tell you directly but its the
#						amount of RAM on your computer. Its on the sticker on your
#						computer you dumb bitch.
#						P.S. I hope he gives you the aids."
#==================================================================================

managerName = "Amitav Gutipaty" #Just so I can change it easily if I want.
#imManager = managerName + "says: " #So I don't have to type "says:"

say(0, "Hello, I'm " + managerName + ".")
# Blah blah. Other intro stuff describing the reason you cant talk back and what your job is. I'll think of it later.

# Makes you scan "Steve Waller Security Consultant".
# Makes you crack password
# Makes you connect to computer
# Makes you list files
# Makes you cat employLst.lst
# Makes you cat mail.hist
# Makes you decrypt employLst.lst
# Makes you download savedFile.xtr
# Makes you disconnect
# Makes you upload savedFile.xtr to Amitav Gutipaty Manager

# He tells you that he screwed you and that you can't leave.
# Print password

#====================================================================================
# Stage 2
#------------------------------------------------------------------------------------
# The protagonist has just been told that he's been had.
#------------------------------------------------------------------------------------
# Computer:"Steve Waller Security Consultant"
#
# Computer:"Amitav Gutipaty Manager" - Password Protected: 
#	Specs: Intel i7 Extreme 8 cores @ 3.4Ghz
#		   RAM: 8GB
#		   OS: Windows8
#	Files: 
#
# Computer:"Sally Stark Receptionist" - Password Protected: 
#	Specs: Intel i7 Extreme 8 cores @ 3.4Ghz
#		   RAM: 8GB
#		   OS: Windows8
#	Files: compLog.lst
#=====================================================================================

girlName = "HaxorGurl"
imGirl = girlName + "says: "

# HaxorGurl comes online and goes on to critizise your computer and the fact
# that you installed David's crappy OS and the chat program that he used to eavesdrop on
# girls that he liked. She explains that she knows you.

# She goes on to say that a hacking blog has just posted that the company the protagonist
# works for has just been hacked and that it seems that the way they did it was by bringing
# another computer. She figures out its you by the blog. She states that the company has
# ordered a lockdown so he can't leave.
# She insists that you clear your name and find the culprit. By finding clues about the
# culprit.

# Suggests you try to connect to any computers that you connected to before.

# LIST OF ACTIVE COMPS: Steve, Sally
# 