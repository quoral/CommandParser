from unittest import TestCase
from CommandParser import CommandParser
import Exceptions
import helpers

__author__ = 'krantz'


class TestCommandParser(TestCase):
	def test_add_command_foo(self):
		parser = CommandParser()
		try:
			parser.add_command("foo", helpers.bar)
		except Exceptions.CommandAlreadyExists:
			self.fail()

	def test_add_command_foo_twice(self):
		parser = CommandParser()
		parser.add_command("foo", helpers.bar)
		self.assertRaises(Exceptions.CommandAlreadyExists, parser.add_command, "foo", helpers.bar)

	def test_add_data(self):
		parser = CommandParser()
		try:
			parser.add_data("foo_data")
		except Exceptions.DataAlreadyExists:
			self.fail("Data foo_data should not exist")

	def test_add_data_twice(self):
		parser = CommandParser()
		parser.add_data("foo_data")
		self.assertRaises(Exceptions.DataAlreadyExists, parser.add_data, "foo_data")