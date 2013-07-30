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
		try:
			parser.add_command("foo", helpers.bar)
		except Exceptions.CommandAlreadyExists:
			self.fail("parser.add_command(foo)")
		self.assertRaises(Exceptions.CommandAlreadyExists, parser.add_command, "foo", helpers.bar)

