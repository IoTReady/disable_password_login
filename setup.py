from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in disable_password_login/__init__.py
from disable_password_login import __version__ as version

setup(
	name="disable_password_login",
	version=version,
	description="Disallow Password Login If Social Login Is Enabled",
	author="IoTReady",
	author_email="hello@iotready.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
