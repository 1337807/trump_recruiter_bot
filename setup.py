#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='trump_recruiter_bot',
    version='0.1.0',
    description="Trump Recruiter Bot is a Markov chain mashup bot using recruiter spam and Trump speechhes.",
    long_description=readme + '\n\n' + history,
    author="Jonan Scheffler",
    author_email='jonanscheffler@gmail.com',
    url='https://github.com/1337807/trump_recruiter_bot',
    packages=[
        'trump_recruiter_bot',
    ],
    package_dir={'trump_recruiter_bot':
                 'trump_recruiter_bot'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='trump_recruiter_bot',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
