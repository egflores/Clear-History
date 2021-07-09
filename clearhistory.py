import time
from cmd import *
	
#----------------------------------------------------------------------------------
# Intro
#----------------------------------------------------------------------------------
clear()

input("Press enter to begin...")

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

say(0, "Hello, I'm " + managerName + ".\n")

say(1, "I'm sorry that I had you bring your own laptop.\nYour office isn't yet ready so you have to use the empty storage room for now.\nI have something to do so I can't come in to work today\nbut I think we can start training with this USB flash drive with instructions.\nLets Begin.\n")

input("Press Enter to Continue")

say(1, "First, I'll teach you how to connect to other computers on the network.\nType 'connect The name of the computer'.\n")
say(1,  "The computers on this network are usually called 'full name of the employee'\n followed by their 'job'.\n")
say(1, "The names don't have any spaces, only underscores.\n")

input("Press Enter to Continue")

say(1, "Now, I want you to connect to 'Steve_Waller_Security_Consultant'\nIt's case-sensitive so be sure to remember.\n")

input("Press Enter to Continue")

say(2, "\nMost of the time.\n The computers will be password protected.\nYou can easily bypass it with the 'crack' command.\n")
say(1, "That won't completely do all the work for you but it'll make it easier.\nIt'll show you the amount of letters the password is along with hints \nof some letters contained.\n")

input("Press Enter to Continue")

say(1, "Just type in a letter at a time to check if it's contained in the word.\nKind of like 'Hangman'\n")
say(1, "Now crack the password.")
say(1, "type: crack Steve_Waller_Security_Consultant\n")

while True:
	if cmd() == ["crack", "Steve_Waller_Security_Consultant"] : break

say(1, "\nNow that the password has been entered, you can connect to it.\n")
say(1, "You type it in this format: connect (name_of_computer)\nNow connect to Steve_Waller_Security_Consultant\n")
	
while True:
	if cmd() == ["connect", "Steve_Waller_Security_Consultant"] : break

say(1, "\nTo see all the files contained in the computer use the 'ls' command.\n")
say(1, "type: ls\n")

while True:
	if cmd() == ["ls"]: break

say(1, "\nTo read files use the 'cat' command\nfollowed by the file you want to read.\n")
say(1, "In this format: cat (name_of_file)\nTry reading SteveMail.hist.\n")

while True:
	if cmd() == ["cat", "SteveMail.hist"]: break

say(1.5, "Good. Now try to decrypt employLst.lst by using the 'decrypt' command\nfollowed by the filename and password(if you have it).\n")
say(1, "That command brings up the jumbled keyword.\nThe letters in the keyword are shifted by a certain number.\n")

input("Press Enter to Continue")

say(1, "For example 'a' shifted by -1 will be 'z'.\nAnd if 'a' is shifted by 1 it will be 'b'.\nIts your job to find out the decryption code\n(the number of letters the keyword is shifted by.)\n")

input("Press Enter to Continue")

say(1, "You can use the keyword 'scan' followed the name of the computer to view its specs.\n")
say(1, "In this format to reveal the jumbled word: decrypt (filename)\n")
say(1, "In this format to enter the password: decrypt (filename) (Password)\n")
say(1, "Type this to see the specs: scan (Name_Of_Computer)\n")
say(1, "Now decrypt employLst.lst\n")

while True:
	if cmd() == ["decrypt", "employLst.lst", "password"]: break

say(1, "\nGood. Now I'm going to need you to retrieve all the files from the computer.")
say(1, "Use the 'download' command followed by the filename\nto download any file to your computer.\n")
say(1, "Like this: download (filename)\n")

while True:
	cmd()
	if "savedFragment2.ry"in Home_Computer.files and "SteveMail.hist" in Home_Computer.files and "employLst.lst" in Home_Computer.files: break

say(1, "\nOnce you've downloaded the file,\ndisconnect from the computer by using the 'disconnect' function.\n")
say(1, "Format: disconnect\n")

while True:
	if cmd() == ["disconnect"] : break

say(1, "\nNow upload savedFragment2.ry to using the 'upload' command\nfollowed by the fileame you want to upload, then the computer name.\n")
say(1, "Format: upload (filename) (Name_Of_Computer)")
say(0, "Send it to 'Amitav_Gutipaty_Manager'\n")

while True:
	if cmd() == ["upload", "savedFragment2.ry", "Amitav_Gutipaty_Manager"]: break

say(2, "\nYou have just given me highly classified information about the company.\nBut since this company has a closed network I couldn't get in it through the inside computers.\n")
say(1, "But with your computer I could access the internet\nand everything will be traced back to you.\n")
say(5, "Good Bye")
say(9, "")

fill_screen()

clear()

#====================================================================================
# Stage 2
#------------------------------------------------------------------------------------
# The protagonist has just been told that he's been had.
#=====================================================================================

load_stage_2()

girlName = "HaxorGurl"
imGirl = girlName + " says: "

say(4, girlName + " is now online.")
say(3, imGirl + "Hey!")
say(2, imGirl + "its really early!")
say(3, imGirl + "Aren't u supposed to be @ work?! o_0")
say(2, imGirl + "Answer me! >_<")
say(4, imGirl + "Dats it! I'm scanning u! >:D")
say(5, imGirl + "Ohh! you ARE at work....")
say(3.8, imGirl + "lol, you're using David's crappy ass OS?!")
say(2.3, imGirl + "It doesn't let you send messages, huh?")
say(2.4, imGirl + "You know he just used that to spy on girls' conversations...")
say(2.1, imGirl + "Anyways~")
say(3.3, imGirl + "I just read on a blog..")
say(3.5, imGirl + "that the company you now work for just got hacked.")
say(3.5, imGirl + "The blog says that the company is not letting anybody leave")
say(2.3, imGirl + "until they catch the culprit.")
say(3.3, imGirl + "So far the only leads the cops have is a new employee")
say(5, imGirl + "was seen bringing a personal laptop. But they can't find him.")
say(3, imGirl + "Wait a minute...")
say(1, imGirl + "Thats....")
say(6, imGirl + "you!")
say(4.2, imGirl + "that's strange though,")
say(3.2, imGirl + "because this other guy is taking credit for it.")
say(2, imGirl + "But he says the cops will never find him cuz he's in hiding.")
say(3.3, imGirl + "it must be a mistake, you have to clear your name...")
say(3.5, imGirl + "look around the network for some proof!")
say(3.2, imGirl + "before the cops find you. D:")
say(3.1, imGirl + "If you want,")
say(5, imGirl + "you can upload files to me and I'll see if i can helps. :3")
say(2.1, imGirl + "Just upload to 'haxorgurl'.")
say(4.1, imGirl + "Don't worry, I'll give you the files back")
say(6.1, imGirl + "A word to the wise...")
say(4, imGirl + "Download anything that might be useful later")
say(3, imGirl + "Try connecting to some computers on the network...")
say(5.3, imGirl + "Now get to searchinnnN!!!!")

while True:
	cmd()
	if "savedFragment3.ih" in Home_Computer.files and "savedFragment0.jby" in Home_Computer.files: break

say(3, "SECURITY TRIGGERED")
say(3.3, "NOW TRIGGERING SECURITY MEASURES")

fill_screen()

clear()

#======================================================================================
# Stage 3
#--------------------------------------------------------------------------------------
# Security was just triggered which means all the computers were switched.
#============================================================================================

load_stage_3_1()

say(1.5, imGirl + "wut was dat?! D:")
say(2.2, imGirl + "An update on that dude's blog...")
say(3, imGirl + "he says that security\nhas been activated.")
say(2.3, imGirl + "o_o")
say(6, imGirl + "not")
say(6, imGirl + "good")
say(2.1, imGirl + "pick up the pace!")
	
while True:
	cmd()
	if final_conditions() == True: break

fill_screen()

clear()

load_stage_3_2()

say(1, imGirl + "what cause thkat/")
say(2.2, imGirl + "caused that?")
say(2.3, imGirl + "send the file to me")

while True:
	if cmd() == ["upload", "pandorasBox.exe", "haxorgurl"]: break

say(1.1, imGirl + "lets see")
say(1, imGirl + "har harhahar har!!!")
say(2.5, imGirl + "this guy is a dummy! XD")
say(2.5, imGirl + "He wrote this from his home computer!!")
say(3, imGirl + "I was able to extract all his location information!!!")
say(2.3, imGirl + "Imma give this to the cops.")
say(2.3, imGirl + "maybe I'll get a reward for giving tips hehehe :P")
say(1.2, imGirl + "brb")
say(10, imGirl + "urgh, they put me on hold >:C")
say(5, imGirl + "okay hold on, they're processing.")
say(5, imGirl + "haha they said my tip was helpfulllll ^^")
say(2.5, imGirl + "oh, Pheonixeon's website posted something!")
say(3, imGirl + "'Thanks to an anonymous tip,")
say(3, imGirl + "the hacker has been identified as a recently laid off employee.")
say(5, imGirl + "Even though he just hacked through our least important")
say(3, imGirl + "and least secure network we are working our hardest to get things")
say(2, imGirl + "back to normal.'")
say(4, imGirl + "That was damn quick!")
say(3, imGirl + "They're not a top company for nothing...")
say(1, imGirl + "it seems that you're off the hook! :D")
say(2.5, imGirl + "but this pandora file.....")
say(2.5, imGirl + "only contains personal conversations between employees...")
say(5, imGirl + "I guess that's all the 'least important' network contained.")
say(2.3, imGirl + "either way, congrats on your new job XD")
say(2.3, imGirl + "well, i'm off! see ya after work!")
say(1.4, imGirl + "oh...")
say(3.5, imGirl + "The guy's fetish....")
say(4, imGirl + "is peanut butter....go figure :/")
say(1, girlName + " is now offline.")

# EXIT the game
