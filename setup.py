from setuptools import setup

setup(
   name='useful_scripts',
   version='1.0',
   description='Some useful scripts',
   author='jwb4335',
   packages = find_packages(
        where = 'useful_scripts',
        include = ['to_tex','to_excel','winsor'],
    )
)
