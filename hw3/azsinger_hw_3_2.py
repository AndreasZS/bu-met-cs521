"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/04
Homework Problem # 3_2
Description of Problem (1-2 sentence summary in your own words):
Create a docstring containing three sentences then print out counts based on the
 different characters in the strings.
"""

import re
import string


# 3.2a
DOCSTRING_CONSTANT = """The quick brown fox jumps over the lazy dog. Sphinx of \
black quartz, judge my vow. How quickly daft jumping zebras vex!
"""

# 3.2b
# use re.split() to account for sentences that end in '!' or '?' instead of '.'
sentences = re.split("[.!?]", DOCSTRING_CONSTANT)

# 3.2c
print(f"#{'# Upper':>11}{'# Lower':>11}{'# Digits':>12}{'# Punct.':>12}")
print(f"-{'-------':>11}{'-------':>11}{'--------':>12}{'--------':>12}")
for ind, sentence in enumerate(sentences):
    # split() includes a new line at the end, if there is one. Skip this
    if sentence in string.whitespace:
        continue

    count_uppercase = 0
    count_lowercase = 0
    count_digits = 0
    # initialize count_punctuation as 1 to account for chars removed by split()
    count_punctuation = 1

    for char in sentence:
        if char.isupper():
            count_uppercase += 1
        elif char.islower():
            count_lowercase += 1
        elif char.isdigit():
            count_digits += 1
        elif char in string.punctuation:
            count_punctuation += 1

    print(f"{ind + 1:^1}{' '*4}{count_uppercase:^7}{' '*4}{count_lowercase:^7}\
{' '*4}{count_digits:^8}{' '*4}{count_punctuation:^8}")
