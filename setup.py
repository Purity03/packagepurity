from setuptools import setup, find_packages

setup(
    name='packagepurity',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Purity03/packagepurity.git',
    author='Purity Molala',
    author_email='molalapurity22@gmail.com'
)
