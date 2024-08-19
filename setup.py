from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function return the list of requirements
    '''
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        


setup(
    name='ml-projects',
    version ='0.0.1',
    author='Aati',
    autor_email='aarti15052004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)