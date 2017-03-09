#!/usr/bin/env python3

import os
import subprocess
import sys
import argparse

VERSION = 'pyunz 0.2'

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
    subprocess.run([bin('tar'), args, file])

def unzip(file):
    if 'core_perl' in bin('unzip'):
        print("You don't have unzip")
        return sys.exit(1)
    args = '-o'
    subprocess.run([bin('unzip'), args, file])

def un7z(file):
    _7z = '7z'
    _7za = '7za'
    args1 = 'x'
    args2 = '-y'

    if 'core_perl' not in bin(_7z):
        subprocess.run([bin(_7z), args1, args2, file])
    elif 'core_perl' not in bin(_7za):
        subprocess.run([bin(_7za), args1, args2, file])
    else:
        print("You don't have 7z or 7za")
        return sys.exit(1)

def compress_tar(type, i_file, o_file):
    if type == 'tgz':
        args = 'cvzf'
        subprocess.run([bin('tar'), args, o_file, i_file])

    elif type == 'txz':
        args = 'cvJf'
        subprocess.run([bin('tar'), args, o_file, i_file])

    elif type == 'tbz':
        args = 'cvjf'
        subprocess.run([bin('tar'), args, o_file, i_file])

def compress_7z(i_file, o_file):
    args = 'a'
    _7z = '7z'
    _7za = '7za'
    if 'core_perl' not in bin(_7z):
        subprocess.run([bin(_7z), args, o_file, i_file])

    elif 'core_perl' not in bin(_7za):
        subprocess.run([bin(_7za), args, o_file, i_file])

def compress_zip(i_file, o_file):
    subprocess.run([bin('zip'), o_file, i_file])

def package_error():
    print('Is it a package?')
    return sys.exit(1)

parser = argparse.ArgumentParser(description = 'an extract tool for tgz, zip, 7z...')
parser.add_argument('-x', '--extract', help = 'extract the package automatically')
parser.add_argument('-v', '--version',action = 'store_true', help = 'print version')
parser.add_argument('-i', '--input', help = 'create a package')
parser.add_argument('-t', '--type', choices = ['tgz', 'tbz', 'txz', '7z', 'zip'], help = 'choose the package type')
parser.add_argument('-o', '--output', help = 'the package name')


args = parser.parse_args()


try:
    zfile_type = file_type(args.extract)
except TypeError:
    pass


if args.extract:
    if zfile_type == b'application/x-7z-compressed':
        un7z(args.extract)

    elif (zfile_type == b'application/x-gzip' or zfile_type == b'application/x-xz' or
        zfile_type == b'application/x-bzip2'):
        untar(args.extract)

    elif zfile_type == b'application/zip':
        unzip(args.extract)

    else:
        package_error()

if args.version:
    print(VERSION)


if args.type == 'tgz':
    compress_tar(args.type, args.input, args.output)

elif args.type == 'tbz':
    compress_tar(args.type, args.input, args.output)

elif args.type == 'txz':
    compress_tar(args.type, args.input, args.output)

elif args.type == '7z':
    compress_7z(args.input, args.output)

elif args.type == 'zip':
    compress_zip(args.input, args.output)
