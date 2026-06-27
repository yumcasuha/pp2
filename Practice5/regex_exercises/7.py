"""
Write a python program to convert snake case string
to camel case string.
"""

def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

txt = input("String: ")

print("Result:", snake_to_camel(txt))
