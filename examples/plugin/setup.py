from setuptools import setup, find_packages

setup(
    name='simphony_plugin_example',
    version='1.0',
    author='SimPhoNy FP7 European Project',
    description='An example plugin package',
    packages=find_packages(),
    install_requires=['simphony'],
    entry_points={
        'simphony.visualisation': ['example = simphony_example'],
        'simphony.engine': ['example_engine = simphony_example']
    })
