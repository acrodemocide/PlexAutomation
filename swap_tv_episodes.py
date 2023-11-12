#This script is used to reorder TV episodes for a given season if they
#ended up out of order. 
# 
# THIS HAS TO BE RUN FROM THE DIRECTORY CONTAINING THE EPISODES TO BE SWAPPED
#

# The file passed in will be a text file with the following format:
# 01:02
# 03:08
# 10:12

# The above example will swap episode 1 and 2, 3 and 8, and 10 and 12.

# Usage: python swap_tv_episodes.py <swap_file>

import sys
import re
from os import listdir, rename

class swap_instruction:
    def __init__(self, actual_file, expected_file):
        self.actual_file = actual_file
        self.expected_file = expected_file

def swap(episode1, episode2):
    first_file_name = listdir('.')[0]
    actual_file = re.sub(r'e\d\d', f'e{episode1}', first_file_name)
    expected_file = re.sub(r'e\d\d', f'e{episode2}', first_file_name)

    print(f"actual_file: {actual_file}")
    print(f"expected_file: {expected_file}")

    rename(actual_file, 'temp_file')
    actual_file = rename(expected_file, actual_file)
    expected_file = rename('temp_file', expected_file)

swap_file = sys.argv[1]

with open(swap_file) as f:
    swap_instructions = f.readlines()
    swap_instructions = [x.strip() for x in swap_instructions]
    for swap_instruction in swap_instructions:
        split = swap_instruction.split(":")
        actual_file = split[0]
        expected_file = split[1]
        swap(actual_file, expected_file)
