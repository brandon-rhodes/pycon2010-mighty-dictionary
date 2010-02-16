import _dictdraw, sys

d = {'smtp': 21, 'dict': 2628, 'svn': 3690}
surface = _dictdraw.draw_dictionary(d, [0])
surface.write_to_png(sys.argv[1])
