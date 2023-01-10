#!/usr/bin/python3
"""A module with a function related to object and instances."""


def is_same_class(obj, a_class):
	"""Check if an object is a instance of a class.

	Args:
		obj: the object to check
		a_class: the class to use
	Return:
		True is obj is an instance of a_class
		False if not
	"""
	return type(obj) is a_class
