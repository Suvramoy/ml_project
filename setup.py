from setuptools import find_packages,setup
from typing import List  # for  return a list bcs the requirements.txt return a list


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)# for not trigger the -e . in requirements.txt
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='suvramoy',
author_email='suvramoy58@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')# it find the __init__.py it consider itself as a package and try to buid this then we can import this anywhere

)