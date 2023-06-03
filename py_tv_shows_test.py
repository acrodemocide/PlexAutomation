import os
from file_and_directory_util import generate_directories, generate_sequential_dirs, generate_file
from os.path import join

def generate_generic_tv_shows(
    base_path,
    number_of_tv_shows,
    number_of_seasons,
    number_of_discs_per_show,
    number_of_episodes_per_disc):

    if not os.path.exists(base_path):
        os.makedirs(base_path)

    tv_show_dirs = generate_directories(base_path, number_of_tv_shows)

    for tv_show_dir in tv_show_dirs:
        season_dirs = generate_sequential_dirs(tv_show_dir, "Season", number_of_seasons)
        for season_dir in season_dirs:
            disc_dirs = generate_sequential_dirs(season_dir, "Disc", number_of_discs_per_show)
            for disc_dir in disc_dirs:
                for i in range(number_of_episodes_per_disc):
                    file_size = 500
                    generate_file(f"{disc_dir}/A{i}.mkv", file_size)

def generic_tv_shows_test():
    base_path = "tv_shows"
    number_of_tv_shows = 10
    number_of_seasons = 5
    number_of_discs_per_show = 4
    number_of_episodes_per_disc = 5

    generate_generic_tv_shows(
        base_path, 
        number_of_tv_shows,
        number_of_seasons,
        number_of_discs_per_show, 
        number_of_episodes_per_disc)

    # Verify tv shows laid out as expected
    if not os.path.exists(base_path):
        print(f"Failed! Base Path {base_path} does not exist")
    tv_shows = os.listdir(base_path)
    for tv_show in tv_shows:
        tv_show_path = join(base_path, tv_show)
        seasons = os.listdir(tv_show_path)
        if len(seasons) != number_of_seasons:
            print(f"Failed! Actual number of seasons {len(seasons)} != expected {number_of_seasons}")
        for season in seasons:
            season_path = join(tv_show_path, season)
            discs = os.listdir(season_path)
            if len(discs) != number_of_discs_per_show:
                print(f"Failed! Actual number of discs {len(discs)} != expected {number_of_discs_per_show}")
            for disc in discs:
                disc_path = join(season_path, disc)
                episodes = os.listdir(disc_path)
                if len(episodes) != number_of_episodes_per_disc:
                    print(f"Failed! Actual number of episodes {len(episodes)} != expected {number_of_episodes_per_disc}")

generic_tv_shows_test()