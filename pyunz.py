import os
import subprocess
import click

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

print(file_type('/tmp/mentohust.7z'))

def untar(file):
    args = '-xvf'
    subprocess.check_output([bin('tar'), args, file])

def unzip(file):
    args = '-o'
    subprocess.check_output([bin('unzip'), args, file])

def un7z(file):
    args1 = 'x'
    args2 = 'y'
    subprocess.check_output([bin('7za'), args1, args2, file])
