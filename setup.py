from setuptools import setup
from setuptools import find_packages

setup(
   name='useful_scripts',
   version='1.0',
   description='Some useful scripts',
   author='jwb4335',
   packages = find_packages(
        where = 'useful_scripts'
   ),
   py_modules = ['to_tex','winsor','to_excel','stacked_bar']
)
