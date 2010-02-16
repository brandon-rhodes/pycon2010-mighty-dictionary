import _dictdraw, sys

d = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'time': 37}
surface = _dictdraw.draw_dictionary(d, [2])
surface.write_to_png(sys.argv[1])
