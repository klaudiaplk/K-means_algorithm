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
        'pandas>=1.2.0',
        'scikit-learn>=0.24',
        'matplotlib>=3.3.3',
        'numpy>=1.19.0',
        'kneed>=0.7.0'
    ]
)
