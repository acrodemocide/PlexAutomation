from os import listdir, stat
from os.path import isfile, join
onlyMkvFiles = [f for f in listdir('.') if isfile(join('.', f)) and f.endswith('.mkv')]

for file in onlyMkvFiles:
    size = stat(file).st_size
    print(f'File: {file} -- size: {size}')