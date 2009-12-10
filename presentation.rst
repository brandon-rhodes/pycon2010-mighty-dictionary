.. include:: <s5defs.txt>

The Mighty Dictionary
=====================

:Author: Brandon Craig Rhodes
:Occasion: Python Atlanta Meetup
:Date: December 2009

The Python List
===============

| Stores objects under integer indexes

.. image:: figures/list1.png

The Python List
===============

| Stores objects under integer indexes
| Assignment to *n* is quick
| Retrieval from *n* is quick

How?
====

| How can Python jump *instantly*
|
| to element 0
| or element 72,
| or element 5758?

A: Computer memory is a list!
=============================

| Memory locations have sequential *addresses*
|
| 0, 1, 2, 3, ...

.. class:: incremental

| So, Python lists
| just translate each integer *index*
| into a memory *address*

What do dictionaries want?
==========================

| A: Dictionaries want to be *fast*

.. class:: incremental

| When you look up ``d[k]``
| the dictionary wants to avoid
| having to search for ``k``

.. class:: incremental

| It wants to jump *right* to the value

How?
====

| There is a mismatch here

| Memory addresses are *integers*
| But dictionary keys are *anything*

.. class:: incremental

| How can floats, strings, and tuples
| become simple integers?

A: Magic
========

A: Hash functions
=================

| A hash function turns *complicated* values
| into *simple* integers

.. class:: incremental

| So a dictionary can accept
| complicated *keys* as index values
| but turn around and secretly store them
| in an *integer-indexed* list

A: Hash functions
=================

| A slot machine displays a crazy *pattern*
| when you pull the handle:
| **apple** **orange** **pear**

.. class:: incremental

| A hash function returns a crazy *integer*
| when called with a number or string or tuple:
| **2138314276**

A: Hash functions
=================

| For a given *value*

| (like a number, string, tuple)

| the function always returns the same *hash*

A: Hash functions
=================

| Python exposes its hash routine
| rather than keep it a secret!

.. class:: incremental

::

 >>> hash('Brandon')
 -1793814897

.. class:: incremental

::

 >>> bin(-1793814897)
 '-0b1101010111010110111000101110001'

A: Hash functions
=================

``hash('Brandon')  ->  11101010111010110111000101110001``

.. class:: incremental

``hash('Brendon')  ->  10001011110000111111010101011101``

A: Hash functions
=================

``hash('Brandon')  ->  .11....0..1.1...0....0....1.00..``

``hash('Brendon')  ->  .00....1..0.0...1....1....0.11..``

| Notice how a one-letter difference
| gets scattered across the hash digits!

A: Hash functions
=================

``hash('Brandon')  ->  11101010111010110111000101110001``

``hash('Brendon')  ->  10001011110000111111010101011101``

.. class:: incremental

``hash('Brando')   ->  01111111011101000001011000100100``

.. class:: incremental

``hash(3.14)       ->  11000100011110011110000010111001``

.. class:: incremental

``hash(3.141)      ->  11001111101101010100010110010010``

A: Hash functions
=================

``hash('Brandon')  ->  11101010111010110111000101110001``

``hash('Brendon')  ->  10001011110000111111010101011101``

``hash('Brando')   ->  01111111011101000001011000100100``

``hash(3.14)       ->  ....0.0001..10..1.1..0.0..1.1.01``

``hash(3.141)      ->  ....1.1110..01..0.0..1.1..0.0.10``

A: Hash functions
=================

``hash('Brandon')  ->  11101010111010110111000101110001``

``hash('Brendon')  ->  10001011110000111111010101011101``

``hash('Brando')   ->  01111111011101000001011000100100``

``hash(3.14)       ->  11000100011110011110000010111001``

``hash(3.141)      ->  11001111101101010100010110010010``

.. class:: incremental

``hash((2, 7, 0))  ->  10010011101110001000000000000110``

Further
=======

So how does dict do it?

With the same trick as a list: contig area of memory.

But the keys are not integers!

Issue #1 how turn keys into integers

A: slot machine

a slot machine produces crazy

::

 'Brandon'  11101010111010110111000101110001
 'Brendon'  10001011110000111111010101011101
 'Brando'   01111111011101000001011000100100
 3.14       01000100011110011110000010111001
 (2, 7, 0)  10010011101110001000000000000110


so a dictionary makes a small list
and uses the last few digits of the hash as the index
so you get instant access of a list
with only the added expense of computing the hash

starts with 8 slots uses 3 bits
then expands to 32 and uses 5 bits

issue: wasted space

issue: cost of expanding the dictionary

issue: collisions

dictionaries are behind every normal object; hence __slots__

Lesson #1: Dictionaries consume space

   not *that* much space as a fraction of the objs stored
   BUT if you are storing same objects over and over it's a problem

lesson: how your own hash functions should behave

   you should twiddle lower-end bits first



The End
=======

.. raw:: html

  <script type="text/javascript">
    var objects = document.getElementsByTagName('object');
    for (var i=0; i<objects.length; i++) {
      var object = objects[i];
      var svg = object.contentDocument.getElementsByTagName('svg')[0];
      var w = svg.getAttribute('width');
      var h = svg.getAttribute('height');
      svg.removeAttribute('width');
      svg.removeAttribute('height');
      svg.setAttribute('viewBox', '0 0 ' + w + ' ' + h);
    }
  </script>
