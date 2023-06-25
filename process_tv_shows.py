import sys
import os
from os import rmdir, remove, rename, stat
from os.path import join, isdir
import statistics

base_path = sys.argv[1]

def get_child_directories(path):
    children = [f for f in os.listdir(path) if isdir(join(path, f))]
    return children

def get_child_files(path):
    children = [f for f in os.listdir(path) if not isdir(join(path, f))]
    return children

# TODO: work on this later -- the different kinds of TV shows have widely enough
#   varying lengths that trying to do this right out the gate is going to be
#   really difficult.
def remove_files_that_are_not_episodes(file_paths):
    file_lengths = [stat(f).st_size for f in file_paths]
    print(f"file_lengths: {file_lengths}")
    mean_length = statistics.mean(file_lengths)
    print(f"mean_length: {mean_length}")
    filtered_files = [f for f in file_paths if stat(f).st_size < 2 * mean_length and stat(f).st_size > 0.75 * mean_length]
    [remove(f) for f in file_paths if stat(f).st_size >= 2 * mean_length or stat(f).st_size <= 0.75 * mean_length]
    return filtered_files

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
            # TODO: We'll use this call instead once we figure out a good way to filter out all non-episode files
            # episode_file_paths = remove_files_that_are_not_episodes([join(disc_path, f) for f in files])
            episode_file_paths = [join(disc_path, f) for f in files]
            episode_file_paths.sort()
            for episode_file_path in episode_file_paths:
                if (current_episode_number < 10):
                    new_file_name = f"{file_name_prefix}e0{current_episode_number}.mkv"
                else:
                    new_file_name = f"{file_name_prefix}e{current_episode_number}.mkv"
                current_episode_number += 1
                new_file_path = join(season_path, new_file_name)
                rename(episode_file_path, new_file_path)
            rmdir(disc_path)
