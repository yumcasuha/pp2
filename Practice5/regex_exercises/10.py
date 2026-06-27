"""
Write a Python program to convert a given camel
case string to snake case.
"""

import re

def camel_to_snake(camel_str):
    snake = re.sub(r'([A-Z])', r'_\1', camel_str)
    return snake.lower()

txt = input("String in camelCase: ")

print("Result:", camel_to_snake(txt))
