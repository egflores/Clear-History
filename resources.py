# This class represents a computer
class Computer(object):
	
	def __init__(self, name, specs, protected, password = None, hints = None, tries = None):
		self.name = name
		self.prompt = "user@%s:> " % name
		self.files = {}
		self.specs = specs
		self.protected = protected
		self.password = password
		self.hints = hints
		self.tries = tries
		
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
		self.encryptedPassword = encrypt(password, shift)
		