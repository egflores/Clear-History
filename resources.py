import time
import Constants

def protect_password(password, hints):
		result = ""
		if password and hints:
			for letter in password:
				if letter in hints:
					result = result + letter + " "
				else:
					result = result + "_ "
		return result
			
def get_guess():
	while True:
		guess = raw_input("Guess:> ")
		if len(guess) != 1:
			print "Only one character guesses accepted."
		else:
			return guess

# This class represents a computer
class Computer(object):
	
	def __init__(self, name, specs, protected, password = None, hints = None, tries = None):
		self.name = name
		self.prompt = "user@%s:> " % name
		self.files = {}
		self.specs = specs
		self.protected = protected
		self.password = password
		self.protected_password = protect_password(password, hints)
		self.hints = hints
		self.tries = tries
		
	def crack(self):
		current_tries = 0
		incorrect_guesses = []
		print "Starting cracking program..."
		time.sleep(2)
		while(current_tries != self.tries):
			print "Password:", self.protected_password
			print "Tries left: %s" % (self.tries - current_tries)
			if incorrect_guesses:
				print "Guesses:", ''.join(incorrect_guesses)
			guess = get_guess() 
			if guess in self.password:
				self.hints += guess
				self.protected_password = protect_password(self.password, self.hints)
				if not '_' in self.protected_password:
					print "The password for %s is %s" % (self.name, self.password)
					return True
			elif guess in incorrect_guesses:
				print "Already attempted that character."
				time.sleep(1)
				continue
			else:
				current_tries = current_tries + 1
				incorrect_guesses.append(guess)
		print "Too many incorrect guesses, reseting..."
		return False
		
def encrypt(text, shift = 1):
	if text:
		return ''.join([[ch,chr((ord(ch) - ord(['A','a'][ch.islower()]) + shift)%26+ord(['A','a'][ch.islower()]))][ch.isalpha()] for ch in text])
	else:
		return None
	
# This class represents a file
class File(object):

	def __init__(self, name, text, is_encrypted, password = None, shift = None):
		self.name = name
		self.text = text
		self.encrypted = is_encrypted
		self.password = password
		self.shift = shift
		self.encrypted_password = encrypt(password, shift)
		
def Home_Computer_Files():
	files = {}
	core_os_files = File("CoreOSFiles.bndl", "Unable to read", False)
	files["CoreOSFiles.bndl"] = core_os_files
	core_img_files = File("coreImgFiles.bndl", "Unable to read", False)
	files["coreImgFiles.bndl"] = core_img_files
	core_script = File("coreScript.bndl", "Unable to read", False)
	files["coreScript.bndl"] = core_script
	ses_crk = File("sesCrk.txt", "Pandora's (i is sqrt of: ?)", False)
	files["sesCrk.txt"] = ses_crk
	ses = File("ses.png", "256kb image file retrieved from http://www.elcachondo.net/", True, "box", -1)
	files["ses.png"] = ses
	error_log = File("errorLog.txt", "Damn send function, I'll write it later, not like I need it to evesdrop on conversations...", False)
	files["errorLog.txt"] = error_log
	return files

Home_Computer = Computer("My_Computer", Constants.home_computer, False)
Home_Computer.files = Home_Computer_Files()
comp_list = {}
		
def Steve_Waller_Files():
	files = {}
	saved_fragment = File("savedFragment2.ry", "N/A", True, "lakjdlirvioej", 1)
	files["savedFragment2.ry"] = saved_fragment
	employ_list = File("employLst.lst", "Sally Stark\nSteve Waller\nRichard Moliere\nTyrella Jense\n", True, "password", 8)
	files["employLst.lst"] = employ_list
	steve_mail = File("SteveMail.hist", Constants.Steve_Mail, False)
	files["SteveMail.hist"] = steve_mail
	return files
	
def load_stage1_computers():
	global comp_list
	Steve_Waller_Security_Consultant = Computer("Steve_Waller_Security_Consultant", Constants.Steve_Waller_Security_Consultant, True, "password", "sword", 3)
	Steve_Waller_Security_Consultant.files = Steve_Waller_Files()
	comp_list["Steve_Waller_Security_Consultant"] = Steve_Waller_Security_Consultant
	return comp_list

def Sally_Stark_Files():
	files = {}
	saved_fragment_3 = File("savedFragment3.ih", "N/A", True, "asdfjklroigjoidfj", 1)
	files["savedFragment3.ih"] = saved_fragment_3
	present_employ = File("presentEmploy.lst", "Present Employees:\nSally Stark\nSteve Waller\nAmitav Gutipaty\nRichard Moliere\nTyrella Jensen", False)
	files["presentEmploy.lst"] = present_employ
	sally_mail = File("SallyMail.hist", Constants.Sally_Mail, True, "sally", 8)
	files["SallyMail.hist"] = sally_mail
	return files

def Richard_Moliere_Files():
	files = {}
	saved_fragment_0 = File("savedFragment0.jby", "N/A", True, "skjdfirni", 1)
	files["savedFragment0.jby"] = saved_fragment_0
	richard_mail = File("RichardMail.hist", Constants.Richard_Mail, True, "password", 8)
	files["RichardMail.hist"] = richard_mail
	richard_memo = File("RichardMemo.txt", Constants.Richard_Memo, True, "gingerbread", 8)
	files["RichardMemo.txt"] = richard_mem0
	return files
	
def load_stage2_computers():
	global comp_list
	Sally_Stark_Receptionist = Computer("Sally_Stark_Receptionist", Constants.Sally_Stark_Receptionist, False)
	Sally_Stark_Receptionist.files = Sally_Stark_Files()
	comp_list["Sally_Stark_Receptionist"] = Sally_Stark_Receptionist
	Richard_Moliere_Security_Consultant = Computer("Richard_Moliere_Security_Consultant", Constants.Richard_Moliere_Security_Consultant, False)
	Richard_Moliere_Security_Consultant.files = Richard_Moliere_Files()
	comp_list["Richard_Moliere_Security_Consultant"] = Richard_Moliere_Security_Consultant
	return comp_list

def Tyrella_Jensen_Files():
	files = {}
	employees = File("employees.lst", "Sally Stark\nAge: 40\n Receptionist\n\nSteve Waller\nAge: 33\nSecurity Consultant", True, "christopher", -4)
	files["employees.lst"] = employees
	tyrella_mail = File("TyrellaMail.hst", Constants.Tyrella_Mail, True, "crissyboo", -4)
	files["TyrellaMail.hst"] = tyrella_mail
	saved_fragment_1 = File("savedFragment1.ihc", "N/A", True, "irimcieds", 1)
	files["savedFragment1.ihc"] = saved_fragment_1
	return files

def Amitav_Gutipaty_Files():
	files = {}
	amitav_memo = File("AmitavMemo.txt", Constants.Amitav_Memo, True, "amitav", 8)
	files["AmitavMemo.txt"] = amitav_memo
	return files

def Chris_Jensen_Files():
	files = {}
	pandoras_box = File("pandorasBox.exe", "Unable to read", False)
	files["pandorasBox.exe"] = pantoras_box
	return files
	
def load_stage3_computers():
	global comp_list
	del comp_list["Steve_Waller_Security_Consultant"]
	del comp_list["Sally_Stark_Receptionist"]
	Tyrella_Jensen_HR_Manager = Computer("Tyrella_Jensen_HR_Manager", Constants.Tyrella_Jensen_HR_Manager, True, "chris", "cs", 3)
	Tyrella_Jensen_HR_Manager.files = Tyrella_Jensen_Files()
	comp_list["Tyrella_Jensen_HR_Manager"] = Tyrella_Jensen_HR_Manager
	Amitav_Gutipaty_Manager = Computer("Amitav_Gutipaty_Manager", Amitav_Gutipaty_Manager, True, "google", "o", 3)
	Amitav_Gutipaty_Manager.files = Amitav_Gutipaty_Files()
	comp_list["Amitav_Gutipaty_Manager"] = Amitav_Gutipaty_Manager
	Chris_Jensen_HR_Manager = Computer("Chris_Jensen_HR_Manager", Constants.Chris_Jensen_HR_Manager, "pheonixeon", "", 3)
	Chris_Jensen_HR_Manager.files = Chris_Jensen_Files()
	comp_list["Chris_Jensen_HR_Manager"] = Chris_Jensen_HR_Manager
	return comp_list