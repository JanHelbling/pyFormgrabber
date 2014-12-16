#!/usr/bin/python3
#    formgrabber.py - A Python-Class to grab html-forms
#
#    Copyright (C) 2014 by Jan Helbling <jan.helbling@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import re

class pyFormgrabber:
	"""Usage:
	>>> f = formgrabber(html)
	>>> f.input_data  # list of inputs
	>>> f.form_method # POST or GET
	>>> f.form_action # post to e.g. index.php""" 
	def __init__(self,html):
		self.html	=	html
		self.input_data	=	[]
		self.__grab_form()
		if self.input_data != None:
			self.__parse_form()
	
	def __grab_form(self):
		try:
			self.formdata	=	re.findall('(<form[^\a]*</form>|<FORM[^\a]*</FORM>)',self.html)[0]
		except IndexError as e:
			self.input_data	=	None
	
	def __parse_form(self):
		self.form_method	=	re.findall('(method="[a-zA-Z]*|METHOD="[a-zA-Z]*)',self.formdata)[0][8:]
		self.form_action	=	re.findall('(action="[a-zA-Z\./:-]*|ACTION="[a-zA-Z\./:-]*)',self.formdata)[0][8:]
		self.inputs		=	re.findall('(<input[^>]*|<INPUT[^>]*)',self.formdata)
		self.input_data		=	[]
		for i in self.inputs:
			tmp		=	{}
			if 'name' in i.lower():
				try:
					tmp['name'] = re.findall('(name="[a-zA-Z]+|NAME="[a-zA-Z]+)',i)[0][6:]
				except IndexError:
					tmp['name'] = 00
			else:
				tmp['name'] = ''
			if 'type' in i.lower():
				try:
					tmp['type'] = re.findall('(type="[a-zA-Z]+|TYPE="[a-zA-Z]+)',i)[0][6:]
				except IndexError:
					tmp['type'] = ''
			else:
				tmp['type'] = ''
			if 'value' in i.lower():
				try:
					tmp['value'] = re.findall('(value="[a-zA-Z]+|VALUE="[a-zA-Z]+)',i)[0][7:]
				except IndexError:
					tmp['value'] = ''
			else:
				tmp['value'] = ''
			self.input_data.append(tmp)
		
		

if __name__ == '__main__':
	import urllib.request
	from os import getenv
	proxy	=	getenv('http_proxy')
	if proxy == None:
		proxyhdl	=	urllib.request.ProxyHandler({})
	else:
		proxyhdl	=	urllib.request.ProxyHandler({'http',proxy})
	opener	=	urllib.request.build_opener(proxyhdl)
	opener.addheaders = [('User-Agent','JanHelblings formgrabber FTW!!!')]
	print('Getting html-form from http://www.utexas.edu/learn/forms/text.html')
	html = (opener.open('http://www.utexas.edu/learn/forms/text.html').read()).decode('utf-8','ignore')
	f = formgrabber(html)
	print('METHOD:',f.form_method)
	print('ACTION:',f.form_action)
	print('DATA:',end='')
	for i in f.input_data:
		print()
		print('input name:',i['name'])
		print('input type:',i['type'])
		print('input value:',i['value'])
		print()
