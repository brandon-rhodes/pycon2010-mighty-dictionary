import _dictdraw, sys

d = {'smtp': 21, 'dict': 2628, 'svn': 2628, 'ircd': 6667, 'zope': 9673}
surface = _dictdraw.draw_dictionary(d, [0, 1, 3])
surface.write_to_png(sys.argv[1])
