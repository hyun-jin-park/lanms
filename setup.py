#! /usr/bin/env python3
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import os
import subprocess
from sys import platform
import setuptools


if "linux" in platform:
    from setuptools.dist import Distribution
    # This is a hack around python wheels not including the adaptor.so library.

    class BinaryDistribution(Distribution):
        def is_pure(self):
            return False

        def has_ext_modules(self):
            return True

    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    if subprocess.call(['make', '--always-make','-C', BASE_DIR]) != 0:
        raise RuntimeError('Cannot compile lanms in the directory: {}'.format(BASE_DIR))

    setuptools.setup(
        name='lanms',
        version='1.0.2',
        description='Locality-Aware Non-Maximum Suppression',
        # The project's main homepage.
        url='https://github.com/Parquery/lanms',
        # Author details
        author='argmen (boostczc@gmail.com) is code author, '
               'Dominik Walder (dominik.walder@parquery.com) and Marko Ristin (marko@parquery.com) only packaged the code',
        author_email='devs@parquery.com',
        # Choose your license
        license='GNU General Public License v3.0',
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3.5',
        ],
        keywords='locality aware non-maximum suppression',
        packages=setuptools.find_packages(exclude=[]),
        install_requires=["numpy"],
        include_package_data=True,
        distclass=BinaryDistribution,
    )
elif "win" in platform:
    from distutils.core import setup, Extension
    cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']

    sfc_module = Extension(
        'lanms', sources=['adaptor.cpp', 'include/clipper/clipper.cpp'],
        include_dirs=['pybind11/include', 'include/clipper/clipper.hpp'],
        language='c++',
        extra_compile_args=cpp_args,
    )

    setuptools.setup(
        name='lanms',
        version='1.0.2',
        description='Locality-Aware Non-Maximum Suppression',
        # The project's main homepage.
        url='https://github.com/Parquery/lanms',
        # Author details
        author='argmen (boostczc@gmail.com) is code author, '
               'Dominik Walder (dominik.walder@parquery.com) and Marko Ristin (marko@parquery.com) only packaged the code',
        author_email='devs@parquery.com',
        # Choose your license
        license='GNU General Public License v3.0',
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3.5',
        ],
        keywords='locality aware non-maximum suppression',
        install_requires=["numpy"],
        include_package_data=True,
        ext_modules=[sfc_module],
    )

else:
    print("unsupported platform: {}".format(platform))


