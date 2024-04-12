from setuptools import setup, find_packages
from setuptools.command.install_scripts import install_scripts
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from setuptools.command.build_ext import build_ext
import subprocess
import os
import glob


# From https://stackoverflow.com/questions/5932804/set-file-permissions-in-setup-py-file
# https://blog.niteo.co/setuptools-run-custom-code-in-setup-py/
def customize(command) :
	command_name = str(command.mro()[1].__name__).strip()
	original_run = command.run
	def run(self) :
		# Run the rest of the installer first
		original_run(self)
		# Create a new subprocess to run the included shell script
		print("Running " + command_name + " commands...")
		current_dir_path = os.path.dirname(os.path.realpath(__file__))
		create_service_script_path = os.path.join(current_dir_path, 'setup.sh')
		# stdout and stderr are combined in shell output
		output=subprocess.run([create_service_script_path,command_name],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout
		print(output.decode('UTF-8'))
	command.run = run
	return command

@customize
class CustomInstallCommand(install) :
	pass

@customize
class CustomDevelopCommand(develop) :
	pass

@customize
class CustomEggInfoCommand(egg_info) :
	pass

@customize
class CustomBuildExtCommand(build_ext) :
	pass



setup(name='home_publisher',
	version='1.0.0',
	url='',
	license='Apache2',
	author='Daniel Dayley',
	author_email='github@cronocide.com',
	description='An automation to update public infrastructure to represent my internal lab',
	packages=find_packages(exclude=['tests']),

	install_requires=['CloudFlare==2.19.2','configparser','requests'],
	scripts=['bin/home_publisher'],
	long_description=open('README.md').read(),
	zip_safe=True
)
