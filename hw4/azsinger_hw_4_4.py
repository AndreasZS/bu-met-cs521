"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/10
Homework Problem # 4_4
Description of Problem (1-2 sentence summary in your own words):
Using a dictionary constant, print out keys, values, and key-value pairs in
different sort orders.
"""

MY_DICT = {'a':15, 'c':18, 'b':20}

# 4.4a
# print all keys as a list
print(f"Keys: {list(MY_DICT.keys())}")

# 4.4b
# print all values as comma separated data
values = ", ".join([str(x) for x in MY_DICT.values()])
print(f"Values: {values}")

# 4.4c
# print all key-value pairs as comma separated data
key_value_pairs = ["{}: {}".format(key, value) for key, value in
                   MY_DICT.items()]
key_value_string = ", ".join(key_value_pairs)
print(f"Key value pairs: {key_value_string}")

# 4.4d
# print dictionary items as list of tuples, in ascending order by key
print(f"Key value pairs ordered by key: {sorted(list(MY_DICT.items()))}")

# 4.4e
# print dictionary items as comma separated data, in ascending order by value
# if use of lambda is allowed, then the following works and is much cleaner
items_by_value = sorted(MY_DICT.items(), key=lambda x: x[1])

# if use of lambda is not allowed, then the following commented-out code works
# items_by_value = []
# values = list(MY_DICT.values())
# while values:
#     for key, value in MY_DICT.items():
#         if values and value == min(values):
#             items_by_value.append((key, value))
#             values.remove(value)

key_value_pairs = ["{}: {}".format(key, value) for key, value in
                   items_by_value]
key_value_string = ", ".join(key_value_pairs)
print(f"Key value pairs ordered by value: {key_value_string}")
