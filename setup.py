from setuptools import setup, find_packages

setup(
    name='repo-introspect',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'repo-introspect=tools.repo_introspect.cli:main',
        ],
    },
    install_requires=[],
)