#!/usr/bin/python3
"""markdown2html
This module receives two arguments: The input markdown (.md) and the output html (.html).
"""
import sys
import os

def markdown2html(md, html):
    if not os.path.isfile(md):
        print("Missing " + md, file=sys.stderr)
        return 1
        
def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        return 1
    md = sys.argv[1]
    html = sys.argv[2]
    return markdown2html(md, html)

if __name__ == "__main__":
    exit(main())
