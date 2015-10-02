# -*- coding: utf-8 -*-
# Inits
from setuptools import setup, find_packages
import sys

# Version, etc
sys.path.insert(0, 'sphinxfortran')
from  sphinxfortran import ( __version__ as version, __author__ as author,
    __email__ as author_email)
del sys.path[0]

# From files
with open('README.rst') as f:
    long_description = f.read()
# From files
with open('requires.txt') as f:
    requires = filter(None, f.read().split('\n'))


# Other infos
description = 'Fortran domain and autodoc extensions to Sphinx'
maintainer = author
maintainer_email = author_email
license = "CeCiLL-A"
url = "http://www.ifremer.fr/vacumm"
classifiers=[]


if __name__ == '__main__':

    # Lauch setup
    setup(name='sphinx-fortran',
        version=version,
        description=description,
        long_description=long_description,
        author=author,
        author_email=author_email,
        maintainer=author,
        maintainer_email=author_email,
        license=license,
        url=url,
        classifiers=classifiers,
        packages=find_packages(),
        install_requires=requires,
    )


