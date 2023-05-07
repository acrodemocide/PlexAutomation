from os import listdir, stat
from os.path import isfile, join

# TODO: dhoward -- get this via command-line args
path = "./test_movies"
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