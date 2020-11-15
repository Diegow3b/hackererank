#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    arr = sentence.split()[::-1]
    
    newSentence = ""
    for _ in arr:
        newLetter = ""
        for letter in _:
            newLetter += letter.upper() if letter.islower() else letter.lower()
        newSentence += newLetter + " "
    return newSentence
if __name__ == '__main__':
