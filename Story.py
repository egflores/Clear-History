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
# culprit. Opens her computer for uploading.

# Suggests you try to connect to any computers that you connected to before.

# Download savedFragment0.xtr
# Security will activate which fills the screen then clears it.

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
#							consultants will make less than what you make. And I will ask
#							That you train this new recruit as well before you leave. Thanks :)
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
#			Once the fragments are happy together in that nest, they will gossip.
#
# Computer: "Chris Jensen HR Manager" - Password Protected: Pheonixeon, (none)
#	Specs: Intel i7 Extreme 8 cores @ 3.4Ghz
#		   RAM: 4GB
#		   OS: Windows8
#	Files: pandorasBox.exe - "Unable to read"
#
# HaxorGurl Responses: employees.lst - "Dang o_O! That Sally is quite old for a receptionist."
#						TyrellaMail.hst - "No doubt that 'new recruit' is u, huh. :p"
#						AmitavMemo.txt - "....Does he mean the file extensions?"
#============================================================================================

# HaxorGurl mentions the blog says that the security has been triggered. And the company will take
# legal action with the hacker which at this time points at the protagonist.

# When connected to "chris jensen hr manager"
# If all the fragments are together
# Trigger a bunch of code that fills the screen
# HaxorGurl asks for the Pandorasbox.exe file
# When uploaded she says that she sent this info to the police and that they said that all the evidence points to amitav
# She congratulates you and says goodbye.
# Exit.