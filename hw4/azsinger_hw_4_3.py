"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/10
Homework Problem # 4_3
Description of Problem (1-2 sentence summary in your own words):
Create two constant lists of first names and last names. Validate the last name
list is not shorter than the first name list. Zip them into a
dictionary with last names as keys and print the lists and dictionary.
"""

FIRST_NAMES = ["Jane", "John"]
LAST_NAMES = ["Doe", "Deer", "Black"]

if len(LAST_NAMES) < len(FIRST_NAMES):
    exit("ERROR: Last name list has fewer names than first name list")

# if we were allowed to import from itertools I would use zip_longest() here
name_dict = dict(zip(LAST_NAMES, FIRST_NAMES))
# if there are more last names than first names then add them to the dictionary
# with value of None
if len(LAST_NAMES) > len(FIRST_NAMES):
    for last_name in LAST_NAMES[len(FIRST_NAMES):]:
        name_dict[last_name] = None

print(f"First Names: {FIRST_NAMES}")
print(f"Last Names: {LAST_NAMES}")
print(f"Name Dictionary: {name_dict}")
