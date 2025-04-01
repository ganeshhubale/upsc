# setup.py
from setuptools import setup, find_packages

setup(
    name='upsc',
    version='0.1',
    packages=find_packages(),
    description='A simple calculator for GS and CSAT exam scores.',
    author='Ganesh Hubale',
    author_email='ganeshhubale03@gmail.com',
    url='https://github.com/ganeshhubale/upsc', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'exam-score-calculator=upsc.calculator:main',
        ],
    },
)

