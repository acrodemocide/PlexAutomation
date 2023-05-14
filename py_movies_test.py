import math
import os
from random import randrange
from os.path import join, isdir
from file_and_directory_util import generate_directories, generate_file

base_path = "./movies"
number_of_movies = 10
number_of_files = 10
largest_file_size = 1000

if not os.path.exists(base_path):
    os.makedirs(base_path)

# generate test movie folders
base_dir_title = "test movie"
generate_directories(base_path, number_of_movies)

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
        
        generate_file(f"{base_path}/{movie_folder}/file{i}.mkv", file_size)
