# This class represents a computer
class Computer(object):
	
	def __init__(self, name):
		self.name = name
		self.prompt = "user@%s:> " % name
		self.files = {}
		self.specs = "Really crappy"
		
# This class represents a file
class File(object):

	def __init__(self, name, text, is_encrypted, is_executable):
		self.name = name
		self.text = text
		self.encrypted = is_encrypted
		self.exexcutable = is_executable