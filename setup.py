from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'

def get_requirements(req_path: str) -> List[str]:
    '''
    this function is to pull the required packages from requirements.txt
    '''

    requirements = []
    with open(req_path, "r") as infile:
        requirements = infile.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='marine_ai',
    version='0.0.1',
    # TODO: Need to add George also
    author='Michael'
    author_email='mtallini361@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)