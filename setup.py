from setuptools import setup, find_packages

setup(
    name='k_means_algorithm',
    version=1.0,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'k_means_algorithm = K_means_algorithm.main:main'
        ]
    },
    install_requires=[
         'pandas>=1.2.0'
    ]
)
