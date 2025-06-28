import re

# Sample file list
files = ["D2_t07.mkv", "C1_t01.mkv", "C5_t05.mkv", "D1_t06.mkv", "C3_t03.mkv"]

# Extract the track number and sort
def extract_track_number(filename):
    match = re.search(r't(\d+)', filename)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"Track pattern not found in filename: {filename}")


sorted_files = sorted(files, key=extract_track_number)

# Output the sorted list
for f in sorted_files:
    print(f)
