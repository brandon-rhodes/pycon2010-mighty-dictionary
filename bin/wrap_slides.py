#!/usr/bin/env python
import sys
from lxml import etree
from lxml.cssselect import CSSSelector
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Read the file.

path = sys.argv[1]
s = open(path).read()
html = etree.HTML(s)

# Wrap a table around each slide so that it can be vertically aligned.

slide_list = CSSSelector('div.slide')(html)
for slide in slide_list:
    children = list(slide)
    maybe_title = children[0]

    # Remove titles whose text is "untitled".
    if maybe_title.tag == 'h1' and maybe_title.text == 'untitled':
        del children[0]

    del slide[:]
    table = etree.SubElement(slide, 'table')
    tr = etree.SubElement(table, 'tr')
    td = etree.SubElement(tr, 'td')
    td[:] = children

# Syntax-highlight all <pre> sections by running them through pygment.

pre_list = CSSSelector('pre')(html)
for pre in pre_list:
    pretty = etree.HTML(highlight(pre.text, PythonLexer(), HtmlFormatter()))
    pre2 = pretty[0][0][0]  # grabs <html><body><div><pre>
    pre.text = pre2.text
    pre.tail = pre2.tail
    pre[:] = pre2[:]

style_list = CSSSelector('style')(html)
style_list[0].text += HtmlFormatter().get_style_defs(['.doctest-block',
                                                      '.literal-block'])

# Save.

result = etree.tostring(html, pretty_print=True, method="html")
open(path, 'w').write(result)
