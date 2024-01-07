import sys
import os
from os import rmdir, remove, rename, stat
from os.path import join, isdir
import statistics

##Usage:
## Put all folders created for each ripped disc into a single season folder named like <tv_show> Season X
##	For example: My Tv Show (1999) Season 3 or My Tv Show (1999) Season 11
## Disc folders don't need to be named any specific way so long as they are listed in chronological order
## The same is true for episode files -- they don't need to be named in any specific way so long as they
##	are in chronological order
##
##Steps:
##	1- Create a folder with the name of the TV Show (e.g. TV Show (1999)).
##	2- For each season of ripped discs, create a folder for that season (i.e.: "Season 1", "Season 2", ... "Season 11")
##	3- For all ripped discs for a given season, put them in the corresponding season folder.
##		A- They don't need to be named in a particular way, so long as they list in chronological order.
##	4- For each ripped disc folder, manually inspect the ripped files, and delete all non-episodes.
##		A- If you're being completely thorough, you'll preview each file and ensure that they are listed in the
##		correct order the episodes occur (though usually they are).
##		B- Ensure that the episode files are listed in chronological order (they don't need any special naming
##		just so long as they are listed in the folder in chronological order)
##	5- (Optional, but good to do) Make a backup copy of your newly organized file structure somewhere (this can take a little bit).
##	6- Ensure that all your TV shows that you want renamed are co-located and organized as described above.
##	7- Run this program to rename all files to follow proper Plex naming convention and to organize your TV show folder structures
##	for Plex. Essentially, you'll have a TV Show folder (named like it should be on Plex), then subfolders named "Season 01,"
##	"Season 02," etc, then each will contain the list of episodes for that season with each properly named for Plex.
##	8- These files are now ready to be easily fed into Handbrake without needing to make any name changes.

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
        discs.sort()
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
