'''import math_utils   # importing our custom file

result1 = math_utils.add(10, 5)
result2 = math_utils.subtract(10, 5)

print("Addition:", result1)
print("Subtraction:", result2)
from math_utils import add, subtract   # directly import specific functions

result1 = add(20, 7)       # no need to write math_utils.add
result2 = subtract(20, 7)

print("Addition:", result1)
print("Subtraction:", result2)'''
from math_utils import *   # import everything

print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))