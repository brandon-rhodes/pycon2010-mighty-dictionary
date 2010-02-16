import insert1, sys

d = {}
surface = insert1.draw_dictionary(d, 720, 330, 104, 30)
surface.write_to_png(sys.argv[1])
