from setuptools import setup, find_packages

setup(
    name='dictum_proto',
    version='0.1',
    packages=find_packages(include=["dictum_proto", "dictum_proto.*"]),
    install_requires=[
        'grpcio~=1.50.0',
        'grpcio-tools~=1.50.0'
    ],
)
