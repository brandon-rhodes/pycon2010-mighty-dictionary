import _dictdraw, sys

d = {'ftp': 21, 'ssh': 22, 'smtp': 25}
surface = _dictdraw.draw_dictionary(d, [7])
surface.write_to_png(sys.argv[1])
