#!/usr/bin/python3
"""This module has a single function text_indentation."""


def text_indentation(text):
    """This function prints a text with 2 new lines after `.`, `?` and `:`.

    Args:
        text: the text to be indented

    Raises:
        TypeError:
            if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delims = [".", "?", ":"]
    n_text = text

    for i, delim in enumerate(delims):
        n_text_list = [ele + delim for ele in n_text.split(delim)[:-1]]
        n_text_list.append(n_text.split(delim)[-1])
        n_text = "\n\n".join(n_text_list)

    n_text_list = [ele.strip() for ele in n_text.split('\n')]
    n_text = '\n'.join(n_text_list)

    print(n_text, end="")
