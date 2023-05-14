import os
from random import randrange
from os.path import join, isdir
from file_and_directory_util import generate_directories, generate_sequential_dirs, generate_file

base_path = "tv_shows"
number_of_tv_shows = 10
number_of_discs_per_show = 4
number_of_episodes_per_disc = 5

def generate_season_dirs(tv_show_path):
    return generate_sequential_dirs(tv_show_path, "Season", 5)

def generate_disc_dirs(season_path):
    return generate_sequential_dirs(season_path, "Disc", 5)

def generate_episodes_only_files(tv_show_path):
    season_dirs = [f for f in os.listdir(tv_show_path) if isdir(join(tv_show_path, f))]
    for season_dir in season_dirs:
        season_path = f"{tv_show_path}/{season_dir}"
        disc_dirs = [file for file in os.listdir(season_path) if isdir(join(season_path, file))]
        for disc_dir in disc_dirs:
            disc_path = f"{season_path}/{disc_dir}"
            for i in range(number_of_episodes_per_disc):
                file_size = 500
                generate_file(f"{disc_path}/A{i}.mkv", file_size)

if not os.path.exists(base_path):
    os.makedirs(base_path)

tv_show_dirs = generate_directories(base_path, number_of_tv_shows)

for tv_show_dir in tv_show_dirs:
    season_dirs = generate_season_dirs(tv_show_dir)
    for season_dir in season_dirs:
        disc_dirs = generate_disc_dirs(season_dir)
    generate_episodes_only_files(tv_show_dir)

# def create_episodes_only_discs(number_of_discs):
#     pass

# def create_discs_with_special_episode(number_of_discs):
#     pass

# def create_discs_with_special_features(number_of_discs):
#     pass

# def create_discs_with_master_file(number_of_discs):
#     pass

# # Special episodes, special features, and a master_file
# def create_discs_with_all_possibilities(number_of_discs):
#     pass