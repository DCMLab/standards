****************
The first phrase
****************

Phrase annotations
==================

The DCML standard includes a rudimentary form of phrase annotations using
curly brackets ``{}``. They may stand alone or be the last character of a chord
label.

The opening bracket is put on a phrase's first event, so the previous Beethoven
example would actually start like this:

.. figure:: img/phrase_01_beethoven.svg
  :alt: Annotated beginning of Beethoven's piano sonata no. 1
  :scale: 30 %

  Beginning of Beethoven's piano sonata no. 1 with phrase annotation

The closing bracket is put on the perceived structural ending of the musical
phrase which is either followed by a small transitory 'codetta' leading up to
the next phrase or coincides with the beginning of the next phrase ('phrase
interlocking', ``}{``). At the end of the Beethoven phrase we get:

.. figure:: img/phrase_02_beethoven.svg
  :alt: First phrase of Beethoven's piano sonata no. 1 annotated

  First phrase of Beethoven's piano sonata no. 1 annotated

Note that the ``}`` sits on beat 1, the structural ending of the sentence.

Chord syntax
============

The remaining chord labels are achieved by simply typing the characters
``V65 i #viio6 i6 iio6 V(4)} V``. Note how every label fully defines the chord
type: Uppercase numerals express a major third, lowercase numerals a minor third,
and diminished triads are indicated with ``o``. Inverted triads are followed by
``6`` or ``64`` (not ``46``), leading to these combinations:

.. table:: Triads. <NA> = empty; RN = uppercase numeral; rn = lowercase numeral
  :width: 70 %
  :widths: auto
  :align: center

  +------+------+--------------+-------------------------+---------------------------------+
  | Root | Type | Inversions   | Chord type              | Examples                        |
  +======+======+==============+=========================+=================================+
  | RN   | <NA> | <NA>, 6, 64  | Major triad             | ``I``, ``V6``, ``IV64``         |
  +------+------+--------------+-------------------------+---------------------------------+
  | rn   | <NA> | <NA>, 6, 64  | Minor triad             | ``vi``, ``ii6``, ``iv64``       |
  +------+------+--------------+-------------------------+---------------------------------+
  | rn   | o    | <NA>, 6, 64  | Diminished triad        | ``viio``, ``iio6``, ``#ivo64``  |
  +------+------+--------------+-------------------------+---------------------------------+
  | RN   | \+   | <NA>, 6, 64  | Augmented triad         | ``III+``, ``III+6``, ``III+64`` |
  +------+------+--------------+-------------------------+---------------------------------+


The same principle follows for seventh chord types. Every seventh chord is distinguished by
one out of ``7``, ``65`` (not ``56``), ``43`` (not ``34``), or ``2``.

.. admonition:: Mnemonic Hook
  :class: caution

  Arabic numbers always occur in descending order.

In addition to the types based on the four triads, there are the special symbols
``%`` for half diminished chords and ``M`` for chords with a major seventh:

.. table:: Seventh chords. <NA> = empty; RN = uppercase numeral; rn = lowercase numeral
  :width: 75 %
  :widths: auto
  :align: center

  +------+------+--------------+-------------------------+-----------------------+
  | Root | Type | Inversions   | Chord type              | Examples              |
  +======+======+==============+=========================+=======================+
  | RN   | <NA> | 7, 65, 43, 2 | Dominant seventh        | ``VII7``, ``V2``      |
  +------+------+--------------+-------------------------+-----------------------+
  | rn   | <NA> | 7, 65, 43, 2 | Minor seventh           | ``vi7``, ``ii43``     |
  +------+------+--------------+-------------------------+-----------------------+
  | rn   | o    | 7, 65, 43, 2 | Diminished seventh      | ``vio7``, ``#viio2``  |
  +------+------+--------------+-------------------------+-----------------------+
  | RN   | \+   | 7, 65, 43, 2 | Augmented minor seventh | ``V+7``               |
  +------+------+--------------+-------------------------+-----------------------+
  | rn   | \%   | 7, 65, 43, 2 | Half-diminished seventh | ``vii%7``, ``#vi%43`` |
  +------+------+--------------+-------------------------+-----------------------+
  | RN   | M    | 7, 65, 43, 2 | Major seventh           | ``IVM7``, ``IIIM65``  |
  +------+------+--------------+-------------------------+-----------------------+
  | rn   | M    | 7, 65, 43, 2 | Minor major seventh     | ``iiiM7``             |
  +------+------+--------------+-------------------------+-----------------------+
  | RN   | +M   | 7, 65, 43, 2 | Augmented major seventh | ``I+M7``              |
  +------+------+--------------+-------------------------+-----------------------+


.. admonition:: Annotate ``corelli_op01n01a.mscx`` up to beat 1 of m. 3
  :class: toggle

  .. figure:: img/phrase_sol01_corelli.svg
    :alt: Beginning of Corelli op. 1/1 annotated

    Beginning of Corelli op. 1/1 annotated

  .. admonition:: Things to note
    :class: caution

    * In thorough bass music, the figured bass and historical knowledge about
      how it used to be realized needs to be included in the analysis.
    * Here, the labels' display was changed to "above" after annotating.
      Musescore handles the label placement automatically but if you're
      optically disturbed by figures and numerals mingling while you annotat,
      you may annotate under the third staff instead.
    * At the beginning of the next phrase, the harmony does not change, so the
      ``I`` is not repeated; instead, ``{`` stands alone.
    * Probably you remembered the fourth suspension ``V(4)`` from the Beethoven
      example above. More on suspensions in the next section.
    * Did you put the resolving ``V`` on beat 2.5 (with figure ``3``) or on beat
      2.75 (with ``E5`` in Vl. II)? Both solutions have a point but the harmonic
      rhythm speaks for the one shown here.


.. admonition:: Annotate ``gastoldi_baletto_a5_10.mscx`` up to beat 1 of m. 7
  :class: toggle

  .. figure:: img/phrase_sol02_gastoldi.svg
    :alt: Beginning of Gastoldi Baletti a 5, no. 10 annotated

    Beginning of Gastoldi Baletti a 5, no. 10 annotated

  .. admonition:: Things to note
    :class: caution

    * In vocal music the phrases are naturally hardwired to the lyrics.
      Otherwise, one would probably not interpret the 'Fa' in the cantus, m. 4
      as beginning a new phrase.
    * ``V/V`` probably came to you naturally? More on that later...

.. admonition:: Do a complete annotation of ``corelli_op01n04b.mscx`` after deciding on its harmonic pace
  :class: toggle

  What harmonic pace did you decide on and how did you decide? Did you listen to a recording or to a live rendition in
  your head? In case you didn't, does `listening to a recording <https://youtu.be/OKp_abVXIq8?t=54>`__ make you want to
  change your mind? In the latter case, please create an alternative set of annotations in a separate file for
  comparison.

  Once you're settled, let's take it to :doc:`the next section<detail>` to walk through some of the possibilities and
  their implications.
