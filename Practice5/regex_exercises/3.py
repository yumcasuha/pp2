"""
Write a Python program to find sequences of
lowercase letters joined with a underscore.
"""

import re
txt = input("Enter str: ")
pattern = r"[a-z]+_[a-z]+"

if re.fullmatch(pattern, txt):
    print(f"'{txt}' => matches")
else:
    print(f"'{txt}' => no match")