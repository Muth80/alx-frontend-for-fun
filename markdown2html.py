#!/usr/bin/python3
"""
markdown2html
This module receives two arguments: The input markdown (.md) and the output html (.html).
"""
import sys
import os
import re

def markdown2html(md, html):
    if not os.path.isfile(md):
        print("Missing " + md, file=sys.stderr)
        return 1

    with open(md, 'r') as f:
        markdown = f.readlines()

    html_str = []
    inside_list = False
    inside_order_list = False

    for line in markdown:
        if line.startswith('-'):
            if not inside_list:
                html_str.append('<ul>\n')  # Start list
                inside_list = True
            count = line.count('-')
            text = line[count:].strip()
            html_str.append('<li>{}</li>\n'.format(text))  # Add list item
        elif line.startswith('*'):
            if not inside_order_list:
                html_str.append('<ol>\n')  # Start order list
                inside_order_list = True
            count = line.count('*')
            text = line[count:].strip()
            html_str.append('<li>{}</li>\n'.format(text))  # Add list item
        else:
            if inside_list:
                html_str.append('</ul>\n')  # End list
                inside_list = False
            if inside_order_list:
                html_str.append('</ol>\n')  # End order list
                inside_order_list = False
            count = line.count('#')
            text = line[count:].strip()
            html_str.append('<h{0}>{1}</h{0}>\n'.format(count, text))

    if inside_list:  # Close list if still open
        html_str.append('</ul>\n')
    if inside_order_list:  # Close order list if still open
        html_str.append('</ol>\n')

    with open(html, 'w') as f:
        f.writelines(html_str)

    return 0
