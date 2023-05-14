import os
from random import randrange
from os.path import join, isdir

base_path = "./tv_shows"
number_of_tv_shows = 10
number_of_discs_per_show = 4
number_of_episodes_per_disc = 5

if not os.path.exists(base_path):
    os.makedirs(base_path)

def generate_test_tv_show_output_dir():
    random_year = randrange(1940, 2022, 1)
    movie_name = f"./{base_path}/test tv show ({random_year})"
    if not os.path.exists(movie_name):
        os.makedirs(movie_name)

for i in range(number_of_tv_shows):
    generate_test_tv_show_output_dir()