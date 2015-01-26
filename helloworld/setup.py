# coding=utf-8
import setuptools

plugin_package = "octoprint_helloworld"

def package_data_dirs(source, sub_folders):
	import os
	dirs = []

	for d in sub_folders:
		for dirname, _, files in os.walk(os.path.join(source, d)):
			dirname = os.path.relpath(dirname, source)
			for f in files:
				dirs.append(os.path.join(dirname, f))

	return dirs

def params():
	name = "OctoPrint-HelloWorld"
	version = "1.0"
	description = "A quick \"Hello World\" example plugin for OctoPrint"

	packages = [plugin_package]
	package_data = {plugin_package: package_data_dirs(plugin_package, ['static', 'templates'])}
	include_package_data = True
	zip_safe = False

	install_requires = open("requirements.txt").read().split("\n")

	entry_points = {
		"octoprint.plugin": ["helloworld = %s" % plugin_package]
	}

	return locals()

setuptools.setup(**params())