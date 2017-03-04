#!/usr/bin/env python3

import os
import subprocess
import sys
#import getopt

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
    if 'core_perl' in bin('tar'):
        print("You don't have tar")
        return sys.exit(1)
    args = '-xvf'
    subprocess.Popen([bin('tar'), args, file])

def unzip(file):
    if 'core_perl' in bin('unzip'):
        print("You don't have unzip")
        return sys.exit(1)
    args = '-o'
    subprocess.Popen([bin('unzip'), args, file])

def un7z(file):
    _7z1 = '7z'
    _7z2 = '7za'
    args1 = 'x'
    args2 = '-y'

    if 'core_perl' not in bin(_7z1):
        subprocess.Popen([bin(_7z1), args1, args2, file])
    elif 'core_perl' not in bin(_7z2):
        subprocess.Popen([bin(_7z2), args1, args2, file])
    else:
        print("You don't have 7z or 7za")
        return sys.exit(1)

def pkg_error():
    print('Is it a package?')
    return sys.exit(1)

def not_found():
    print('Where is the package?')
    return sys.exit(1)

try:
    zfile = sys.argv[1]
    zfile_type = file_type(zfile)

except IndexError:
    not_found()


if zfile_type == b'application/x-7z-compressed':
    un7z(zfile)

elif (zfile_type == b'application/x-gzip' or zfile_type == b'application/x-xz' or
    zfile_type == b'application/x-bzip2'):
    untar(zfile)

elif zfile_type == b'application/zip':
    unzip(zfile)

else:
    pkg_error()
