# setup.py is used to create packages, libarary can be shared by others or can be used for any other project

# these are the basic need for us to start the project 

from setuptools import find_packages, setup
from typing import List

def get_requirements():
    """ 
    This function will return list of requirements
    """
    requirement_list = []
    
    '''
    write a code to read requirement.txt and append each requirements in requirement_list variable.
    '''

    file = open('D:/Project/sensor-fault-detection/requirements.txt', 'rt')
    requirement_list = file.readlines()
    
    return requirement_list

setup(
      name='sensor',
      version='0.0.1',
      author='mayank_ghai',
      author_email='mayankatulghai@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements(),
)

# after this run # https://docs.python.org/3/library/logging.html consult the documentation for further use of the logger files in the projects to setup the requirements by using setup.py file

# or we can use pip install -r requirements.txt

# wget -O dataset  https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
# to the the dataset use this command and add it to git

