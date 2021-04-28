#!/usr/bin/env python3
import os


#input for working dir
root_path = input("Provide path to files:\n")
#allow linux relative file path i.e. ~/
os.chdir(os.path.expanduser(root_path))
print(root_path)
#reset path variable to relative path
root_path = os.getcwd()

exten = '.mkv'

#function of video file extensions
#def vid_files(vid_dir, vid_exten=['avi', 'mp4', 'mkv', 'mov']):
#    ''' Print files in vid_dir with extensions in vid_exten, recursively.'''

#check if file or Directory
#if os.path.isfile()
#walking directory
print("******Start os walk**********")
for dirpath, subdir, files in os.walk(root_path):
    for name in files:
        if name.endswith(exten):
            print(name)
    #print("files:", files)
    print('*' * 25)
print("******End os walk**********")
