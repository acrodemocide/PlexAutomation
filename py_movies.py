from os import listdir, stat
from os.path import isfile, join
onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]

for file in onlyfiles:
    size = stat(file).st_size
    print(f'File: {file} -- size: {size}')