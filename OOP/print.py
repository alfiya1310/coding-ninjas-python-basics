from os import *
from sys import *
from collections import *
from math import *

class Person:

    #create your class here
    def __init__(self):
        self.name = ""
        self.age = ""
        
    def setValue(self,name,age):
        self.name = name
        self.age = age
        
    def getValue(self):
        print("The name of the person is " + self.name + " and the age is " + age + ".")
        
#Driver code goes here.
 
P = Person()
name = input()
age = input()
P.setValue(name,age)
P.getValue()
