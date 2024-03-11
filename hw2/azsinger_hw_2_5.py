"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/01/28
Homework Problem # 2_5
Description of Problem (1-2 sentence summary in your own words):
A variation of the fizz-buzz challenge using foo, bar, baz. This problem uses a
for loop and then a while loop.
"""

# 5a
MAXVAL = 30
# 5b
for value in range(1, MAXVAL + 1):
    print_string = ""
    # 5c
    if value % 2 == 0:
        print_string += "foo"
    if value % 3 == 0:
        print_string += "bar"
    if value % 5 == 0:
        print_string += "baz"
    print(f"{value}:{print_string}")
# 5d
print("")
# 5e
value = 1
while value <= MAXVAL:
    print_string = ""
    # 5c
    if value % 2 == 0:
        print_string += "foo"
    if value % 3 == 0:
        print_string += "bar"
    if value % 5 == 0:
        print_string += "baz"
    print(f"{value}:{print_string}")
    value += 1
