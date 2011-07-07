from resources import Computer, File
import Constants
import time

# Public variables
command_list = {};
home_computer = Computer("home")
current_computer = home_computer
computer_list = {}

# This function displays the the files to the user
def ls():
	if current_computer.files:
		print Constants.file_header
		for file in current_computer.files:
			if current_computer.files[file].encrypted:
				print file, "(encrypted)"
			else:
				print file
	else:
		print "No files."
	
# This functions displays the text of a file if not encrypted
def cat(file_name):
	if file_name:
		if file_name in current_computer.files:
			print current_computer.files[file_name].text
		else:
			print "%s does not exist." % file_name
	else:
		print "Please enter name of file you wish to open."

def connect(name):
	if name != "":
		if name in computer_list:
			global current_computer
			current_computer = computer_list[name]
			print "Connecting to %s..." % current_computer.name
			time.sleep(3)
			print "Connected to %s." % current_computer.name
		else:
			print name, "does not exist or is not connected."
	else:
		print "No address given, try again.."
	
def disconnect():
	global current_computer
	current_computer = home_computer
	print "Disconnecting..."
	time.sleep(3)
	print "Disconnected."

def scan():
	print "Scanning ports..."

def crack():
	print "Initializing cracking protocol..."

def decrypt():
	print "Initilizing decrypting program..."

def download():
	print "Downloading file..."

def upload():
	print "Uploading file..."

def execute():
	print "Executing program..."
	
def help():
	print Constants.help
	
# Load the command list into the command_list dictionary
def load_commands():
	command_list["ls"] = ls
	command_list["cat"] = cat
	command_list["connect"] = connect
	command_list["disconnect"] = disconnect
	command_list["scan"] = scan
	command_list["crack"] = crack
	command_list["decrypt"] = decrypt
	command_list["download"] = download
	command_list["upload"] = upload
	command_list["exec"] = execute
	command_list["help"] = help
	
def load_computers():
	computer_list["home"] = home_computer
	computer_list["test"] = Computer("test")
	computer_list["test"].files["test"] = File("test", "this is text", False, False)
	computer_list["test"].files["test2"] = File("test2", "super secret stuff", True, False)
	
	
def load_stage():
	load_computers()
	load_commands()
	
# This function parses the commands and executes correct input
def cmd():
	while True:
		command = raw_input(current_computer.prompt).split()
		if command:
			if command[0] in command_list:
				if command[0] != "connect" and command[0] != "cat":
					command_list[command[0]]()
				else:
					if command[1]:
						command_list[command[0]](command[1])
					else:
						command_list[command[0]]("")
			else:
				print command[0], "is not a valid command"
		else:
			return
			
def play():
	load_stage()
	cmd()
	
play()