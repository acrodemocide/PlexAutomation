from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]

for file in onlyfiles:
    print(file)

# print(onlyfiles)