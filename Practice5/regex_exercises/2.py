"""
Write a Python program that matches a string that
has an 'a' followed by two to three 'b'.
"""
import re

pattern = r"ab{2,3}"
txt = input("Enter str: ")

if re.fullmatch(pattern, txt):
        print(f"'{txt}' => matches")
else:
        print(f"'{txt}' => no match")