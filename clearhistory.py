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
say(0.1, "Connecting to the network")
say(0.2, "Connected")
say(0.1, "Initializing myCustomChat")
say(0.3, "Error! Send function not initialized")
say(0.1, "No friends online")
say(0.1, "Reading from USB")
say(0.2, "Now executing")
clear()

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
#    Files: savedFragment2.ry - Encrypted(really long random text, no hints)
#			employLst.lst - Encrypted(password, 8) - "Sally Stark
#							Steve Waller
#							Richard Moliere
#							Tyrella Jensen"
#			SteveMail.hist - "From: Sally Stark
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
#						hell would you want to know the code?! Only Security Consultants
#						would want to know that.
#
#						From: Sally Stark
#						It's to help a cute new employee! He forgot it and I want to look smart so
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

say(0, "Hello, I'm" + managerName + ".")

say(0.1, "I'm sorry that I had you bring your own laptop. Your office isn't yet ready so you have to use the empty storage room for now. I have something to do so I can't come in to work today but I think we can start training with this USB flash drive with instructions. Lets Begin.")

say(0.1, "First, I'll teach how to connect to other computers on the network. Type 'connect' followed by the name of the computeron the network.")
say(0, "The computers on this network are usually called 'full name employee' followed by 'position'.")
say(0, "Now, I want you to connect to 'Steve Waller Security Consultant'")

# IF TYPES IN CONNECT TO STEVE WALLER AND FAILS (WHICH IT WILL)
say(0, "Don't worry if it's password protected. You can easily bypass it with the 'crack' command.")
say(0, "That won't completely do all the work for you but it'll make it easier. It'll show you the amount of letters the password is along with hints of some letters containted.")
say(0, "Just type in a letter at a time to check if it's contained in the word.")
say(0, "Now crack the password.")

# 3 TRIES. IF HE GETS IT WRONG:
say(0, "The password is 'password'")
# ELSE: CONTINUE

say(0, "Now that the password has been entered, you can connect to it. Do so now.")

# IF CURRENT COMPUTER IS STEVE WALLER: CONTINUE

say(0, "To see all the files contained in the computer use the 'ls' command.")

# IF LS IS USED: CONTINUE

say(0, "To read files use the 'cat' command followed by the file you want to read. Try reading SteveMail.hst.")

# IF CAT IS USED WITH STEVEMAIL.HST: CONTINUE

say(0, "Good. Now try to decrypt emplyLst.lst by using the 'decrypt' command followed by the filename.")
say(0, "That command brings up the jumbled keyword. The letters in the keyword are shifted by a certain number.")
say(0, "For example 'a' shifted by -1 will be 'z'. And if shifted by 1 it will be 'b'. Its your job to find out the decryption code (the number of letters the keyword is shifted.)")
say(0, "Use the keyword 'scan' followed the name of the computer to view its specs.")

# IF EMPLYLST.LST IS DECRYPTED: CONTINUE

say(0, "Good. Now I'm going to need you to retrieve the savedFragment2.ry file.")
say(0, "Use the 'download' command followed by the filename to download any file to your computer.")

# IF MYCOMPUTER CONTAINS SAVEDFRAGMENT2.RY: CONTINUE

say(0, "Once you've downloaded the file, disconnect from the computer by using the 'disconnect' function.")

# IF CURRENT COMPUTER IS MYCOMPUTER: CONTINUE

say(0,"Now upload savedFragment2.ry to using the 'upload' command followed by the computer name you want to upload it to.")
say(0, "Send it to 'Amitav Gutipaty Manager")

# IF UPLOADED SAVEDFRAGMENT2.RY TO "AMITAV GUTIPATY MANAGER": CONTINUE

say(0, "You have just given me highly classified information about the company. But since this company has a closed network I couldn't get in it through the inside computers.")
say(0, "But with your computer I could access the internet and everything will be traced back to you. Good bye.")

# FILL SCREEN WITH RANDOM LETTERS FOR A WHILE. WITH PAUSES SO THEY WILL BE ABLE TO NOTICE IT.
clear()

#====================================================================================
# Stage 2
#------------------------------------------------------------------------------------
# The protagonist has just been told that he's been had.
#------------------------------------------------------------------------------------
# Computer:"Steve Waller Security Consultant"
#
# Computer:"Sally Stark Receptionist" 
#	Specs: Intel i7 Extreme 8 cores @ 3.4Ghz
#		   RAM: 8GB
#		   OS: Windows8
#	Files: savedFragment3.ih - Encrypted(really long random text, no hints)
#			presentEmploy.lst - "Present Employees:
#							Sally Stark
#							Steve Waller
#							Amitav Gutipaty
#							Richard Moliere
#							Tyrella Jensen"
#			SallyMail.hist - Encrypted(sally, 8) - "From: Tyrella Jensen
#						 Hey, Sal. I need a big favor from you! I need to take my
#						 kid to the doctor. Could you clock me in anyway? Appreciate it.
#						 
#						 To: Tyrella Jensen
#						 No problem, I hope he gets better because I know you love your little boy.
#						
#						 To: Richard Moliere
#						 Remember me? It's Sally, the receptionist. I just wanted to say
#						 that I found out the code for you. It's 8.
#
#						 From: Richard Moliere
#						 Thank you so much, ma'am. You are a life saver. It would be
#						 so embarrassing to ask for such important information from my
#						 boss. Especially right after he just told me. So, thanks again.
#
#						 To: Richard Moliere
#						 No problem. And what's with the ma'am stuff? Just call me Sally."
#						 
#						 From: Richard Moliere
#						 Haha okay Sally. The code you gave me worked for most of the files
#						 except for one. I don't know what the file does, I'll ask my boss."
#
# Computer: "Richard Moliere Security Consultant"
#	Specs: Intel i7 Extreme 8 cores @ 3.4Ghz
#		   RAM: 8GB
#		   OS: Windows8
#	Files: savedFragment0.jby - Encrypted(long random, no hints)
#			RichardMail.hist - Encrypted(password, 8)
#						"To: Amitav Gutipaty
#						 I'm sorry to disturb you but I have a file here sitting on my computer.
#						 I can't open it with our current encryption code. Do you know how to
#						 decrypt it?
#
#						 From: Amitav Gutipaty
#						 No.
#
#						 To: Amitav Gutipaty
#						 So, do I just leave it alone?
#
#						 From: Amitav Gutipaty
#						 Yes."
#			RichardMemo.txt - Encrypted(gingerbread, 8)
#						"Things to remember:
#						1. The decryption code for our files is 8.
#						But when security is comprimised it turns into the opposite plus the ram contained.
#						Then the network will re-arrange itself. Which means some computers will not be hooked up.
#						But some others will.
#						
#						2. I was told not to mess that wierd savedFragment file.
#						
#						3. Call Sally by her first name...even though she's like 20 years older than me.
#						
#						4. Our HR Manager really loves her little boy. His name is Chris.
#
#						5. Don't fuck this up."
#
# HaxorGurl Responses: SteveMail.hist - "A cute new employee? I wonder who she means? o_o That must be quite a fetish!"
#					   RichardMemo.txt - "So if somebody triggers security the computers available to you are switched around? Weird. :/"
#						ses.png - ">:/ This isn't the time for this!! @_@; poor donkey.
#						(all fragment files) - "They seem to be numbered. Try to collect all of them together in your computer.^^"
#=====================================================================================

girlName = "HaxorGurl"
imGirl = girlName + "says: "

say(3, girlName + " is now online.")
say(3, imGirl + "Hey!")
say(.2, imGirl + "its really early!")
say(.3, imGirl + "Aren't u supposed to be @ work?! o_0")
say(1, imGirl + "Answer me! >_<")
say(1, imGirl + "Dats it! I'm scanning u! >:D")
say(1, imGirl + "Ohh! you ARE at work....lol, you're using David's crappy ass OS?! It doesn't let you send messages, huh?")
say(.4, imGirl + "You know he just used that to spy on girls' conversations...")
say(.1, imGirl + "Anyways~")
say(.3, imGirl + "I just read on a blog that the company you now work for just got hacked.")
say(.5, imGirl + "The blog says that the company is not letting anybody leave until they catch the culprit.")
say(.3, imGirl + "So far the only leads the cops have is a new employee was seen bringing a personal laptop. But they can't find him.")
say(3, imGirl + "Wait a minute...")
say(1, imGirl + "Thats....")
say(.5, imGirl + "you!")
say(.2, imGirl + "that's strange though, because this other guy is taking credit for it. But he says the cops will never find him cuz he's in hiding.")
say(.3, imGirl + "it must be a mistake, you have to clear your name...")
say(.5, imGirl + "look around the network for some proof before the cops find you. D:")
say(0.1, imGirl + "If you want, you can upload files to me and I'll see if i can helps. :3")
say(0.1, imGirl + "Just upload to 'haxorgurl'.")
say(0.3, imGirl + "Now get to searchinnnN!!!!")

# IF BOTH SAVEDFRAGMENT0.JBY AND SAVEDFRAGMENT3.IH ARE IN MYCOMPUTER: CONTINUE

say(0, "SECURITY TRIGGERED")
say(.3, "NOW TRIGGERING SECURITY MEASURES")

# RANDOM WALL OF TEXT. WITH PAUSES SO THEY CAN SEE THE WALL GETTING LONGER.
clear()

#======================================================================================
# Stage 3
#--------------------------------------------------------------------------------------
# Security was just triggered which means all the computers were switched.
#--------------------------------------------------------------------------------------
# Computers: "Richard Moliere Security Consultant"
#
# Computer: "Tyrella Jensen HR Manager" - Password Protected: Chris, cs
#	Specs: Intel i7 Extreme 8 cores @ 3.4Ghz
#		   RAM: 4GB
#		   OS: Windows8
#	Files: employees.lst - Encrypted(Christopher, -4)
#							"Sally Stark
#							 Age: 40
#							 Receptionist
#							 
#							 Steve Waller
#							 Age: 33
#							 Security Consultant
#
#			TyrellaMail.hst - Encrypted(CrissyBoo, -4)
#							"To: Amitav Gutipaty
#							 We're were very honored to have you work for us. But as a
#							 result of the recent economy we have no choice but to let
#							 you go. We wish you luck and you should recieve your final
#							 check by the end of the week. Thank you.
#
#							From: Amitav Gutipaty
#							What?! Bullshit!!!! if the whole shit about the economy is
#							true, then you wouldn't be hiring more motherfucking security
#							consultants! I just trained that stupid little jerk-off and
#							now you're firing me? FUCk you! and all your shit. I'm gonna
#							go work for Google....fuck you and Pheonixeon.
#
#							To: Amitav Gutipaty
#							Please refrain from using vulgar language. And both of those
#							consultants will make less than what you make. I will ask
#							that you train this new recruit as well before you leave. Thanks :)
#
#							From: Amitav Gutipaty
#							Oh, I'm gonna train him good alright."
#
#			savedFragment1.ihc - Encrypted(really long random text, no hints)
#
# Computer: "Amitav Gutipaty Manager" - Password Protected: Google, o
#	Specs: Intel i7 Extreme 8 cores @ 3.4Ghz
#		   RAM: 16GB
#		   OS: Windows8
#	Files: AmitavMemo.txt - Encrypted(amitav, 8)
#			"The connection: The name of the son and the job of the mother
#			The ends of the files Encrypted by the age of the new employee will give me Passage.
#			Once the fragments are happy together with the son and mother, they will gossip.
#
# Computer: "Chris Jensen HR Manager" - Password Protected: Pheonixeon, (none)
#	Specs: Intel i7 Extreme 8 cores @ 3.4Ghz
#		   RAM: 4GB
#		   OS: Windows8
#	Files: pandorasBox.exe - "Unable to read"
#
# HaxorGurl Responses: employees.lst - "Dang o_O! That Sally is quite old for a receptionist."
#						TyrellaMail.hst - "No doubt that 'new recruit' is u, huh. :p"
#						AmitavMemo.txt - "....Does he mean the file extensions? I guess you have to read them in order?"
#============================================================================================

say(.5, imGirl + "wut was dat?! D:")
say(.2, imGirl + "An update on that dude's blog....he says that security has been activated.")
say(.3, imGirl + "o_o")
say(.3, imGirl + "not")
say(.4, imGirl + "good")
say(.1, imGirl + "pick up the pace!")

# IF connected to "chris jensen hr manager"
# IF all the fragments uploaded to that computer
# Trigger a bunch of code that fills the screen
# Delete all fragments

say(0, imGirl + "what cause thkat/")
say(0.2, imGirl + "caused that?")
say(0.3, imGirl + "send the file to me")

# IF uploaded pandorasBox.exe to haxorgurl: continue

say(0.1, imGirl + "lets see")
say(1, imGirl + "har harhahar har!!!")
say(.5, imGirl + "this guy is a dummy! XD")
say(.5, imGirl + "He wrote this from his home computer!! I was able to extract all his location information!!!")
say(.3, imGirl + "Imma give this to the cops.")
say(.3, imGirl + "maybe I'll get a reward for giving tips hehehe :P")
say(.2, imGirl + "brb")
say(10, imGirl + "urgh, they put me on hold >:C")
say(5, imGirl + "okay hold on, they're processing.")
say(5, imGirl + "haha they said my tip was helpfulllll ^^")
say(.5, imGirl + "oh, Pheonixeon's website posted something!")
say(1, imGirl + "'Thanks to an annonymous tip, the hacker has been identified as a recently laid off employee.")
say(.4, imGirl + "Even though he just hacked through our least important and least secure network we are working our hardest to get things back to normal.'")
say(.4, imGirl + "That was damn quick! They're not a top company for nothing...")
say(1, imGirl + "it seems that you're off the hook! :D")
say(.5, imGirl + "but this pandora file.....")
say(.5, imGirl + "only contains personal converstations between employees....I guess that's all the 'least important' network contained.")
say(.3, imGirl + "either way, congrats on your new job XD")
say(.3, imGirl + "well, i'm off! see ya after work!")
say(.4, imGirl + "oh...")
say(.5, imGirl + "The guy's fetish....")
say(1, imGirl + "is peanut butter....go figure :/")
say(0, girlName + "is now offline.")

# EXIT the game
