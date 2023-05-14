import math
import os
from random import randrange
from os.path import join, isdir

class TestUtilities:
    def __init__(self, base_path, number_dirs, base_dir_title):
        self.base_path = base_path
        self.number_dirs = number_dirs
        self.base_dir_title = base_dir_title

    def generate_test_mkv_output_dir(self):
        random_year = randrange(1940, 2022, 1)
        movie_name = f"./{self.base_path}/{self.base_dir_title} ({random_year})"
        if not os.path.exists(movie_name):
            os.makedirs(movie_name)

    def generate_directory_tree(self):
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

        for i in range(self.number_dirs):
            self.generate_test_mkv_output_dir()