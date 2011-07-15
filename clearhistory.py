import time
import os
from cmd import *

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
clear()

raw_input("Press enter to begin...")

print("MyCustomOS")
time.sleep(0.4)
print("Loading CoreOSFiles")
say(1.1, "Connecting to the network")
say(1.2, "Connected")
say(1.1, "Initializing myCustomChat")
say(1.3, "Error! Send function not initialized")
say(1.1, "No friends online")
say(1.1, "Reading from USB")
say(1.2, "Now executing Training Program")
time.sleep(3)
clear()
load_commands()

#==================================================================================
# Stage 1
#----------------------------------------------------------------------------------
# Very early in the morning.
# This takes place in the offices of Pheonixeon Corp.
# The protagonist is just starting his new job as a security consultant.
# He enters an empty room. He then inserts a USB flash drive into his computer as
# he was instructed by his manager over the phone.
#==================================================================================

load_stage_1()

managerName = "Amitav Gutipaty" #Just so I can change it easily if I want.
imManager = managerName + "says: " #So I don't have to type "says:"

say(0, "Hello, I'm " + managerName + ".")

say(0.1, "I'm sorry that I had you bring your own laptop. Your office isn't yet ready so you have to use the empty storage room for now. I have something to do so I can't come in to work today but I think we can start training with this USB flash drive with instructions. Lets Begin.\n")
say(0.1, "First, I'll teach how to connect to other computers on the network. Type 'connect' followed by the name of the computeron the network.\n")
say(0,  "The computers on this network are usually called 'full name employee' followed by 'position'.\n")
say(0, "Now, I want you to connect to 'Steve_Waller_Security_Consultant' (case-sensitive)\n")

while True:
	if cmd() == ["connect", "Steve_Waller_Security_Consultant"] : break

say(0, "\nDon't worry if it's password protected. You can easily bypass it with the 'crack' command.\n")
say(0, "That won't completely do all the work for you but it'll make it easier. It'll show you the amount of letters the password is along with hints of some letters containted.\n")
say(0, "Just type in a letter at a time to check if it's contained in the word.\n")
say(0, "Now crack the password.")

while True:
	if cmd() == ["crack", "Steve_Waller_Security_Consultant", "password"]: break


say(0, "\nNow that the password has been entered, you can connect to it. Do so now.\n")
	
while True:
	if cmd() == ["connect", "Steve_Waller_Security_Consultant"] : break

say(0, "\nTo see all the files contained in the computer use the 'ls' command.\n")

while True:
	if cmd() == ["ls"]: break

say(0, "\nTo read files use the 'cat' command followed by the file you want to read. Try reading SteveMail.hist.\n")

while True:
	if cmd() == ["cat", "SteveMail.hist"]: break

say(0, "Good. Now try to decrypt employLst.lst by using the 'decrypt' command followed by the filename.\n")
say(0, "That command brings up the jumbled keyword. The letters in the keyword are shifted by a certain number.\n")
say(0, "For example 'a' shifted by -1 will be 'z'. And if shifted by 1 it will be 'b'. Its your job to find out the decryption code (the number of letters the keyword is shifted.)\n")
say(0, "Use the keyword 'scan' followed the name of the computer to view its specs.\n")

while True:
	if cmd() == ["decrypt", "employLst.lst", "password"]: break

say(0, "\nGood. Now I'm going to need you to retrieve the savedFragment2.ry file.")
say(0, "Use the 'download' command followed by the filename to download any file to your computer.\n")

while True:
	cmd()
	if "savedFragment2.ry" in home_computer.files: break

say(0, "\nOnce you've downloaded the file, disconnect from the computer by using the 'disconnect' function.\n")

while True:
	cmd()
	if current_computer == home_computer: break

say(0, "\nNow upload savedFragment2.ry to using the 'upload' command followed by the computer name you want to upload it to.\n")
say(0, "Send it to 'Amitav Gutipaty Manager'\n")

while True:
	if cmd() == ["upload", "savedFragment2.ry", "Amitav_Gutipaty_Manager"]: break

say(0, "\nYou have just given me highly classified information about the company. But since this company has a closed network I couldn't get in it through the inside computers.\n")
say(0, "But with your computer I could access the internet and everything will be traced back to you. Good bye.\n")

#######################
raw_input("Press enter")
#######################

# FILL SCREEN WITH RANDOM LETTERS FOR A WHILE. WITH PAUSES SO THEY WILL BE ABLE TO NOTICE IT.
clear()

#====================================================================================
# Stage 2
#------------------------------------------------------------------------------------
# The protagonist has just been told that he's been had.
#------------------------------------------------------------------------------------
# HaxorGurl Responses: SteveMail.hist - "A cute new employee? I wonder who she means? o_o That must be quite a fetish!"
#					   RichardMemo.txt - "So if somebody triggers security the computers available to you are switched around? Weird. :/"
#						ses.png - ">:/ This isn't the time for this!! @_@; poor donkey.
#						(all fragment files) - "They seem to be numbered. Try to collect all of them together in your computer.^^"
#=====================================================================================

girlName = "HaxorGurl"
imGirl = girlName + " says: "

say(4, girlName + " is now online.")
say(3, imGirl + "Hey!")
say(2, imGirl + "its really early!")
say(3, imGirl + "Aren't u supposed to be @ work?! o_0")
say(2, imGirl + "Answer me! >_<")
say(4, imGirl + "Dats it! I'm scanning u! >:D")
say(5, imGirl + "Ohh! you ARE at work....lol, you're using David's crappy ass OS?! It doesn't let you send messages, huh?")
say(2.4, imGirl + "You know he just used that to spy on girls' conversations...")
say(2.1, imGirl + "Anyways~")
say(3.3, imGirl + "I just read on a blog that the company you now work for just got hacked.")
say(3.5, imGirl + "The blog says that the company is not letting anybody leave until they catch the culprit.")
say(3.3, imGirl + "So far the only leads the cops have is a new employee was seen bringing a personal laptop. But they can't find him.")
say(3, imGirl + "Wait a minute...")
say(1, imGirl + "Thats....")
say(1.5, imGirl + "you!")
say(4.2, imGirl + "that's strange though, because this other guy is taking credit for it. But he says the cops will never find him cuz he's in hiding.")
say(3.3, imGirl + "it must be a mistake, you have to clear your name...")
say(3.5, imGirl + "look around the network for some proof before the cops find you. D:")
say(3.1, imGirl + "If you want, you can upload files to me and I'll see if i can helps. :3")
say(2.1, imGirl + "Just upload to 'haxorgurl'.")
say(2.1, imGirl + "Don't worry, I'll give you the files back.")
say(2.3, imGirl + "Now get to searchinnnN!!!!")

# IF BOTH SAVEDFRAGMENT0.JBY AND SAVEDFRAGMENT3.IH ARE IN MYCOMPUTER: CONTINUE

say(3, "SECURITY TRIGGERED")
say(3.3, "NOW TRIGGERING SECURITY MEASURES")

# RANDOM WALL OF TEXT. WITH PAUSES SO THEY CAN SEE THE WALL GETTING LONGER.
clear()

#======================================================================================
# Stage 3
#--------------------------------------------------------------------------------------
# Security was just triggered which means all the computers were switched.
#--------------------------------------------------------------------------------------
# HaxorGurl Responses: employees.lst - "Dang o_O! That Sally is quite old for a receptionist."
#						TyrellaMail.hst - "No doubt that 'new recruit' is u, huh. :p"
#						AmitavMemo.txt - "....Does he mean the file extensions? I guess you have to read them in order?"
#============================================================================================

say(1.5, imGirl + "wut was dat?! D:")
say(2.2, imGirl + "An update on that dude's blog....he says that security has been activated.")
say(2.3, imGirl + "o_o")
say(1.3, imGirl + "not")
say(1.4, imGirl + "good")
say(2.1, imGirl + "pick up the pace!")

# IF connected to "chris jensen hr manager"
# IF all the fragments uploaded to that computer
# Trigger a bunch of code that fills the screen
# Delete all fragments

say(0, imGirl + "what cause thkat/")
say(2.2, imGirl + "caused that?")
say(2.3, imGirl + "send the file to me")

# IF uploaded pandorasBox.exe to haxorgurl: continue

say(1.1, imGirl + "lets see")
say(1, imGirl + "har harhahar har!!!")
say(2.5, imGirl + "this guy is a dummy! XD")
say(2.5, imGirl + "He wrote this from his home computer!! I was able to extract all his location information!!!")
say(2.3, imGirl + "Imma give this to the cops.")
say(2.3, imGirl + "maybe I'll get a reward for giving tips hehehe :P")
say(1.2, imGirl + "brb")
say(10, imGirl + "urgh, they put me on hold >:C")
say(5, imGirl + "okay hold on, they're processing.")
say(5, imGirl + "haha they said my tip was helpfulllll ^^")
say(2.5, imGirl + "oh, Pheonixeon's website posted something!")
say(3, imGirl + "'Thanks to an annonymous tip, the hacker has been identified as a recently laid off employee.")
say(5, imGirl + "Even though he just hacked through our least important and least secure network we are working our hardest to get things back to normal.'")
say(4, imGirl + "That was damn quick! They're not a top company for nothing...")
say(1, imGirl + "it seems that you're off the hook! :D")
say(2.5, imGirl + "but this pandora file.....")
say(2.5, imGirl + "only contains personal converstations between employees....I guess that's all the 'least important' network contained.")
say(2.3, imGirl + "either way, congrats on your new job XD")
say(2.3, imGirl + "well, i'm off! see ya after work!")
say(1.4, imGirl + "oh...")
say(3.5, imGirl + "The guy's fetish....")
say(4, imGirl + "is peanut butter....go figure :/")
say(1, girlName + " is now offline.")

# EXIT the game
