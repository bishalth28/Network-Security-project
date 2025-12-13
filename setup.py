'''
the setup.py file is used for packaging Python projects. It contains metadata about the project and instructions on how to install it.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    this function will retun list of requirements
    """
    requirement_lst = []
    try:
       with open("requirements.txt", "r") as f:
          lines = f.readlines()
          for line in lines:
             requirement=line.strip()
             if requirement and requirement!= '-e .':
                requirement_lst.append(requirement)
    except FileNotFoundError:
         print("requirements.txt file not found.")

    return requirement_lst
print(get_requirements())   

setup(
    name="Network_Security",
    version="0.0.1",
    author="Bishal Thapa",
    author_email="btbishal09@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)