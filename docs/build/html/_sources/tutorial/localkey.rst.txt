**********************
Changing the local key
**********************

The syntax
==========

At the beginning of the tutorial, we saw that the first label in every piece defines a **global** major or minor key
as a note name followed by a dot and a chord label, e.g. ``C.I`` for the first tonic chord in a C major
(lydian, mixolydian) piece. What is implicit in this label is that the **local** key in the beginning is the key of
``I``. If the C major piece started, say, with a slow introduction in A minor, the first label would be ``C.vi.i``,
indicating the local key of ``vi``, thus as scale degree relative to the global key.

.. admonition:: Remember
  :class: caution

  The local key is always expressed relatively to the global key. Consequently, the distances between the local tonics
  of the keys of ``III``, ``VI``, and ``VII`` from the global tonic are major intervals in a major piece and minor
  intervals in a minor piece.

To change the local key in the course of the piece it is enough to begin the label with the corresponding scale degree
followed by a dot and a chord label relative to the new local key. The question often is when to introduce the key
change. For example, the following progressions are equivalent, the first label simply indicating the local key of
``I``:

1. ``I.I viio6 I6 viio/V V V7/V V``
2. ``I.I viio6 I6 viio/V I/V V.V7 I``
3. ``I.I viio6 I6 V.viio I V7 I``
4. ``I.I V.viio6/IV IV6 viio I V7 I``

* In (1), the local key does not change at all, expressing a mere tonicization of ``V`` in a context that continues
  in the key of ``I``.
* (3) interprets the first three chords in the 'old' key and from the moment the leading tone of ``V`` is introduced,
  it assumes a change of key.
* (4) even performs the change to the key of ``V`` two chords earlier, interpreting the 'old' tonic as the 'new'
  ``IV`` chord. Coming from the key of ``I``, one would have to justify what evokes the impression of key change at
  this early point.
* (2) expresses that the key of ``V`` is first tonized and then becomes the new local key. We would probably have a
  hard time coming up with a real-word example where this interpretation would be justified.

.. admonition:: Note
  :class: caution

  By the way, there is no real difference between notating ``viio/V V`` (1) and ``viio/V I/V`` (2), except that the
  latter facilitates reading the chord progression as ``viio I``. This is strongly encouraged in cases where the
  tonicization includes a cadence, e.g. ``I.I ii6/V V7/V I/V}``.

.. admonition:: Common mistake
  :class: danger

  Since the root of ``viio/V`` has an accidental, novice annotators are often tempted to write ``#viio/V``. This is
  incorrect because the leading tone is scale degree ``7`` in major, not ``#7``. These are all correct:

  * ``I.viio/V``
  * ``i.viio/V``
  * ``I.#viio/v``
  * ``i.#viio/v``


Try it out!
===========

.. admonition:: Get back to ``corelli_op01n01a.mscx`` and continue your annotations up to beat 1 of m. 6. Where do you change the local key?
  :class: toggle

  Here are three possibilities, is yours among them? What don't you like about the others?

  Option 1: m. 5
    .. figure:: img/localkey_01_corelli.svg
      :alt: First movement of Corelli op. 1/1, mm. 3-6, key change in m. 5
      :scale: 30 %

      First movement of Corelli op. 1/1, mm. 3-6, key change in m. 5

  This version stays in the key of ``I`` as long as possible and does not reflect the signal ``B`` in m. 4 in any way.

  Option 2: m. 4
    .. figure:: img/localkey_02_corelli.svg
      :alt: First movement of Corelli op. 1/1, mm. 3-6, key change in m. 4
      :scale: 30 %

      First movement of Corelli op. 1/1, mm. 3-6, key change in m. 4

  This version takes the signal ``B`` into account by changing the local key immediately after. It is therefore more
  expressive than the previous one.

  Option 3: m. 3
    .. figure:: img/localkey_03_corelli.svg
      :alt: First movement of Corelli op. 1/1, mm. 3-6, key change in m. 3
      :scale: 30 %

      First movement of Corelli op. 1/1, mm. 3-6, key change in m. 3

  Here, the annotator decided to interpret the whole passage in the 'new' key of ``V``, but, being uncomfortable
  with the resulting minor ``v`` in m. 4, decided to add the alternative interpretation as a borrowing from the 'old'
  key of ``I``, as in the two versions above. Note that in the new key of ``V``, the old key of ``I`` is
  located on scale degree ``IV``, hence the expression ``ii6/IV``. The primary solution ``v6`` was probably
  kept to highlight the 7-6 consecutive with its stepwise descending roots. This version certainly the least elegant
  one and probably hard to justify.

  **Taking all arguments together, Option 2 is the winner.**


Change of key or tonicization?
==============================

But what if we take the following two measures into account, mm. 6 & 7?

.. figure:: img/localkey_04_corelli.svg
  :alt: First movement of Corelli op. 1/1, mm. 5-7, annotated
  :scale: 30 %

  First movement of Corelli op. 1/1, mm. 5-7, ``IV(9)`` rather than ``IV(2)`` because ``Bb`` is present in the bass
  and therefore the placed chord tone is ``8``, not ``1``.

The music is clearly back in the key of ``I``. Doesn't that make a fourth option more likely where the local key
does not change to the key of ``V`` at all and m. 5 is simply considered as a tonicization
(``V/V iv/V ii65/V V/V I/V``)? Yes, that is possible and once again it is the annotator's decision what they want to
express. Let us look at the piece's tonal plan when sticking to this decision and annotating both the cadence to ``C``
in m. 6 and the cadence to ``d`` in m. 9 as temporary tonicizations (*applied chords*, in more general terms):

.. raw:: html
   :file: interactive/localkey_06_corelli.html

The blue line shows the local key which remains in the key of ``I`` in this version. Red lines show keys that are
tonicized using applied chords (i.e. labels including a slash), and the green lines show where the the tonic of the
temporarily tonicized key is present. Whereas this kind of interpretation might be sensible when looking at a longer
piece or, for example, the whole trio sonata, considering the short form alone calls for an analysis that reflects
the two cadences to other keys, resulting in this tonal plan:

.. raw:: html
   :file: interactive/localkey_07_corelli.html

Going forward, let's have a look at how to encode contrapuntal patterns such as sequences.




