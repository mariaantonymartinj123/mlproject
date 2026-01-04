from setuptools import find_packages, setup
from typing import List

h_e_d='-e .'
def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirement = []
        with open(file_path) as file_obj:
            requirement=file_obj.readlines()
            [req.replace("\n"," ") for req in requirement]
            if h_e_d in requirement:
                requirement.remove(h_e_d)
        return requirement

setup(
    name='mlproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt"),
    author='Maria Antony Martin J',
    author_email='mariaantonyprofessional@gmail.com',
    description='A machine learning project setup',
)