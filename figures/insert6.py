import _dictdraw, sys

d = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'time': 37, 'www': 80}
surface = _dictdraw.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
