#!/usr/bin/env python3
import os
import re

#list with all file extension
VIDEO_EXTENSIONS = ('.wmv', '.avi', '.mkv', '.mp4', '.mpg', '.mpeg', '.mov')

#input for working dir
root_path = input('Provide path to files:\n')
#allow linux relative file path i.e. ~/
os.chdir(os.path.expanduser(root_path))
print(root_path)
#reset path variable to relative path
root_path = os.getcwd()
print('*' * 80)

#loop through and walk every dir in path and print out video Files
def vid_file():
    for root, subdir, files in os.walk(root_path):
        for video_filename in files:
            if video_filename.endswith(VIDEO_EXTENSIONS):
                yield video_filename


#loop through each file and format the string to remove file extension and split on '.'
def vid_str():
    for root, subdir, files in os.walk(root_path):
        for video_filename in files:
            if video_filename.endswith(VIDEO_EXTENSIONS):
                for exten in VIDEO_EXTENSIONS:
                    video_filename = video_filename.strip(exten)
                video_filename = ' '.join(video_filename.split('.'))
                yield video_filename #also can try os.path.join(vi    for root, sub    for root, subdir, files in os.walk(rdir, files in os.walk(rdeo_filename)

vid_file_list = list(vid_file())
print(vid_file_list)
print('*' * 80)
vid_str_list = list(vid_str())
print(vid_str_list)
print('*' * 80)

'''
testing REGEX to find season and episode.
save info to use in mkdir funct of season dir
save tv show name before 'S0xE0x' to use in mkdir funct of series dir.
'''

season = re.compile(r'S\d+')
episode = re.compile(r'E\d+')
#season_split = re.split(r'S\d+')


matches = season.finditer(str(vid_str_list))
#print (start,stop) index location followed by group=text found
for match in season.finditer(str(vid_str_list)):
    print(match.start(), match.end(), match.group())
#prints index in form of '(x, y)'
print('*' * 80)
print(match.span())
print(re.split(season, str(vid_str_list)))


'''
IDEA maybe just take the video file folder name and use it for the formatting.
Use if subdir has video file 1 level down then split and strip and regex...
'''

# TODO make directory of given show name
# print series name and strip or remove all other parts after season #
'''
series = str(vid_str_list.partition)
print(series)
'''
# TODO make directory of given season name

# TODO move video files to its appropriate season directory

# TODO function that defines what season a video file belongs to
