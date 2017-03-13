# pyunz

## usage

```
usage: pyunz.py [-h] [-x EXTRACT] [-v] [-c {tgz,tbz,txz,7z,zip}]
                [archive] [file]

an extract tool for tgz, zip, 7z...

positional arguments:
  archive               package name
  file                  file

optional arguments:
  -h, --help            show this help message and exit
  -x EXTRACT, --extract EXTRACT
                        extract the package automatically
  -v, --version         print version
  -c {tgz,tbz,txz,7z,zip}, --create {tgz,tbz,txz,7z,zip}
                        create package
```

## support

- tar.gz
- tar.xz
- tar.bz
- zip
- 7z

## PS:
看了unp后尝试自己写一个像unp这样的东西，于是pyunz就这样诞生了
