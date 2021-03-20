#!/usr/bin/env python3
import os

#get current director
print(os.getcwd())

#change directory to ...
os.chdir('/home/ivanperez/Projects/')

# list files and folders in current directory
print(os.listdir())

#makes subdirectory if parent directory doesn't exist
#os.makedirs('makedirs_test_2/subdir1')

#make one directory. if parent doesn't exist then it will fail. it expects parent and targets the last sub dir specified
#os.mkdir('makedir_test_1')
#os.mkdir('makedir_test_1/subdir1')

print(os.listdir())

os.rmdir('makedirs_test_2/')
#os.removedirs('makedirs_test_2/subdir1')
