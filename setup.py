from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='###',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/<username>/<package-name>',
    author='<Your Name>',
    author_email='<Your Email>'
