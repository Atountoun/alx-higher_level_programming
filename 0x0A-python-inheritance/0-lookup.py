"""
A module to returns available attributes and methods
of an object
"""


def lookup(obj):
	"""Return list of attibutes and methods"""
	return list(dir(obj))
