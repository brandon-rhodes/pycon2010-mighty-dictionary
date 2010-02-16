import _dictdraw, sys

d = {'smtp': 21, 'dict': 2628, 'svn': 3690, 'ircd': 6667, 'zope': 9673}
del d['smtp']
del d['svn'], d['dict'], d['zope']
surface = _dictdraw.draw_dictionary(d, [0, 1, 4, 6])
surface.write_to_png(sys.argv[1])
