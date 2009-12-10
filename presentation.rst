.. include:: <s5defs.txt>

The Mighty Dictionary
=====================

:Author: Brandon Craig Rhodes
:Occasion: Python Atlanta Meetup
:Date: December 2009

The Python List
===============

* Stores objects under integer indexes

.. raw:: html

   <object data="figures/list1.svg" type="image/svg+xml"
     style="width: 50%; height: 20%;" />

.. image:: figures/list1.svg

The Python List
===============

* Stores objects under integer indexes
* Assignment to *n* is quick

A
=

* a
* b

A
=

* a
* b
* c
* a
* b
* c
* a
* b
* c

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
