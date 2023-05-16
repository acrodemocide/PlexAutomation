import os
from os import rmdir, rename
from os.path import join, isdir

base_path = "tv_shows"

def get_child_directories(path):
    children = [f for f in os.listdir(path) if isdir(join(path, f))]
    return children

def get_child_files(path):
    children = [f for f in os.listdir(path) if not isdir(join(path, f))]
    return children

tv_shows = get_child_directories(base_path)
for tv_show in tv_shows:
    tv_show_path = join(base_path, tv_show)
    seasons = get_child_directories(tv_show_path)
    for season in seasons:
        season_number = int(season.split()[1])
        season_path = join(tv_show_path, season)
        if (season_number < 10):
            file_name_prefix = f"{tv_show} - s0{season_number}"
        else:
            file_name_prefix = f"{tv_show} - s{season_number}"
        current_episode_number = 1
        discs = get_child_directories(season_path)
        for disc in discs:
            disc_path = join(season_path, disc)
            files = get_child_files(disc_path)
            # Remove files that are not episodes
            files.sort()
            for file in files:
                if (current_episode_number < 10):
                    new_file_name = f"{file_name_prefix}e0{current_episode_number}.mkv"
                else:
                    new_file_name = f"{file_name_prefix}e{current_episode_number}.mkv"
                current_episode_number += 1
                cur_file_path = join(disc_path, file)
                new_file_path = join(season_path, new_file_name)
                rename(cur_file_path, new_file_path)
            rmdir(disc_path)


            
