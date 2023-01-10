#!/usr/bin/python3
"""A module that defines a single function."""


def is_kind_of_class(obj, a_class):
	"""Checks if the object of subclass of a given class.

	Args:
		obj: the object to check
		a_class: the class to use
	"""
	return isinstance(obj, a_class) 
