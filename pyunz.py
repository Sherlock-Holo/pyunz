#!/usr/bin/env python3

import os
import subprocess
import sys
#import getopt

#zlist = []

def bin(name):
    path = os.environ.get('PATH')
    path = path.split(os.pathsep)
    for bin_path in path:
        binary = os.path.join(bin_path, name)
        if os.access(binary,os.X_OK):
            break

    return binary

def file_type(file):
    file_bin = 'file'
    file_type = subprocess.Popen([file_bin,'-b','--mime-type',file],
                                 stdout = subprocess.PIPE,stderr = subprocess.DEVNULL)
    file_type = file_type.communicate()[0]
    return file_type.strip()

def untar(file):
    args = '-xvf'
    subprocess.Popen([bin('tar'), args, file])

def unzip(file):
    args = '-o'
    subprocess.Popen([bin('unzip'), args, file])

def un7z(file):
    args1 = 'x'
    args2 = '-y'
    subprocess.Popen([bin('7za'), args1, args2, file])

zfile = sys.argv[1]
zfile_type = file_type(zfile)

if zfile_type == b'application/x-7z-compressed':
    un7z(zfile)

elif (zfile_type == b'application/x-gzip' or zfile_type == b'application/x-xz' or
    zfile_type == b'application/x-bzip2'):
    untar(zfile)

elif zfile_type == b'application/zip':
    unzip(zfile)

else:
    print('failed')
