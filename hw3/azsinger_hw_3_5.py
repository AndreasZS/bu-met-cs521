"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/05
Homework Problem # 3_5
Description of Problem (1-2 sentence summary in your own words):
Read a file of student records and process the contents line by line
"""

import os.path


INPUT_FILE_NAME = "cs521_3_5_input.txt"

if not os.path.exists(INPUT_FILE_NAME):
    print(f"ERROR: {INPUT_FILE_NAME} does not exist in current directory.")
    exit(-1)
else:
    with open(INPUT_FILE_NAME, "r") as file:
        tuples = []
        for line in file:
            student_record = line.split(",")
            student_tuple = (student_record[0], int(student_record[1]),
                             float(student_record[2]))
            tuples.append(student_tuple)
        print(f"Student Records: {tuples}")
