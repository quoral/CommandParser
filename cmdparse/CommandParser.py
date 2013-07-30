import Exceptions


class CommandParser:
	def __init__(self):
		self.arguments = {}
		self.data = {}

	def add_command(self, command, action):
		if command in self.arguments:
			raise Exceptions.CommandAlreadyExists(command)
		self.arguments[command] = {'action': action}

	def add_data(self, data):
		if data in self.data:
			raise Exceptions.DataAlreadyExists(data)
		self.data[data] = {}