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
inserting MuseScore 3 shots (``Tools -> Image Capture``) or by uploading the file as attachment to your issue.

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
    * The first label in m. 12 is actually spelled correctly, ``V(#764)``, but displayed incorrectly. No worries.

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

.. admonition:: Just for the fun of it, please try annotating mm. 27-42 in the key of ``V``.
  :class: toggle

  .. figure:: img/features_04_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 27-42, annotated
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 27--42, annotated

  So how do you stay in the same local key but still express the equivalence of mm. 27--32 and mm. 33--38? Well, maybe
  you guessed from the heading: The "applied chord notation" ``/`` can be used to a wider extent than is maybe common.
  Note how the second system is just a copy of the first one with ``/v`` appended to all labels up to m. 38, where
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
(which, in return, always precedes a potential phrase annotation). But see for yourself:

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




