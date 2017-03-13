from setuptools import setup

setup(
    name = 'pyunz',
    license = 'GPL-3.0',
    version = '0.2.3',
    url = 'https://github.com/Sherlock-Holo/pyunz',
    author = 'Sherlock Holo',
    author_email = 'sherlockya@gmail.com',
    description = 'an extract wrapper',
    #packages = ['pyunz.py'],
    scripts = ['pyunz.py'],
    classifiers = [
        'License :: OSI Approved :: GPL-3.0 License',
        'Programming Language :: Python :: 3.6',
        ],
    entry_points = '''
        [console_scripts]
        pyunz = pyunz : cli
    ''',
)
