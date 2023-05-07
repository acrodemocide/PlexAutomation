import os
from random import randrange

new_path = "./test movies (1978)"
number_of_files = 106
largest_file_size = 1000

def generate_test_file(file_name, number_of_bytes):
    fp = open(file_name, "w")
    for j in range(number_of_bytes):
        fp.write("a")
    fp.close()


if not os.path.exists(new_path):
    os.makedirs(new_path)

for i in range(number_of_files):
    file_size = 0
    # Create largest file here
    if i == 0:
        file_size = largest_file_size
    else:
        file_size = randrange(1, (largest_file_size - 1), 1)
    
    generate_test_file(f"{new_path}/file{i}.mkv", file_size)
