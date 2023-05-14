import math
import os
from random import randrange
from os.path import join, isdir
from file_and_directory_util import TestUtilities

base_path = "./movies"
number_of_movies = 10
number_of_files = 10
largest_file_size = 1000

def generate_test_file(file_name, number_of_bytes):
    fp = open(file_name, "w")
    for j in range(number_of_bytes):
        fp.write("a")
    fp.close()

# generate test movie folders
base_dir_title = "test movie"
util = TestUtilities(base_path, number_of_movies, base_dir_title)
util.generate_directory_tree()

generated_movie_folders = [f for f in os.listdir(base_path) if isdir(join(base_path, f))]

for movie_folder in generated_movie_folders:
    for i in range(number_of_files):
        rough_midpoint = math.floor(number_of_files / 2)
        file_size = 0
        # Create largest file here
        if i == rough_midpoint:
            file_size = largest_file_size
        else:
            file_size = randrange(1, (largest_file_size - 1), 1)
        
        generate_test_file(f"{base_path}/{movie_folder}/file{i}.mkv", file_size)
