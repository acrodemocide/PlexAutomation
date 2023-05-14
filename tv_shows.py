import os
from os.path import join, isdir

base_path = "tv_shows"

def get_child_directories(path):
    children = [f for f in os.listdir(path) if isdir(join(path, f))]
    return children

tv_shows = get_child_directories(base_path)
print(tv_shows)

tv_show = join(base_path, tv_shows[0])
seasons = get_child_directories(tv_show)
print(seasons)