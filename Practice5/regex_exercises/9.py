"""
Write a Python program to insert spaces between
words starting with capital letters.
"""

import re

txt = input("String: ")

result = re.sub(r'([A-Z])', r' \1', txt)
result = result.strip()

print("Result:", result)
