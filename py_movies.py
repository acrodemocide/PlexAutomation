from os import listdir, stat
from os.path import isfile, join

# TODO: dhoward -- get this via command-line args
path = "./test_movies"
only_mkv_files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.mkv')]

for file in only_mkv_files:
    size = stat(file).st_size
    print(f"File: {file} -- size: {size}")