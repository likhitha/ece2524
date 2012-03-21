#!/usr/bin/env python

import re 
#import fileinput
#from sys import stderr,stdin,argv,exit

def change_grade(usr_in):
	"""Takes the student name and grade and updates the information in the file accordingly"""
	changes = ""
	for line in usr_in:
		if argv[1] in line: 
			changes += re.sub('[0-9].*',argv[2],line)
		else:
			changes += line
	return changes

if __name__=='__main__':
    from sys import stdin,stdout,stderr,argv
    if len(argv) !=3:
        stderr.write("Usage: "+ argv[0] + " STRING NUMBER \n")
        exit(1)
    (result) = change_grade(stdin)
    #print result    
    stdout.write(result)
