#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import cairo, sys
import my_inspect

WIDTH, HEIGHT = 720, 480

from contextlib import contextmanager

def bits(n, width=None):
    s = bin(n)[2:]  # '0b...' without the '0b'
    if width:
        s = '0' * (width - len(s)) + s
    return s

@contextmanager
def save(cr):
    cr.save()
    p = cr.get_current_point()
    yield
    cr.restore()
    cr.move_to(*p)

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
cr = cairo.Context(surface)

pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(1, 0.7, 0, 0, 1) # First stop, 100% opacity
pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1) # Last stop, 100% opacity

cr.select_font_face('Inconsolata',
                    cairo.FONT_SLANT_NORMAL,
                    cairo.FONT_WEIGHT_BOLD)

def draw_textbox(x, y, texts, rectpat):
    with save(cr):
        cr.translate(x, y)
        colors = [ a for i, a in enumerate(texts) if i%2 == 0 ]
        texts = [ a for i, a in enumerate(texts) if i%2 == 1 ]
        fulltext = 'M' * sum( len(text) for text in texts )
        tx, ty, twidth, theight = cr.text_extents(fulltext)[:4]
        charwidth = twidth / len(fulltext)
        padding = charwidth / 3

        width = twidth + 2 * padding
        height = theight + 2 * padding
        cr.rectangle(0,0, width,height)
        cr.set_source(rectpat)
        cr.fill()

        cr.move_to(padding, padding + -ty)
        for i in range(len(colors)):
            cr.set_source_rgb(*colors[i])
            cr.show_text(texts[i])

        return height

        cr.move_to(font_size / 5, slot_height / 2 + font_size / 3)
        cr.set_source_rgb(1, 0.9, 0.5)
        s = bin(i)[2:]
        s = '0' * (3 - len(s)) + s
        p = cr.get_current_point()
        cr.show_text(s + '=' + '…')
        cr.move_to(*p)
        cr.show_text('   /')


white = (1, 1, 1)
gold = (1, 0.9, 0.5)

def draw_dictionary(d, x0, y0):
    """Supply `d` a Python dictionary."""
    o = my_inspect.dictobject(d)

    with save(cr):
        if len(o) == 8:
            font_size = 32
            slot_height = 40
            gap_height = 4

        cr.set_font_size(font_size)
        charwidth = cr.text_extents('M')[2]
        width = 100 #actually compute from font size later

        cr.translate(x0, slot_height)  # upper-left corner of the dictionary

        with save(cr):
            cr.set_source_rgb(0,0,0)
            cr.translate(2,-2)
            cr.show_text('Hash')

        height = 0

        for i in range(len(o)):

            cr.translate(0, height + gap_height)

            with save(cr):
                texts = [white, bits(i, 3)]
                height = draw_textbox(0, 0, texts, pat)
                continue
                cr.rectangle(0,0, width,slot_height)
                cr.set_source(pat)
                cr.fill()

                cr.move_to(font_size / 5, slot_height / 2 + font_size / 3)
                cr.set_source_rgb
                p = cr.get_current_point()
                print cr.text_extents(s + '=')
                cr.show_text(s + '=' + '…')
                cr.move_to(*p)
                cr.show_text('   /')
            #try:
            #    cr.show_text(' ' + k)
            #except ValueError:
            #    cr.show_text(' ' + k)

                #try:
                #    v = o.ma_table[i].me_key
                #except ValueError:
                #    v = 'NULL'
                
                #cr.show_text(' ' + v)

#

cr.rectangle(0,0, WIDTH,HEIGHT)
cr.set_source_rgb(1,1,1)
cr.fill()
draw_dictionary({}, 100, 20)

surface.write_to_png(sys.argv[1])
