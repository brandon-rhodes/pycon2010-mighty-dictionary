#!/usr/bin/env python
import sys
from lxml import etree
from lxml.cssselect import CSSSelector
path = sys.argv[1]
s = open(path).read()
html = etree.HTML(s)
slides = CSSSelector('div.slide')(html)
for slide in slides:
    children = list(slide)
    maybe_title = children[0]
    if maybe_title.tag == 'h1' and maybe_title.text == 'untitled':
        del children[0]
    del slide[:]
    table = etree.SubElement(slide, 'table')
    tr = etree.SubElement(table, 'tr')
    td = etree.SubElement(tr, 'td')
    td[:] = children
result = etree.tostring(html, pretty_print=True, method="html")
open(path, 'w').write(result)
