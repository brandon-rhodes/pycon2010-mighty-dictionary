import insert1, sys

d = {}
surface = insert1.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
