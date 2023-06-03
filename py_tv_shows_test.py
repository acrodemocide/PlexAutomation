import os
from file_and_directory_util import generate_directories, generate_sequential_dirs, generate_file

base_path = "tv_shows"
number_of_tv_shows = 10
number_of_discs_per_show = 4
number_of_episodes_per_disc = 5

def generate_generic_tv_shows():
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    tv_show_dirs = generate_directories(base_path, number_of_tv_shows)

    for tv_show_dir in tv_show_dirs:
        season_dirs = generate_sequential_dirs(tv_show_dir, "Season", 5)
        for season_dir in season_dirs:
            disc_dirs = generate_sequential_dirs(season_dir, "Disc", number_of_discs_per_show)
            for disc_dir in disc_dirs:
                for i in range(number_of_episodes_per_disc):
                    file_size = 500
                    generate_file(f"{disc_dir}/A{i}.mkv", file_size)


generate_generic_tv_shows()