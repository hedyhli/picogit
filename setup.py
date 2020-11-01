from setuptools import setup

setup(
    name = 'picogit',
    version = '0.0.1',
    packages = ['picogit'],
    entry_points = {
        'console_scripts' : [
            'picogit = picogit.cli:main'
        ]
    }
)