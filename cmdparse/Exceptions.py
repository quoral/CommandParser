class CommandAlreadyExists(Exception):
	def __init__(self, command):
		self.command = command

	def __str__(self):
		return repr(self.command)