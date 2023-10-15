#!/usr/bin/python3
import os
import sys
import re

def parse_heading(line):
    level = len(line) - len(line.lstrip('#'))
    line = line.lstrip('#').strip()
    return '<h' + str(level) + '>' + line + '</h' + str(level) + '>' + '\n'

if len(sys.argv) != 3:
    print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Checking if the file exists
if not os.path.exists(input_file):
    print('Missing ' + input_file, file=sys.stderr)
    sys.exit(1)

# Open input and output files
with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file.readlines():
        line = line.strip()
        if re.search('^#{1,6}\s', line):
            out_file.write(parse_heading(line))

# If everything is good
sys.exit(0)
