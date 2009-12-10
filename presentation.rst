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

 >>> hash('PyCon or Bust')
 2091597697

.. class:: incremental

::

 >>> bin(2091597697)
 '0b1111100101010110011111110000001'

A: Hash functions
=================

``hash('Brandon')  ->  10010101000101001000111010001111``

.. class:: incremental

``hash('Brendon')  ->  11110100001111000000101010100011``

A: Hash functions
=================

``hash('Brandon')  ->  .00....1..0.0...1....1....0.11..``

``hash('Brendon')  ->  .11....0..1.1...0....0....1.00..``

| Notice how a one-letter difference
| gets scattered across the hash digits!

A: Hash functions
=================

``hash('Brandon')  ->  10010101000101001000111010001111``

``hash('Brendon')  ->  11110100001111000000101010100011``

.. class:: incremental

``hash('Brandoni') ->  10101011000110000101110111111001``

.. class:: incremental

``hash(3.141)      ->  11011110100100110100001110101100``

.. class:: incremental

``hash(3.1415)     ->  01101010101011010000100100000010``

A: Hash functions
=================

``hash('Brandon')  ->  10010101000101001000111010001111``

``hash('Brendon')  ->  11110100001111000000101010100011``

``hash('Brandoni') ->  10101011000110000101110111111001``

``hash(3.141)      ->  1.01.1....01001..1..0.1.1.1.110.``

``hash(3.1415)     ->  0.10.0....10110..0..1.0.0.0.001.``

A: Hash functions
=================

``hash('Brandon')  ->  10010101000101001000111010001111``

``hash('Brendon')  ->  11110100001111000000101010100011``

``hash('Brandoni') ->  10101011000110000101110111111001``

``hash(3.141)      ->  11011110100100110100001110101100``

``hash(3.1415)     ->  01101010101011010000100100000010``

.. class:: incremental

``hash((2, 7, 0))  ->  11101100010001110111111111111010``

A dictionary in action
======================

| Behind a new, empty dictionary
| is a list with eight slots

.. class:: incremental

| Why eight?

.. class:: incremental

| Because if you grab the last **3 digits**
| off the end of a hash you get **8 combinations**

A dictionary in action
======================

Try adding all of the values
from the table we created earlier::

 hash('Brandon')  ->  10010101000101001000111010001111
 hash('Brendon')  ->  11110100001111000000101010100011
 hash('Brandoni') ->  10101011000110000101110111111001
 hash(3.141)      ->  11011110100100110100001110101100
 hash(3.1415)     ->  01101010101011010000100100000010
 hash((2, 7, 0))  ->  11101100010001110111111111111010

Further
=======

When does it expand?
When does it contract?


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
