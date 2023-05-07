import sys
from os import listdir, stat, remove, rename
from os.path import isfile, join, isdir

base_path = sys.argv[1]
movie_folders = [f for f in listdir(base_path) if isdir(join(base_path, f))]

for movie_folder in movie_folders:
    path = f"{base_path}/{movie_folder}"
    only_mkv_files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.mkv')]

    largest_file_size = 0
    largest_file = ""
    for file in only_mkv_files:
        full_file_path = f"{path}/{file}"
        size = stat(full_file_path).st_size
        if size > largest_file_size:
            largest_file_size = size
            largest_file = file
        print(f"File: {file} -- size: {size}")

    print(f"largest_file: {largest_file} -- largest_file_size: {largest_file_size}")

    files_to_delete = [f for f in only_mkv_files if f != largest_file]
    print("Files to delete:")
    for file in files_to_delete:
        full_file_path = f"{path}/{file}"
        size = stat(full_file_path).st_size
        print(f"File: {file} -- size: {size}")
        remove(full_file_path)

    rename(f"{path}/{largest_file}", f"{movie_folder}.mkv")