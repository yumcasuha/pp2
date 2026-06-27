"""
Write a Python program to replace all occurrences of
space, comma, or dot with a colon.
"""

import re

pattern = r"[\s,.]"
txt = input("Enter str: ")

result = re.sub(pattern, ":", txt)
print(f"'{txt}' => '{result}'")