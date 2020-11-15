#!/bin/python3

import math
import os
import random
import re
import sys



class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def area(self):
        return self.a*self.b

class Circle:
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return math.pi * (self.r ** 2)
if __name__ == '__main__':  
