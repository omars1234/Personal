## setup.py is resposible of bulidig my ML application as a package 
## so these packages can be install and use in my project


from setuptools import find_packages,setup
from typing import List


HYPTHEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
        This fucntion will return the lists of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:                                    ## or with open("requirements.txt") as file_object: 
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]    ## to remove the slash comming after each pacjake name

        if HYPTHEN_E_DOT in requirements:                                   ## to remove the HYPTHEN form the when loading packages form requirements.txt
           requirements.remove(HYPTHEN_E_DOT)

            
    return requirements        



setup(
name="Ml_Project",
version="0.0.1",
author="Omar",
author_email="omars.soub@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")## will create fucntion called get_requirements

)