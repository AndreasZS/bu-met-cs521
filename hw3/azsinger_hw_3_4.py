"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/05
Homework Problem # 3_4
Description of Problem (1-2 sentence summary in your own words):
Read a one-sentence file, write the sentence as four lines of five word output
to an output file.
"""

import os.path


INPUT_FILE_NAME = "cs521_3_4_input.txt"
REQUIRED_WORD_COUNT = 20
NUM_WORDS_PER_LINE = 5
OUTPUT_FILE_NAME = "cs521_3_4_output.txt"

if not os.path.exists(INPUT_FILE_NAME):
    print(f"ERROR: {INPUT_FILE_NAME} does not exist in current directory.")
    exit(-1)
else:
    with open(INPUT_FILE_NAME, "r") as text_file:
        content = text_file.read()
        words = content.split()
        if len(words) != REQUIRED_WORD_COUNT:
            print(f"ERROR: File does not contain {REQUIRED_WORD_COUNT} words.")
            exit(-1)
        with open(OUTPUT_FILE_NAME, "w") as output_file:
            for ind in range(0, REQUIRED_WORD_COUNT, NUM_WORDS_PER_LINE):
                line = " ".join(words[ind:ind+NUM_WORDS_PER_LINE]) + "\n"
                output_file.write(line)
        print(f"Success! Output written to: {OUTPUT_FILE_NAME}")
