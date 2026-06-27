"""
Write a Python program to split a string at 
uppercase letters.
"""

import re

txt = input("String: ")
parts = re.findall(r'[A-Z][^A-Z]*', txt)

print("Result:", parts)
