#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            if type(my_list[i]) is not int:
                pass
            else:
                print("{:d}".format(my_list[i]), end="")
                printed += 1
        except Exception as e:
            raise
    print()

    return printed
