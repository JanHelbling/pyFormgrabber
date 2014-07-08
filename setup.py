#!/usr/bin/python3

from distutils.core import setup

setup(name='formgrabber',
	version='0.1',
	description='Grab HTML-Forms',
	author='Jan Helbling',
	author_email='jan.helbling@gmail.com',
	url='http://www.jan-helbling.ch/index.php/projekte/24-python3-formgrabber-ein-html-formulargrabber',
	package_dir = {'formgrabber' : 'lib'},
	packages=['formgrabber'],
)

print("On ubuntu you need to add /usr/ (local) /lib/python3.4/site-packages/ to your PYTHONPATH environmentvariable")
