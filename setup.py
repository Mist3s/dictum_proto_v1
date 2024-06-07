from setuptools import setup, find_packages

setup(
    name='dictum_proto',
    version='0.1',
    packages=find_packages(include=["dictum_proto", "dictum_proto.*"]),
    install_requires=[
        'grpcio~=1.64.1',
        'grpcio-tools~=1.64.1',
        'protobuf~=3.19.5'
    ],
)
