from os import *
from sys import *
from collections import *
from math import *

class Rectangle:
    
    def __init__(self):
        self.length = 0
        self.breadth = 0
        
    def getArea(self):
        area = self.length * self.breadth
        return area