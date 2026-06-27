"""
Write a Python program to find the sequences of one
upper case letter followed by lower case letters.
"""
import re

pattern = r"[A-Z][a-z]+"
txt = input("Enter str: ")

if re.fullmatch(pattern, txt):
    print(f"'{txt}' => matches")
else:
    print(f"'{txt}' => no match")