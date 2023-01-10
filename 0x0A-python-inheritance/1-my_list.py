"""Module of a class inherited from list object."""


class MyList(list):
	"""Inherits form list built-in object"""

	def print_sorted(self):
		print(list(sorted(self)))
