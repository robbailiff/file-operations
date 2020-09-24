# Import libraries
import os
import csv

# Directories
orig_dir = "Z:\ARCHIVE\LIVE_ARCHIVE\8000-8999\8176_Permo_Triassic\Permo-Triassic\Data\Figures"
new_dir = "S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Images\From Archive"

# Find all original files in folders and sub folders
orig_files = []
for root, dirs, files in os.walk(orig_dir):
    for name in files:
        orig_files.append(os.path.join(root, name))

print("Number of original files: %d" % len(orig_files))

# Find all files in new folder and remove non-image files from list
new_all = os.listdir(new_dir)
file_types = [".jpg", ".png", ".tif", ".img", ".bmp"]
new_files = [x for x in new_all if x[-4:].lower() in file_types]

print("Number of new files: %d" % len(new_files))

# Find matches between the 2 directories and append the filepath and filename to the match_files list
match_files = []

for file in new_files:
    for item in orig_files:
        column_list = []
        f_path = '\\'.join(item.split('\\')[:-1])
        f_name = item.split('\\')[-1]
        column_list.append(f_path)
        column_list.append(f_name)
        
        if f_name == file:
            match_files.append(column_list)

print("Number of matched files: %d" % len(match_files))
#print(match_files[0])

# Find user homepath
home_path = os.path.expanduser('~')

# Write to users homepath and save as csv file. Open in binary mode to avoid extra carriage return
with open(home_path + "\\file_match.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(match_files)

f.close()

print("File saved to %s\\file_match.csv" % home_path)