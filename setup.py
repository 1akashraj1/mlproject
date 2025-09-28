from setuptools import setup, find_packages
from typing import List

def get_packages(file_path: str) -> List[str]:
    'this function will return the list of requirements from file_path'

    requirements = []
    with open(file_path) as file:
        list_ = file.readlines()
        requirements = [req.replace('\n','') for req in list_]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Akash',
    author_email = 'akash.raj.dhn@gmail.com',
    packages = find_packages(),
    install_requires = get_packages('requirements.txt')

)