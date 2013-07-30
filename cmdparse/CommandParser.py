import Exceptions


class CommandParser:
	def __init__(self):
		self.arguments = {}

	def add_command(self, command, action):
		if command in self.arguments:
			raise Exceptions.CommandAlreadyExists("Command %s already exists." % command)
		self.arguments[command] = {'action': action}
