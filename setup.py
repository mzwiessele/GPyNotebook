#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

# Version number
version = '0.0.1'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'GPyNotebook',
      version = version,
      author = 'Max Zwiessele',
      author_email = "ibinbei@gmail.com",
      description = ("Visualization of GPy models in Ipython Notebook"),
      license = "BSD 3-clause",
      keywords = "machine-learning gaussian-processes kernels ipython-notebook visualization",
      url = "https://github.com/mzwiessele/GPyNotebook",
      packages = [
                  "GPyNotebook",
                  "GPyNotebook.plotting",
                  "GPyNotebook.latent",
                  "GPyNotebook.controls",
                  ],
      package_dir={'GPyNotebook': 'GPyNotebook'},
      package_data = {},
      include_package_data = True,
      py_modules = ['GPyNotebook.__init__'],
      long_description=read('README.md'),
      install_requires=['numpy>=1.7', 'scipy>=0.12', 'GPy>=0.6', 'IPython', 'matplotlib>=1.3', 'seaborn'],
      classifiers=['License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence']
      )
