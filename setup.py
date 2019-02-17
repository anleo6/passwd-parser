from setuptools import setup

setup(
    name='passwd-parser',
    version='0.1.0',
    packages=['passwdparser'],
    entry_points={
		'console_scripts':
		['passwd-parser = passwdparser.__main__:main']
	}
)
