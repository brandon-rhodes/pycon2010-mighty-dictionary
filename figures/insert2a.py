import _dictdraw, sys

d = {'ftp': 21}
surface = _dictdraw.draw_dictionary(d, [5])
surface.write_to_png(sys.argv[1])
