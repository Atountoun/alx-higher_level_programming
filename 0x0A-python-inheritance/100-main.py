#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)

cust_int = MyInt(11)
print(cust_int)
print(cust_int == 12)
print(cust_int == 11)
print(cust_int != 11)
print(cust_int != 12)
