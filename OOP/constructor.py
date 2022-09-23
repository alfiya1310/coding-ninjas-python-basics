from os import *
from sys import *
from collections import *
from math import *

class Square:

    # Write init and printArea method here.
    def __init__(self, length = 10):
        self.length = length
        
    def printArea(self):
        print(self.length * self.length)
        
