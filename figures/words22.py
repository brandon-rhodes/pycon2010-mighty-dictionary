import insert1, sys

wordfile = open('/usr/share/dict/words')
text = wordfile.read().decode('utf-8')
words = [ w for w in text.split()
          if w == w.lower() and len(w) < 6 ]

d = dict.fromkeys(words[:22])
surface = insert1.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
