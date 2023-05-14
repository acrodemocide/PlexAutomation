import math
import os
from random import randrange
from os.path import join, isdir

def generate_directories(base_path, number_dirs):
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    generated_directories = []

    for i in range(number_dirs):
        random_year = randrange(1940, 2022, 1)
        dir_path = f"./{base_path}/test ({random_year})"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            generated_directories.append(dir_path)
    
    return generated_directories

