from setuptools import setup, find_packages

setup(
    name='data_analyser',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A package for calculating summary metrics and analysing Twitter data',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/MENZI-MCHUNU/EDSA_ANALYSE_PREDICT.git',
    author='Team 20 Jhb',
    author_email='menzi639@gmail.com')
