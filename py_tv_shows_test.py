import os
from random import randrange
from file_and_directory_util import generate_directories

base_path = "./tv_shows"
number_of_tv_shows = 10
number_of_discs_per_show = 4
number_of_episodes_per_disc = 5

test_show_folder_name = "test tv show"
tv_show_dirs = generate_directories(base_path, number_of_tv_shows)

# def create_seasons_folders = 

def create_tv_show_files():
    for tv_show_dir in tv_show_dirs:
        number_seasons = randrange(1, 4, 1)
        for j in range(number_seasons):
            season_dir = f"{tv_show_dir}/Season 0{j}"
            os.makedirs(season_dir)
            number_of_discs = randrange(1, 6, 1)
            for k in range(number_of_discs):
                disc_dir = f"{season_dir}/Disc {k}"
                os.makdedirs(disc_dir)
                for l in range(number_of_episodes_per_disc):
                



def create_episodes_only_discs(number_of_discs):
    pass

def create_discs_with_special_episode(number_of_discs):
    pass

def create_discs_with_special_features(number_of_discs):
    pass

def create_discs_with_master_file(number_of_discs):
    pass

# Special episodes, special features, and a master_file
def create_discs_with_all_possibilities(number_of_discs):
    pass

def episodes_only_on_disc():
    # Test discs where only files on disc or episodes, and all are of similar length
    pass

def disc_with_special_episode():
    # Test discs where one episode is a special is significantly longer than the others
    pass

def disc_with_special_features():
    # Some discs have special features along with episodes
    pass

def disc_with_master_file():
    # Most discs have a file that contains the entire content contained in all the others
    pass