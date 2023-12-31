#!/usr/bin/python3
"""
markdown2html
This module receives two arguments: The input markdown (.md) and the output html (.html).
"""

import os
import sys
import re
import hashlib

def markdown2html(md, html):
    if not os.path.isfile(md):
        print("Missing " + md, file=sys.stderr)
        return 1

    with open(md, 'r') as f:
        markdown = f.read().split('\n')

    html_str = []
    inside_list = False
    inside_order_list = False
    inside_paragraph = False

    for line in markdown:
        if line.startswith('-'):
            if not inside_list:
                if inside_paragraph:
                    html_str.append('</p>\n')
                    inside_paragraph = False
                html_str.append('<ul>\n')
                inside_list = True
            count = line.count('-')
            text = line[count:].strip()
            text = re.sub(r'__([^__]*)__', r'<em>\1</em>', text)  # Parsing emphasis syntax
            text = re.sub(r'\*\*([^**]*)\*\*', r'<b>\1</b>', text)  # Parsing bold syntax
            html_str.append('<li>{}</li>\n'.format(text))
        elif line.startswith('*'):
            if not inside_order_list:
                if inside_paragraph:
                    html_str.append('</p>\n')
                    inside_paragraph = False
                html_str.append('<ol>\n')
                inside_order_list = True
            count = line.count('*')
            text = line[count:].strip()
            html_str.append('<li>{}</li>\n'.format(text))
        else:
            if inside_list:
                html_str.append('</ul>\n')
                inside_list = False
            if inside_order_list:
                html_str.append('</ol>\n')
                inside_order_list = False
            if line.strip() != '':
                if not inside_paragraph:
                    html_str.append('<p>\n')
                    inside_paragraph = True
                text = line.strip()
                text = re.sub(r'__([^__]*)__', r'<em>\1</em>', text)  # Parsing emphasis syntax
                text = re.sub(r'\*\*([^**]*)\*\*', r'<b>\1</b>', text)  # Parsing bold syntax
                text = re.sub(r'\[\[(.*?)\]\]', lambda x: hashlib.md5(x.group(1).encode()).hexdigest(), text)  # Convert to MD5
                text = re.sub(r'\(\((.*?)\)\)', lambda x: x.group(1).replace('c', '').replace('C', ''), text)  # Remove 'c'
                text = re.sub(r'\[\[(.*?)\]\]', lambda x: x.group(1).lower(), text)  # Convert to lowercase
                html_str.append('{}<br/>\n'.format(text))
            else:
                if inside_paragraph:
                    html_str = html_str[:-1] # Remove the last <br/>
                    html_str.append('</p>\n')
                    inside_paragraph = False

    if inside_list:
        html_str.append('</ul>\n')
    if inside_order_list:
        html_str.append('</ol>\n')
    if inside_paragraph:
        html_str = html_str[:-1]
        html_str.append('</p>\n')

    with open(html, 'w') as f:
        f.writelines(html_str)

    return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python markdown2html.py input.md output.html", file=sys.stderr)
        sys.exit(1)
    md_file = sys.argv[1]
    html_file = sys.argv[2]
    markdown2html(md_file, html_file)

