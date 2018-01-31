from setuptools import setup, find_packages

setup(
    name='perso',
    version='1.0.0',
    description='Static generator for my perso page',

    author='Lucas Escot',
    author_email='lucas.escot@ens-lyon.fr',
    licence='MIT',

    packages=find_packages(exclude=['tests']),
    install_requires=[
        'jinja2',
        'docutils',
    ],

    entry_points={
        'console_scripts': [
            'perso=perso:main',
        ],
    })
