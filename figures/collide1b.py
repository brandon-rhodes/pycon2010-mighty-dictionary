import _dictdraw, sys

d = {'smtp': 21}
surface = _dictdraw.draw_dictionary(d, [4])
surface.write_to_png(sys.argv[1])
