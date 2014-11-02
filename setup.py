from setuptools import setup, find_packages
from pypandoc import convert


classifiers = [
    'Environment :: Console',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7'
]

setuptools_kwargs = {
    'install_requires': [
        'click>=3.3,<4'
    ],
    'setup_requires': [
        'wheel>=0.24.0,<1',
        'pypandoc>=0.8.2,<1'
    ],
    'entry_points': {
        'console_scripts': [
            'pymr-register = pymr.register:register',
            'pymr-run = pymr.run:run'
        ]
    }
}


def get_version():
    version_file = open('./VERSION')
    return version_file.read().strip()


def get_readme():
    return convert('./README.md', 'rst')


setup(
    name='pymr',
    description='',
    long_description=get_readme(),
    author='Kyle W Purdon',
    author_email='kylepurdon@gmail.com',
    url='https://github.com/kpurdon/pymr',
    version=get_version(),
    packages=find_packages(),
    classifiers=classifiers,
    **setuptools_kwargs
)
