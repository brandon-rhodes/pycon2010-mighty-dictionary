import insert1, sys

d = {}
surface = insert1.draw_dictionary(d, 512, 330, 10, 30)
surface.write_to_png(sys.argv[1])
