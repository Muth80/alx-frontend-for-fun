#!/usr/bin/python3
import os
import sys

if len(sys.argv) != 3:
    print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Checking if the file exists
if not os.path.exists(input_file):
    print('Missing ' + input_file, file=sys.stderr)
    sys.exit(1)

# If everything is good
sys.exit(0)
