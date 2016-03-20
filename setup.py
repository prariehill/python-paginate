"""
python-paginate
--------------

Pagination support for python web frameworks (study from will_paginate).
Supported CSS: bootstrap2&3&4, foundation and semanticui
Supported web frameworks: Flask, Tornado
"""
from setuptools import setup

setup(
    name='python-paginate',
    version='0.0.1',
    url='https://github.com/lixxu/python-paginate',
    license='BSD',
    author='Lix Xu',
    author_email='xuzenglin@gmail.com',
    description='Simple paginate support for python web frameworks',
    long_description=__doc__,
    packages=['python_paginate'],
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)