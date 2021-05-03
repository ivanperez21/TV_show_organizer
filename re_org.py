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

#loop through each file and format the string to remove file extension and split on '.'
#def vid_str():
for root, subdir, files in os.walk(root_path):
    for video_filename in files:
        if video_filename.endswith(VIDEO_EXTENSIONS):
            for exten in VIDEO_EXTENSIONS:
                video_filename = video_filename.strip(exten)
            video_filename2 = ' '.join(video_filename.split('.'))
            print(video_filename2)
#            return video_filename2

print('*' * 80)
#print(vid_str)



'''
IDEA maybe just take the video file folder name and use it for the formatting.
Use if subdir has video file 1 level down then split and strip and regex...
'''
