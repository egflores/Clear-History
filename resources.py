import time

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
				self.hints.append(guess)
				self.protected_password = protect_password(self.password, self.hints)
				if not '_' in self.protected_password:
					print "The password for %s is %s" % (self.name, self.password)
					return
			elif guess in incorrect_guesses:
				print "Already attempted that character."
				time.sleep(1)
				continue
			else:
				current_tries = current_tries + 1
				incorrect_guesses.append(guess)
		print "Too many incorrect guesses, reseting..."
		
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
		