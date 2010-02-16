import _dictdraw, sys

d = {'smtp': 21, 'dict': 2628, 'svn': 3690, 'ircd': 6667, 'zope': 9673}
del d['smtp']
surface = _dictdraw.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
