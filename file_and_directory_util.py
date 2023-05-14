import math
import os
from random import randrange
from os.path import join, isdir

def generate_directories(base_path, number_dirs):
    generated_dirs = []
    for i in range(number_dirs):
        random_year = randrange(1940, 2022, 1)
        dir_path = f"./{base_path}/test ({random_year})"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            generated_dirs.append(dir_path)
    
    return generated_dirs

def generate_sequential_dirs(base_path, base_name, max_number_to_generate):
    number_to_generate = randrange(1, max_number_to_generate, 1)
    generated_dirs = []
    for i in range(number_to_generate):
        generated_dir = f"{base_path}/{base_name} {i}"
        if not os.path.exists(generated_dir):
            os.makedirs(generated_dir)
            generated_dirs.append(generated_dir)
    return generated_dirs


def generate_file(file_name, number_of_bytes):
    fp = open(file_name, "w")
    for j in range(number_of_bytes):
        fp.write("a")
    fp.close()

# for movie_folder in generated_movie_folders:
#     for i in range(number_of_files):
#         rough_midpoint = math.floor(number_of_files / 2)
#         file_size = 0
#         # Create largest file here
#         if i == rough_midpoint:
#             file_size = largest_file_size
#         else:
#             file_size = randrange(1, (largest_file_size - 1), 1)
        
#         generate_test_file(f"{base_path}/{movie_folder}/file{i}.mkv", file_size)

# def generate_sequential_files(base_path, base_name, max_number_to_generate):
#     number_to_generate = randrange(1, max_number_to_generate, 1)
#     generated_files = []
#     for i in range(number_to_generate):
#         generated_file = f"{base_path}/{base_name} {i}"
#         if not os.path.exists(generated_file):
#             os.makedirs(generated_file)
#             generated_files.append(generated_file)
#     return generated_files
#     pass
