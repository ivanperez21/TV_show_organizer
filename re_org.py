#!/usr/bin/env python3
import os
import re

#list with all file extention
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
                print(video_filename)


#loop through each file and format the string to remove file extension and split on '.'
def vid_str():
    for root, subdir, files in os.walk(root_path):
        for video_filename in files:
            if video_filename.endswith(VIDEO_EXTENSIONS):
                for exten in VIDEO_EXTENSIONS:
                    video_filename = video_filename.strip(exten)
                video_filename = ' '.join(video_filename.split('.'))
                print(video_filename)

vid_file()
print(type(vid_file()))
print('*' * 80)
vid_str()
print(type(vid_str()))
print('*' * 80)

'''
testing REGEX to find season and episode.
save info to use in mkdir funct of season dir
save tv show name before 'S0xE0x' to use in mkdir funct of series dir.
'''



test_str = 'Kims Convenience S05E05 A Tangled Web 1080p iT WEB-DL DD5 1 H264-KiMCHi'
season = re.compile(r'S\d+')
episode = re.compile(r'E\d+')
#season_split = re.split(r'S\d+')

matches = season.finditer(test_str)
#print start,stop index location. group=text found
for match in season.finditer(test_str):
    print(match.start(), match.end(), match.group())
#prints index in form of '(x, y)'
print(match.span())
print(re.split(season, test_str))
'''
this doesn't work. python doesn't see vid_str as a string i guess.
maybe need to loop it? or find a way to go through it line by line?

'''
#print(re.split(season, vid_str()))

#make series and season dir from input of ...
#def mk_shw_dir(series, season):
#    os.mkdir
#if-elif-else folder already exists then break/cancel making duplicate folder

'''
IDEA maybe just take the video file folder name and use it for the formatting.
Use if subdir has video file 1 level down then split and strip and regex...
'''
