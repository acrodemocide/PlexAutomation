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
