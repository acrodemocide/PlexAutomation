#This script is used to reorder TV episodes for a given season if they
#ended up out of order. 
# 
# THIS HAS TO BE RUN FROM THE DIRECTORY CONTAINING THE EPISODES TO BE REORDERED
# IT IS ESSENTIAL THAT THE FIRST FILE IN THE DIRECTORY IS THE FIRST EPISODE (rename
# this script so that it appears at the bottom of the list if necessary)

# The file passed in will be a text file with the following format:
# 01:02
# 02:03
# 03:08
# 08:01
# 10:12
# 12:10

# The above example will rename the episodes as follows:
# 01 -> 02
# 02 -> 03
# 03 -> 08
# 08 -> 01
# 10 -> 12
# 12 -> 10

# Usage: python swap_tv_episodes.py <swap_file>

import sys
import re
from os import listdir, rename
from os.path import isfile, join

class rename_instruction:
    def __init__(self, actual_file, expected_file):
        self.actual_file = actual_file
        self.expected_file = expected_file

def mark_files_for_rename(base_file_name, actual_episode, expected_episode):    
    file_to_rename = re.sub(r'e\d\d', f'e{actual_episode}', base_file_name)
    new_file_name = f'expected_episode_number{expected_episode}_' + file_to_rename

    print(f"file_to_rename: {file_to_rename}")
    print(f"new_file_name: {new_file_name}")

    rename(file_to_rename, new_file_name)

def rename_marked_files():
    marked_files = [f for f in listdir('.') if isfile(join('.', f)) and f.startswith('expected_episode_number')]
    for marked_file in marked_files:
        # get expected episode number from file name
        expected_episode = re.search(r'expected_episode_number(\d\d)', marked_file).group(1)
        # Replace the number r'e\d\d' with the expected episode number
        file_name_with_expected_episode = re.sub(r'e\d\d', f'e{expected_episode}', marked_file)
        new_file_name = re.sub(r'expected_episode_number\d\d_', '', file_name_with_expected_episode)
        rename(marked_file, new_file_name)

swap_file = sys.argv[1]

with open(swap_file) as f:
    swap_instructions = f.readlines()
    swap_instructions = [x.strip() for x in swap_instructions]
    base_file_name = listdir('.')[0]
    for rename_instruction in swap_instructions:
        split = rename_instruction.split(":")
        actual_file = split[0]
        expected_file = split[1]
        mark_files_for_rename(base_file_name, actual_file, expected_file)
    rename_marked_files()
