"""
Write a Python program that matches a string that
has an 'a' followed by zero or more 'b''s.
"""

import re

pattern = r"ab*"
txt = input("Enter str: ")

if re.fullmatch(pattern, txt):
        print(f"'{txt}' => matches")
else:
        print(f"'{txt}' => no match")
