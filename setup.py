from setuptools import find_packages, setup

with open('requirements.txt') as f:
        required = f.read().splitlines()

setup(name='growatt',
      packages=find_packages(include=['growatt']),
      version='0.1.0',
      description='Python Library for Growatt SPF5000ES',
      author='Greg Giannoni',
      install_requires=required,
      entry_points = {
              'console_scripts': ['growatt=growatt:command_line'],
          })

