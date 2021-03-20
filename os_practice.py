#!/usr/bin/env python3
import os
import shutil
from datetime import datetime
#get current director
print(os.getcwd())

#change directory to ...
#os.chdir('/home/ivanperez/Projects/')

# list files and folders in current directory
print(os.listdir())

#makes subdirectory if parent directory doesn't exist
#os.makedirs('makedirs_test_2/subdir1')

#make one directory. if parent doesn't exist then it will fail. it expects parent and targets the last sub dir specified
#os.mkdir('makedir_test_1')
#os.mkdir('makedir_test_1/subdir1')

#print(os.listdir())

#removes one directory. if dir is not empty will fail
#os.rmdir('makedirs_test_2/subdir1','makedir_test_1')
#removes recursively all folders. only if not empty
#os.removedirs('makedir_test_1/subdir1')

#print(os.listdir())

#delete file tree even if not empty.
#shutil.rmtree('makedirs_test_2/')

#os.rename('file1.txt', 'renamedfile1.txt')
#print(os.listdir())

mod_time = os.stat('file2.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
