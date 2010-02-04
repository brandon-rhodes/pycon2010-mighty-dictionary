.. include:: <s5defs.txt>

The Mighty Dictionary
=====================

:Author: Brandon Craig Rhodes
:Occasion: Python Atlanta Meetup
:Date: December 2009

The Python List
===============

.. image:: figures/average_probes.png

The Python List
===============

| Stores objects under integer indexes

.. .. image:: figures/list1.png

| ``[0]   [1]   [2]   [3]   [4]``
| ``'Jan' 'Feb' 'Mar' 'Apr' 'May'``

The Python List
===============

| Stores objects under integer indexes
| Assignment to ``[`` *n* ``]`` is quick
| Retrieval from ``[`` *n* ``]`` is quick

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
| in an *integer-indexed* “hash table”

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

| Try adding all of the values
| from the table we created earlier

::

 hash('Brandon')  ->  10010101000101001000111010001111
 hash('Brendon')  ->  11110100001111000000101010100011
 hash('Brandoni') ->  10101011000110000101110111111001
 hash(3.141)      ->  11011110100100110100001110101100
 hash(3.1415)     ->  01101010101011010000100100000010
 hash((2, 7, 0))  ->  11101100010001110111111111111010

A Question of Space
===================

| What happened?

.. class:: incremental

| The dictionary *resized* its internal hash table
| from 8 entries (3 bits) to 32 entries (5 bits).

A Question of Space
===================

| The rules:

.. class:: incremental

| When dictionary exceeds 5 elements, size ×4
| When dictionary exceeds ⅔ full, size ×4
| When len > 50k entries, factor is ×2

A Question of Space
===================

| Q: Why allow so much extra space?

.. class:: incremental

| A: To make gambling safer.

The Gamble
==========

| The dictionary is based on a gamble.

.. class:: incremental

| The above example worked so well
| because the last three digits of the hashes
| *happened* to be distinct

.. class:: incremental

| What if they were not?

The Gamble
==========

| What if we try adding these keys to a dict?

| ``'The' 'sassy' 'Dane' 'pranced' 'showily'``

.. class:: incremental

| When a key arrives whose slot is already taken,
| the dictionary has experienced a *collision*

Stupid Dictionary Trick #1
==========================

>>> from timeit import timeit
>>> d = {}
>>> for i in range(0, 681*1024, 1024):
...     d[i] = None
>>> timeit('d[0]', 'd=%r' % d)
>>> timeit('d[680*1024]', 'd=%r' % d)

Stupid Dictionary Trick #2
==========================

x>>> class Seven(object):
x...     def __hash__(self): return 7
x>>> sevens = [ Seven() for i in range(681) ]
x>>> d = dict([ (seven, None) for seven in sevens ])
x>>> timeit('d[0]', 'd=%r' % d)
x>>> timeit('d[680*1024]', 'd=%r' % d)


Collisions
==========

| Only the first key with a given hash value
| gets to live in that slot

.. class:: incremental

| Every subsequent key gets placed in another slot

.. class:: incremental

| When you look up one of the later keys,
| the dictionary has to look through every
| previous key involved in the collision
| before it finds the one you want

Collisions
==========

| When a hash table is given *more*
| space in which to hold *n* items,

.. class:: incremental

| collisions are *fewer,*

.. class:: incremental

| inserts happen *faster,*

.. class:: incremental

| and lookups cost *less*.

The Gamble
==========

| So *the gamble* is that by taking extra room
| the dictionary will provide you with nearly
| instantaneous results.

Iteration
=========

| When you iterate over a dictionary,
| it steps in order through its hash table

Iteration
=========

| **Consequence #1.** Triggering a dictionary resize
| can change the order of existing elements

 >>> d = {'Double': 1, 'double': 2, 'toil': 3, 'and': 4, 'trouble': 5}
 >>> d.keys()
 ['toil', 'Double', 'and', 'trouble', 'double']
 >>> d['fire'] = 6
 >>> d.keys()
 ['and', 'fire', 'Double', 'double', 'toil', 'trouble']

Iteration
=========

| **Consequence #2.** The dictionary could lose its place
| an add or remove caused a resize during iteration, so it
| refuses the change with a ``RuntimeError``

 >>> d = {'Double': 1, 'double': 2, 'toil': 3, 'and': 4, 'trouble': 5}
 >>> for key in d:
 ...     d['fire'] = 6
 ... 
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
 RuntimeError: dictionary changed size during iteration

Iteration
=========

| **Consequence #3.** Because collisions move keys
| away from their natural hash values, key order
| is sensitive to dictionary history

 >>> d = {'Double': 1, 'double': 2, 'toil': 3, 'and': 4, 'trouble': 5}
 >>> d.keys()
 ['toil', 'Double', 'and', 'trouble', 'double']
 >>> e = {'Double': 1, 'double': 2, 'and': 4, 'toil': 3, 'trouble': 5}
 >>> e.keys()
 ['and', 'Double', 'trouble', 'toil', 'double']
 >>> d == e
 True

Iteration
=========

| **Consequence #4.** If a dictionary has
| been recently resized, its key order will
| have been reordered even if it is now equal

 >>> d = {'Double': 1, 'double': 2, 'toil': 3, 'and': 4, 'trouble': 5}
 >>> e = dict(d)
 >>> e['fire'] = 6
 >>> del e['fire']
 >>> d.keys()
 ['toil', 'Double', 'and', 'trouble', 'double']
 >>> e.keys()
 ['and', 'Double', 'double', 'toil', 'trouble']

Iteration
=========

| *Ergo:* a dictionary cannot guarantee the order
| in which you encounter its keys when iterating

Small dictionaries
==================

| If you keep thousands of small dictionaries,
| the wasted space can become significant

Small dictionaries
==================

| Instead, try using a tuple with index constants
| or, in Python 2.6, a namedtuple

::

 x>>> mytuple = ('Brandon', 35)
 x>>> print mytuple[NAME], 'is', mytuple[AGE]
 Brandon is 35

Objects and their dicts
=======================

| Normal objects have a ``__dict__`` dictionary
| in which their instance attributes are stored

.. class:: incremental

| To avoid the overhead of using a dictionary,
| you can specify ``__slots__`` for your class

Hashing your own classes
========================

| Normally, each instance of a user class
| is given a unique hash value, so that no
| two instances will look like the same key

::

 >>> class C(object): pass
 ... 
 >>> c1 = C()
 >>> c2 = C()
 >>> d = {c1: 1, c2: 2}

Hashing your own classes
========================

| But what if your class instances represent *values*
| that could be equal to one another?

.. class:: incremental

| Then equal values will deserve
| to be treated as the same key!

Hashing your own classes
========================

| Think of the two steps
| that a dictionary must take
| with each object offered as a key

Hashing your own classes
========================

| **First,** give your class a ``__hash__()`` method
| that returns a reasonable integer hash

.. class:: incremental

| **Second,** give your class an ``__eq__()`` method
| with which the dictionary

Hashing your own classes
========================

::

 class Point(object):
     def __init__(self, x, y):
         self.x, self.y = x, y

     def __eq__(self, p):
         return self.x == p.x and self.y == p.y

     def __hash__(self):
         return hash(self.x) ^ hash(self.y)

The End
=======

Other material
==============

When does it contract?

How much time does malloc take?  Both on going bigger and smaller!

How much time does it take to look up collided objects?

Measure wasted space!
 - Normally
 - When it contracts to very small


import my_inspect
d = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6}
my_inspect.display_dictionary(d)

- make steps of dictionary lookup clearer at beginning (HASH then COMPARE)
- at end, show how to repackage dictionary (how?)
- mention not to do the __hash__/__eq__ trick with mutable objects
- talk about how setdefault() does only one lookup
- show how space is used (and wasted) for several ranges of dict size
- why dummy keys? because you could remove something from the middle of
  a collision search sequence!

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
