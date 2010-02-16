import insert1, sys

d = {'ftp': 21, 'ssh': 22}
surface = insert1.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
