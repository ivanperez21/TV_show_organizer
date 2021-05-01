#!/usr/bin/env python3
import os

#list with all file extention
VIDEO_EXTENSIONS = ('.wmv', '.avi', '.mkv', '.mp4', '.mpg', '.mpeg', '.mov')

#input for working dir
root_path = input('Provide path to files:\n')
#allow linux relative file path i.e. ~/
os.chdir(os.path.expanduser(root_path))
print(root_path)
#reset path variable to relative path
root_path = os.getcwd()


#loop through and walk every dir in path and print out video Files
for root, subdir, files in os.walk(root_path):
    for video_filename in files:
        if video_filename.endswith(VIDEO_EXTENSIONS):
            print(video_filename)
print('*' * 80)
#TODO: loop through each file and format the string to remove file extension and split on '.'
for root, subdir, files in os.walk(root_path):
    for video_filename in files:
        if video_filename.endswith(VIDEO_EXTENSIONS):
            for exten in VIDEO_EXTENSIONS:
                video_filename = video_filename.strip(exten)
            print(video_filename.split('.'))
