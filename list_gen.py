#!/usr/bin/env python

"""
Used to create the id files for scanning nodes. The keyspace is 32^5 in size, or roughly 30,000,000 items.

Usage:
	./list_gen.py

The list generation will take a while, up to 2 min on some machines.

You will be prompted to enter the number of nodes you wish to run. All files will be placed 
	in ./values/[0th element].txt

"""

import itertools, string

__author__ = "GhostForce[at]mailinator.com"

def build_list():
	"""
	build_list() returns a list of all the possible configurations of the character set for ghostbin paste ids.
	"""
	print('generating list of possible paste ids. This will take up to 2 min.')
	possible = (lambda length : list(itertools.product(list('abcdefghjkmnopqrstuvwxyz23456789'),repeat=length)))(5)
	possible = [''.join(i) for i in possible]
	print('List generated and has size: %s'%(len(possible)))
	return(possible)

if __name__ == '__main__':
	items = build_list()
	chunk = raw_input('how many nodes would you like to run? ')
	num_per_list = int(float(len(items))/float(chunk))
	nestedlist = [items[start:start + num_per_list] for start in range(0, len(items), num_per_list)]

	for i in nestedlist:
		print('writing file')
		with open('./values/%s.txt'%(i[0]),'a') as f:
			for j in i:
				f.write(str(j))
				f.write('\r\n')

