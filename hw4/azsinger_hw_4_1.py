"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/10
Homework Problem # 4_1
Description of Problem (1-2 sentence summary in your own words):
Create a constant list using range. Then generate a new list using the constant
 list. The new list is created by taking the sum of nearest neighbors for each
element in the constant list. Finally, print both lists with descriptions.
"""

# 4.1a
# we established in class that this list should include 5
CONSTANT_LIST = list(range(55, 4, -10))

# 4.1b
# initialize the result list
sum_neighbors_list = []
for ind in range(0, len(CONSTANT_LIST)):
    neighbors_sum = 0
    if ind == 0:
        # special case: first element
        neighbors_sum = sum(CONSTANT_LIST[0:2])
    elif ind == (len(CONSTANT_LIST) - 1):
        # special case: last element
        neighbors_sum = sum(CONSTANT_LIST[ind - 1:ind + 1])
    else:
        neighbors_sum = sum(CONSTANT_LIST[ind - 1:ind + 2])
    # append the sum to the new list
    sum_neighbors_list.append(neighbors_sum)

# 4.1c
print(f"Input List: {CONSTANT_LIST}")
print(f"Result List: {sum_neighbors_list}")
