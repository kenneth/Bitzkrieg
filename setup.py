import os
from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Bitzkrieg",
    version = "0.0.1",
    author = "Gavin Chan",
    author_email = "gavincyi@gmail.com",
    description = ("Lightning bitcoin trading system."),
    license = "MIT",
    keywords = "bitcoin",
    url = "https://github.com/gavincyi/Bitzkrieg",
    packages=['bitz'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: The MIT License",
    ],
    entry_points={
            'console_scripts': ['bitz=bitz.bitzkrieg:main',
                                'balance_archive=bitz.balance_archive:main',
                                'gatecoin=bitz.exch_gatecoin_eis:main']
        },    
    install_requires=[
            'pytest',
            'lightmatchingengine', 
            'pyzmq',
            'redis',
            'PyJWT',
            'mock',
            'requests',
            'pymysql'
    ],
)
