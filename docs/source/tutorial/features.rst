******************
Some more features
******************

In this section, we are going through ``beethoven_n03_1.mscx`` to bring the previous content all together and
to talk about some special cases:

* melodies in the bass
* bass arpeggios
* advanced use of applied chord notation
* organ and pedal points
* unisono
* augmented sixth and ninth chords

At this point of the tutorial you're already familiar with all the important principles of the DCML harmonic
annotation standard, so you're invited to challenge the suggested solutions: Try to guess the reasoning behind the
suggested solutions and check whether it is consistent throughout the examples. Where you have reasons to suggest
a better solution, you are more than welcome to
share and discuss it with us on our `issue tracker <https://github.com/DCMLab/standards/issues>`__ either by
inserting MuseScore 3 shots (``Tools -> Image Capture``) or by uploading the MuseScore file as attachment to your issue.

Melodies in the bass
====================

.. admonition:: To get into the piece, please annotate the first 13 measures after deciding on harmonic pace and phrasing for this *Allegro con brio*.
  :class: toggle

  .. figure:: img/features_01_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 1-13, annotated
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 1--13, annotated

  How did it go? There isn't an aweful lot of choice when it comes to harmonic rhythm and phrasing, is there?

  .. admonition:: Things to note
    :class: caution

    * In mm. 10 & 11 the melody in the bass causes ``I64`` tonic inversions. Please be aware that quite often, when
      the melody is in the bass, it is the next higher voice that perceptually takes over the bass function which is
      decisive for the chord inversion. Here, however, the inversions seem plausible.
    * The first label in m. 12 is actually spelled correctly, ``V(64#0)``, but displayed incorrectly. No worries.
      However, you would have all reason to be surprised why it's ``#0`` and not ``V(#764)``. For an explanation,
      please check :ref:`root_replacement` below.


Bass arpeggios
==============

.. admonition:: Let's continue, please annotate mm. 13-20.
  :class: toggle

  .. figure:: img/features_02_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 13-20, annotated
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 13--20, annotated

  So the annotator decided to express the bass arpeggios as chord inversions. This can hardly be wrong, naturally,
  but depending on the context, in similar cases one might want to express the whole as a single
  harmonic entity, e.g. as a single ``I`` in this case. If that was your solution: great!

  So what did you do to mm. 15-16? Parallel thirds are a classical case of under-determined triads, which the
  annotator reflected by notating alternatives. At first it looks as if a *fauxbourdon* was the first solution and
  step-wise descending root position triads the alternative. But the chords ``V`` and ``I`` reveal that they
  probably rather had a *regola dell'ottava* harmonization in mind---which has of course a lot of overlap with
  *fauxbourdon*. Annotation, here, actually is inventing a third voice so theoretically someone could find an
  excuse to assume a chain of suspensions here. Or someone who feels very uncomfortable with assuming could mark
  missing chord tones by writing ``viio(-5) vi(-5)...`` or ``V6(-1) IV(-1)...``.

.. admonition:: Let's take it to the medial caesura...
  :class: toggle

  .. figure:: img/features_03_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 21-26, annotated
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 21--26, annotated

  In the introduction of the section you read the word "pedal point" but this pedal here is not one that we annotate.
  Rather, it remains implicit in the chord progression.

  Please check whether you also put the phrase ending on beat 1 of m. 25 because it is a great example of how the
  phrase annotation syntax "works": The ``}`` marks the structural ending and what follows in this case
  is just surplus momentum.



Advanced use of applied chord notation
======================================

.. admonition:: Please try annotating mm. 27-42 in the key of ``V``. Below, it will become clearer why.
  :class: toggle

  .. figure:: img/features_04_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 27-42, annotated
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 27--42, annotated

  So how do you stay in the same local key but still express the equivalence of mm. 27--32 and mm. 33--38? Well, maybe
  you guessed from the heading: The "applied chord notation" ``/`` can be used to a wider extent than is maybe common.
  Note how the second system is just a copy of the first one with ``/v`` appended to all labels; up to m. 38 where
  we have reached another fifth above, ``/ii``. The resulting ``V2/V/v`` and ``V2/iv/v`` are fine because they
  fulfill this specific purpose, namely displaying the recursive borrowing of chords from other keys.

  In m. 42 you were probably wondering about some special syntax for augmented sixth chords and indeed, we have
  ``It6``, ``Ger6``, and ``Fr6`` in our repertoire.

  **Why V and not v? And why not change the local keys?**

  The answer to this legitimate question will be much clearer when looking a bit ahead, but before that, let us
  look at another feature:

Organ Points
============

Our organ point annotation uses square brackets ``[]``. Just as our phrase annotations with curly brackets ``{}``,
the completeness of opening and closing brackets is a constant source of errors and needs to be handled with care.

Most organ points stand on a dominant ``V[V .... V]`` or on a tonic ``I[I .... I]`` with the dots representing other
harmonies. In difference to phrase annotations, the square brackets cannot stand alone: They always need to come
in conjunction with a chord label. The opening ``[`` separates the scale degree of the pedal note from the first
harmony over the pedal note, whereas the closing ``]`` always needs to be the *last* element of a chord label
(which, in return, always precedes a potential cadence and/or phrase label). But see for yourself:

.. figure:: img/features_05_beethoven.svg
    :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 43-48, with organ point syntax
    :scale: 30 %

    First movement of Beethoven's Piano Sonata no. 3, mm. 43--48, with organ point syntax

Now looking at the bigger picture of mm. 27--48, we see more clearly what the annotator probably had in mind (and
where at least one reviewer did not object): By changing the local key in m. 27, the beginning of the second tableau
in the expected key of ``V`` has been marked and the overarching harmonic outline of the section,
``{i v ii V7 i V/V V}``, has been made visible. This analytical decision results in a soothing tonal plan, too:

.. raw:: html
   :file: interactive/features_06_beethoven.html

If you want, you can do the G major section mm. 47--68 but there is nothing new or challenging for this tutorial
to discuss, so let's have a look at what to do with


Unisono passages
================

.. admonition:: Please annotate the ending of the exposition, starting from m. 69.
  :class: toggle

  .. figure:: img/features_07_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 27-42, annotated
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 27--42, annotated


The annotator in this example followed the general guideline to infer which chords are being horizontalized. In such
cases, annotators often account for ambiguity by writing labels including two alternatives, separated by a dash
(not in this example, though).

.. comment

  Many theorists would not agree with writing cadence labels in mm. 79 and 81 because of their weak formal implications.
  However, in cadential regions we ask our annotators to mark all instances;
  independently of their formal roles, which we leave open for later analysis.
  After all, could we really say, they are **not** cadences?


Advanced use of chord tone replacement
======================================

General principles
------------------

In :ref:`a previous section <replacing_chordtones>` we introduced the syntax for replacement of the chord tones
``1``, ``3``, and ``5`` from above, namely through the combinations ``2``, ``b2``, ``v#2``
, ``4``, ``b4``, ``v#4``, ``6``, ``b6``, ``v#6`` within parentheses following the chord inversion. The digits
preceded by a sharp require the symbol ``v`` because without it they would be assumed to replace the chord tone above.
Similarly, ``^2``, ``^b2``, ``#2``, ``^4``, ``^b4``, ``#4``, ``^6``, ``^b6``, ``#6`` are used to indicate replacement
of chord tones ``3``, ``5``, and ``7`` from below.

.. admonition:: Note
  :class: caution

  Remember that the accidentals depend on the local major or (natural) minor scale.

Replacement of a chord tone's octave doubling
---------------------------------------------

The same principles apply when the chord tone in question is present, but replaced in one of the octaves above,
in form of the digits ``9``, ``11``, and ``13``. For example in the case of the so-called "Chopin chord"
which is commonly said to be a "dominant seventh chord add 13": We would express that as ``V7(13)`` to make it clear
that the chordal fifth is actually present and the suspension (at least) a ninth apart.

The same logic can be applied to added notes, for example to express a difference between ``V7(+6)``
(dissonance is a second) and ``V7(+13)``.

Ninth chords
------------

To give the most prominent example of ninth chords, dominant ninth chords are expressed as

* ``V7(9)``, ``V7(b9)``, ``V7(v#9)`` if the ninth is considered to replace an octave doubling of the root;
* ``V7(^9)``, ``V7(^b9)``, ``V7(#9)`` if the ninth is considered to replace an octave doubling of the chordal third;
* ``V7(+b9)``, ``V7(+9)``, ``V7(+#9)`` if the ninth is considered as an added note.

.. _root_replacement:

Replacement of the root by its lower neighbour
----------------------------------------------

For root replacement we needed to introduce a special case: Following the above logic, replacement of the
lowest root (``1``)  in the chord should be expressed through through ``0`` and ``#0`` (leading tone in a minor scale).
However, to not overstretch annotator's departure from inveterate annotation practices, we have it commonly
expressed as ``7`` or ``#7`` (which, logically, would express replacement of an octave doubling of the root).
Therefore ``0`` and ``7`` are equivalent in nearly all cases, the exception being root position chords, where the root
is in the bass: Here, ``0`` is required to differentiate from replacement of an octave doubling (``7``). The following
examples, hopefully, will not leave any doubts:

.. figure:: img/retardations.svg
  :alt: DCML syntax for replacement of the chordal root in the bass vs. in other voices.
  :scale: 30 %

  DCML syntax for replacement of the chordal root in the bass vs. in other voices.

.. admonition:: Read only if you subscribed to the full package
  :class: caution, toggle

  In case you wondered: ``v7``, ``vb7`` are theoretically possible but only in debatable cases where a sixth above
  the root could be considered to be a chord tone. At present, this would---if ever stretching the concept of root
  pretty far---theoretically be the case for the augmented sixth chords ``Fr6``, ``Ger6``, and ``It6``.


End of the tutorial
===================

Thank you for making it to the end! In case you managed to read and internalize all sections, congratulations, you are now in the position to
Once more the invitation to state problems you might have had in our
`issue tracker <https://github.com/DCMLab/standards/issues>`__.

Missing sections
----------------

* augmented sixth chords

