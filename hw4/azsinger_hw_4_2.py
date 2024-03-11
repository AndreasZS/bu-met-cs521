"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/10
Homework Problem # 4_2
Description of Problem (1-2 sentence summary in your own words):
Create a string constant sentence of at least 15 characters. Then, analyze the
letter counts of the sentence and save the results to a dictionary. Finally,
print out the results of the analysis.
"""

# SENTENCE = "WAS IT A RAT I SAW?"
SENTENCE = "Wwwas it a rat I saw?"
print(f'The string being analyzed is: "{SENTENCE}"')

# use upper() to ignore case
sentence_upper = SENTENCE.upper()
# use dictionary comprehension to create letter count dictionary
letter_count_dict = {char: sentence_upper.count(char) for char
                     in sentence_upper if char.isalpha()}

# perform analysis on the letter counts
# the highest count observed
max_count = max(letter_count_dict.values())
# sort the dictionary alphabetically
letter_count_dict = dict(sorted(letter_count_dict.items()))
# the letter(s) that appear most frequently by evaluating the dictionary counts
most_frequent = [letter for letter, count in letter_count_dict.items() if count
                 == max_count]
print(f"1. Dictionary of letter counts: {letter_count_dict}")
# build output message based on letter count analysis
if len(most_frequent) == 1:
    # one most frequent letter
    msg = f'2. Most frequent letter "{most_frequent[0]}" appears'
else:
    # multiple most frequent letters
    msg = f"2. Most frequent letters {most_frequent} appear"

if max_count == 1:
    msg += " {} time.".format(max_count)
else:
    msg += " {} times.".format(max_count)

print(msg)
