import sys 
from math import sqrt
import os

print("Square root of 16 is", sqrt(16))

print('The command line arguments are:')

for i in sys.argv:
  print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
print(os.getcwd())