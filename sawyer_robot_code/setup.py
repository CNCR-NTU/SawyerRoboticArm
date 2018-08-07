#!/usr/bin/env python
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['biotac_driver', 'biotac_log', 'biotac_log_parser',
                 'biotac_sensors']
d['package_dir'] = {'': 'src'}

setup(**d)
