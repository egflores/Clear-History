#----------------------------------------------------------------------------------
# Class HaxorGurl
#	should probably go somewhere in the command prompt class to check if her name
#	comes up as an argument in "upload". Her computer can't be directly connected to
#	so this is an alternative.
#----------------------------------------------------------------------------------
class HaxorGurl:
	fileResponses # dictionary of filenames and their responses
	#function: gets an 'uploaded' file and responds accordingly
	def response(filename):
		if filename #is in fileResponses, read string