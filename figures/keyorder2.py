import _dictdraw, sys

d = { 'ircd': 6667, 'zope': 9673, 'smtp': 21,
      'dict': 2628, 'svn': 3690 }
surface = _dictdraw.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
