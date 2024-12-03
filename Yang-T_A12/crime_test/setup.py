from setuptools import setup, find_packages
setup(
	name='A12_package', # Package name
	version='1.0', # Package version
	packages=find_packages(), # Automatically find modules

	install_requires=[
		'numpy>=2.0.2',  # Specific version of numpy
		'pandas>=2.2.3',  # Specific version of pandas
		'python-dateutil>=2.9.0.post0',  # Specific version of python-dateutil
		'pytz>=2024.2',  # Specific version of pytz
		'six>=1.16.0',  # Specific version of six
		'tzdata>=2024.2',  # Specific version of tzdata
	],

	description='A package for A12', # Short description
	author='Tiger Yang',
	author_email='tiger.yang@sjsu.edu',
)

