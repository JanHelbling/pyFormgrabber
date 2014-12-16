#!/usr/bin/python3

from distutils.core import setup

setup(name='pyFormgrabber',
	version='0.1',
	description='Grab HTML-Forms',
	author='Jan Helbling',
	author_email='jan.helbling@gmail.com',
	url='http://www.jan-helbling.ch/~jhelbling/linux.py?gpl3-opensource-library=pyFormgrabber-grab-html-forms-in-python',
	package_dir = {'pyFormgrabber' : 'lib'},
	packages=['pyFormgrabber'],
)

print("On ubuntu you need to add /usr/ (local) /lib/python3.4/site-packages/ to your PYTHONPATH environmentvariable")
