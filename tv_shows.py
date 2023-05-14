import os
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
    print(tv_show)
    tv_show_path = join(base_path, tv_show)
    seasons = get_child_directories(tv_show_path)
    for season in seasons:
        print(season)
        season_path = join(tv_show_path, season)
        discs = get_child_directories(season_path)
        for disc in discs:
            print(disc)
            disc_path = join(season_path, disc)
            files = get_child_files(disc_path)
            files.sort()
            print(files)
