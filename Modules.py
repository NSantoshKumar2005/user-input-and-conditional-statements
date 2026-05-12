'''
Modules:
------------
-->A module is a file containing .py extension.
->variables
->functions
->classes

Modules help us:
-->Reuse of code
-->Reduce code duplicate

Types of modules:
------------------------
-->user define modules
Eg:'''
import My_module
print(My_module.module1())
print(My_module.hello_world())
'''
-->In-built modules:
->os
->math
->sys

-->To use all this module, we have to import with module name

ways to import modules:
--------------------------------
1.using Alias Name
2.import entire module
3.import all functions
4.import specific functions

math module:
------------------
The math module in python is a built-in library that contains a collection of mathematical functions and
constants.
Ex:'''
import math
print(math.sqrt(49))
print(math.sqrt(1/2))
print(math.factorial(5))
'''
sys module:
----------------
-->sys module is system-specific parameters and functions.
Ex:'''
import sys
print(sys.version)
print(sys.path)
'''
random module:
---------------------
-->This module generates random numbers in python
Ex:'''
import random
otp=random.randint(1000,9999)
print("Your OTP is ",otp)













