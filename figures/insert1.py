#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from math import ceil
import cairo, sys
import my_inspect

WIDTH, HEIGHT = 720, 480

from contextlib import contextmanager

def bits(n):
    s = bin(n)[2:]  # '0b...' without the '0b'
    s = '0' * (32 - len(s)) + s
    return unicode(s)

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

def draw_textbox(texts, rectcolor):

    with save(cr):
        colors = [ a for i, a in enumerate(texts) if i%2 == 0 ]
        texts = [ a for i, a in enumerate(texts) if i%2 == 1 ]

        x, y = cr.get_current_point()
        cr.translate(x, y)

        extents = cr.text_extents('M' * len(''.join(texts)))
        ty = ceil(extents[1])
        twidth = ceil(extents[2])
        theight = ceil(extents[3])

        padding = ceil(theight / 3)

        width = twidth + 2 * padding
        height = theight + 2 * padding
        cr.rectangle(0,0, width,height)
        cr.set_source_rgb(*rectcolor)
        cr.fill()

        cr.move_to(padding, padding + -ceil(ty))
        for i in range(len(colors)):
            cr.set_source_rgb(*colors[i])
            if texts[i] == '/':  # special code for not-equals
                with save(cr):   # so the '/' will display atop the '='
                    cr.show_text('=')
            cr.show_text(texts[i])

    cr.rel_move_to(width, 0)
    return height

#

white = (1, 1, 1)
red = (0.7, 0, 0)
green = (0, 0.7, 0)
gold = (1, 0.9, 0.5)
gray = (0.5, 0.5, 0.5)
lightgray = (0.8, 0.8, 0.8)

def draw_dictionary(d, x0, y0):
    """Supply `d` a Python dictionary."""
    o = my_inspect.dictobject(d)

    with save(cr):
        if len(o) == 8:
            sigbits = 3
            hashwidth = 9 # width of the hash field
            font_size = 28
            slot_height = 40
            gap = 2
        elif len(o) == 32:
            sigbits = 5
            hashwidth = 16 # width of the hash field
            font_size = 10
            slot_height = 12
            gap = 0

        cr.set_font_size(font_size)
        charwidth = cr.text_extents(u'M')[2]
        width = 100 #actually compute from font size later

        cr.translate(x0, slot_height)  # upper-left corner of the dictionary

        with save(cr):
            cr.set_source_rgb(0,0,0)
            cr.translate(2,-2)
            cr.show_text(u'Idx    Hash')

        height = 0

        for i in range(len(o)):
            cr.rel_move_to(0, height + gap)

            with save(cr):
                entry = o.ma_table[i]

                height = draw_textbox([gold, bits(i)[:sigbits]], gray)
                cr.rel_move_to(gap, 0)

                try:
                    k = entry.me_key
                except ValueError:
                    # This is a completely empty entry.
                    draw_textbox([white, u' '], lightgray)
                    cr.rel_move_to(gap, 0)
                    draw_textbox([white, u' ' * hashwidth], lightgray)
                    cr.rel_move_to(gap, 0)
                    draw_textbox([white, u' ' * 9], lightgray)
                    cr.rel_move_to(gap, 0)
                    draw_textbox([white, u' ' * 9], lightgray)
                    continue

                if k is my_inspect.dummy:
                    draw_textbox([white, u'!'], red)
                    cr.rel_move_to(gap, 0)
                    draw_textbox([white, u' ' * hashwidth], gray)
                    cr.rel_move_to(gap, 0)
                    draw_textbox([white, u' <dummy> '], gray)
                    cr.rel_move_to(gap, 0)
                    draw_textbox([white, u' ' * 9], gray)
                    continue

                h = entry.me_hash
                v = entry.me_value

                if h & o.ma_mask == i:
                    draw_textbox([white, u'='], green)
                else:
                    draw_textbox([white, u'/'], red)
                cr.rel_move_to(gap, 0)
                bstr = bits(h)[:hashwidth - 1]
                texts = [lightgray, u'…' + bstr[:-sigbits],
                         gold, bstr[-sigbits:]]
                draw_textbox(texts, gray)
                cr.rel_move_to(gap, 0)
                draw_textbox([white, u'%9s' % repr(k)], gray)
                cr.rel_move_to(gap, 0)
                draw_textbox([white, u'%9s' % repr(v)], gray)

#

if __name__ == '__main__':
    cr.rectangle(0,0, WIDTH,HEIGHT)
    cr.set_source_rgb(1,1,1)
    cr.fill()
    d = {0: 'zero', 'Brandon': 1, 'Brendon': 2, 'brandy': 3,
         3.141: 'pi', 'nom': 9}
    draw_dictionary(d, 100, 20)
    surface.write_to_png(sys.argv[1])
