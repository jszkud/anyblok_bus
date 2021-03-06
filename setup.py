# -*- coding: utf-8 -*-
# This file is a part of the AnyBlok / Bus project
#
#    Copyright (C) 2018 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from setuptools import setup, find_packages
import os

version = '0.1.0'


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), 'r',
          encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(
    os.path.join(here, 'doc', 'CHANGES.rst'), 'r', encoding='utf-8'
) as change:
    CHANGES = change.read()

with open(
    os.path.join(here, 'doc', 'FRONT.rst'), 'r', encoding='utf-8'
) as front:
    FRONT = front.read()

requirements = [
    'anyblok',
    'pika',
    'marshmallow',
]

setup(
    name='anyblok_bus',
    version=version,
    description="Bus for anyblok",
    long_description=readme + '\n' + FRONT + '\n' + CHANGES,
    author="jssuzanne",
    author_email='jssuzanne@anybox.fr',
    url="http://docs.anyblok-bus.anyblok.org/%s" % version,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'anyblok_bus=anyblok_bus.scripts:anyblok_bus',
        ],
        'bloks': [
            'bus=anyblok_bus.bloks.bus:Bus',
        ],
        'anyblok.init': [
            'bus_config=anyblok_bus:anyblok_init_config',
        ],
        'anyblok.model.plugin': [
            'bus_validator=anyblok_bus.validator:ValidatorPlugin',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='bus',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=requirements + ['nose'],
)
