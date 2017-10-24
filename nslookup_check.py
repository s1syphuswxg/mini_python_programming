# Script Name		: nslookup_check.py
# Author				: Craig Richards
# Created				: 5th January 2012
# Last Modified		:
# Version				: 1.0

# Modifications		:

# Description			: This very simple script opens the file server_list.txt and the does an nslookup for each one to check the DNS entry

import os

with open('server_list.txt') as f:				# Open the file and read each line
    for line in f.readlines():
        print('----nslookup----')
        os.system(('nslookup ' + line.strip()))	# Run the nslookup command for each server in the list
