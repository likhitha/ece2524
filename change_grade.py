#!/usr/bin/env python

import re 
import fileinput
from sys import stderr,stdin,argv,exit


if len(argv) !=3:
    stderr.write("Usage: "+ argv[0] + " STRING NUMBER \n")
    exit(1)

result = []
for line in stdin:
	if argv[1] in line: 
		print re.sub('[0-9].*',argv[2],line),
	else:
		print line
exit(0)
		
