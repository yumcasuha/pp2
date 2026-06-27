"""
Write a Python program that matches a string that
has an 'a' followed by anything, ending in 'b'.
"""

import re

pattern = r"a.*b$"
txt = input("Enter str: ")

if re.fullmatch(pattern, txt):
    print(f"'{txt}' => matches")
else:
    print(f"'{txt}' => no match")