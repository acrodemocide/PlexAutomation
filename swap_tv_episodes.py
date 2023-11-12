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

import sys
from os import listdir, stat, remove, rename, rmdir

class swap_instruction:
    def __init__(self, actual_file, expected_file):
        self.actual_file = actual_file
        self.expected_file = expected_file

def swap(tv_season, episode1, episode2):
    """Takes a season of a TV show and two episodes and swaps them."""
    episode1 = int(episode1)
    episode2 = int(episode2)
    tv_season[episode1], tv_season[episode2] = tv_season[episode2], tv_season[episode1]
    return tv_season

swap_file = sys.argv[1]

with open(swap_file) as f:
    swap_instructions = f.readlines()
    swap_instructions = [x.strip() for x in swap_instructions]
    for swap_instruction in swap_instructions:
        split = swap_instruction.split(":")
        actual_file = split[0]
        expected_file = split[1]
        swap_instruction = swap_instruction(actual_file, expected_file)
