import insert1, sys

d = {'smtp': 21, 'svn': 3690, 'dict': 2628, 'ircd': 6667, 'zope': 9673,
     'fido': 60179}
surface = insert1.draw_dictionary(d, 720, 480, 10, 20)
surface.write_to_png(sys.argv[1])
