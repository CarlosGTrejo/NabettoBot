from setuptools import setup, find_packages

setup(
    name='Nabetto',
    version='0.1.0',
    packages=find_packages('nabetto'),
    entry_points={
        'console_scripts': [
            'nabetto=nabetto.__main__:main'
        ]
    }
)