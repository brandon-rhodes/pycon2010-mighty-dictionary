import insert1, sys

d = {'smtp': 21, 'svn': 3690, 'dict': 2628, 'ircd': 6667, 'zope': 9673}
surface = insert1.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
