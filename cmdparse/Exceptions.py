class CommandAlreadyExists(Exception):
	def __init__(self, command):
		self.command = command

	def __str__(self):
		return "Command " + self.command + " Already exists"


class DataAlreadyExists(Exception):
	def __init__(self, data):
		self.command = data

	def __str__(self):
		return "Data " + self.data + " Already exists"