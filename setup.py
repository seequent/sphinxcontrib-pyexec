from distutils.core import setup
from setuptools import find_packages

CLASSIFIERS = [
'Development Status :: 3 - Alpha',
'Intended Audience :: Developers',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3.3',
'Programming Language :: Python :: 3.4',
'Programming Language :: Python :: 3.5',
'Operating System :: Microsoft :: Windows',
'Operating System :: POSIX',
'Operating System :: Unix',
'Operating System :: MacOS',
'Natural Language :: English',
]

with open('README.md') as fp:
    LONG_DESCRIPTION = ''.join(fp.readlines())

setup(
    name = 'sphinxcontrib-pyexec',
    version = '0.0.4',
    packages = find_packages(),
    install_requires = ['sphinx',
                        'docutils',
                       ],
    author = 'Lindsey Heagy',
    author_email = 'lindsey@3ptscience.com',
    description = 'sphinxcontrib-pyexec',
    long_description = LONG_DESCRIPTION,
    license = 'MIT',
    keywords = 'sphinx documentation python execute',
    url = 'https://github.com/3ptscience/sphinxcontrib-pyexec',
    download_url = 'https://github.com/3ptscience/sphinxcontrib-pyexec',
    classifiers = CLASSIFIERS,
    platforms = ['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
    use_2to3 = False,
)
