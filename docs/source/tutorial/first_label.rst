***************
The first label
***************

When writing Roman numerals, we need to be always aware in which key we are
currently analysing. In the DCML standard, we define

* a piece's global key as a note name, e.g. ``Ab`` (major) or ``f#`` (minor);
* a (change of) local key as a Roman numeral.

Every change of key is succeeded by a dot and followed by a harmony label.

Global key
==========

The global key needs to be indicated in the first label. The first label should be
attached to the first note and followed by the first harmony:

.. figure:: img/first_01_beethoven01.png
  :alt: Annotated beginning of Beethoven's piano sonata no. 1
  :scale: 30 %

  Annotated beginning of Beethoven's piano sonata no. 1

Throughout the annotation standard, uppercase stands for major and lowercase
stands for minor. Depending on which mode you're annotating in, the distance of
scale degrees 3, 6, and 7 from the tonic changes:

* in major, the root distances of ``iii III vi VI vii VII`` are major intervals;
* in minor, the root distances of ``iii III vi VI vii VII`` are minor intervals.

Dorian and phrygian mode are annotated in minor, and lydian and mixolydian in major.

.. figure:: img/first_02_bwv813.png
  :alt: Annotated beginning of the Sarabande from BWV 813 in C dorian
  :scale: 35 %

  Annotated beginning of the Sarabande from BWV 813 in C dorian

.. admonition:: Write the first label into ``corelli_op01n01a.mscx``
  :class: toggle

  .. figure:: img/first_sol01_corelli.png
    :alt: First label of Corelli op. 1/1 in F major
    :scale: 30 %

    First label of Corelli op. 1/1 in F major


.. admonition:: Write the first label into ``corelli_op01n04b.mscx``
  :class: toggle

  .. figure:: img/first_sol02_corelli.png
    :alt: First label of Corelli op. 1/4 in a minor
    :scale: 30 %

    First label of Corelli op. 1/4 in a minor

.. admonition:: Write the first label into ``frescobaldi_12.16.mscx``
  :class: toggle

  .. figure:: img/first_sol03_frescobaldi.png
    :alt: First label of Frescobaldi op. 12/16 in e phrygian
    :scale: 35 %

    First label of Frescobaldi op. 12/16 in e phrygian


.. admonition:: Write the first label into ``gastoldi_baletto_a5_10.mscx``
  :class: toggle

  .. figure:: img/first_sol04_gastoldi.png
    :alt: First label of Gastoldi Baletti a 5, no. 10 in G mixolydian
    :scale: 25 %

    First label of Gastoldi Baletti a 5, no. 10 in G mixolydian


Local key
=========

Change of local key will be introduced at a later point. You may proceed with the
:doc:`next section<first_phrase>` of the tutorial.
