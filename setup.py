from setuptools import setup, find_packages
from os import path

pkg_name = 'workflow_sensory-stimulation'

root_directory = path.abspath(path.dirname(__file__))

long_description = """"
# Pipeline for sensory-stimulation
Build sensory-stimulation pipeline using the DataJoint elements
+ [element-lab](https://github.com/datajoint/element-lab)
+ [element-animal](https://github.com/datajoint/element-animal)
+ [element-session](https://github.com/datajoint/element-session)
+ [element-sensory-stimulation](https://github.com/datajoint/element-sensory-stimulation)
"""

with open(path.join(root_directory, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

with open(path.join(root_directory, pkg_name, 'version.py')) as f:
    exec(f.read())

setup(
    name='workflow-sensory-stimulation',
    version=__version__,
    description="Sensory stimulation pipeline using the DataJoint elements",
    long_description=long_description,
    author='DataJoint',
    author_email='info@datajoint.com',
    license='MIT',
    url='https://github.com/datajoint/workflow-sensory-stimulation',
    keywords='neuroscience datajoint sensory stimulation',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
)
