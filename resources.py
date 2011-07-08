# This class represents a computer
class Computer(object):
	
	def __init__(self, name, protected, password):
		self.name = name
		self.prompt = "user@%s:> " % name
		self.files = {}
		self.specs = "Really crappy"
		self.protected = protected
		self.password = password
		
# This class represents a file
class File(object):

	def __init__(self, name, text, is_encrypted):
		self.name = name
		self.text = text
		self.encrypted = is_encrypted