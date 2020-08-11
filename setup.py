from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='findyou',
    version='1.0',
    install_requires=['webstruct',
                      'requests',
                      'flask',
                      'flask_sqlalchemy',
                      'requests',
                      'psycopg2-binary'],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
    },
    #long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
