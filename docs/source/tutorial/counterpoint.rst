*********************
Contrapuntal patterns
*********************

Introduction
------------

Roman numerals describe first and foremost vertical structure but we have already seen examples how the chord
alteration syntax with parentheses ``()`` can be used to describe horizontal, melodic, contrapuntal phenomena
such as a fourth suspension or a ``7-6`` bass figure. Here we are going to have a look how the DCML harmonic
annotation standard can be used to systematically express contrapuntal phenomena such as sequences. Before we dive in,
let's quickly brush up the basic principle.

.. admonition:: Annotate ``corelli_op01n01a.mscx`` from m. 9 until the end, leaving out the part in between for now.
  :class: toggle

  .. figure:: img/counterpoint_01_corelli.svg
      :alt: First movement of Corelli op. 1/1, mm. 9-14, annotated
      :scale: 30 %

      First movement of Corelli op. 1/1, mm. 9-14, annotated

  .. admonition:: Analytical decisions
    :class: caution

    There are a couple of details that different annotators might solve differently. It goes without saying that
    the literal repetition in the music requires the exact same annotation.

    * The beginning of each phrase includes the upbeat: ``{`` is on beat 1.5 ("one and") rather than on 2
      (repetition accordingly).
    * If taken literally, the figures ``6-5`` in m. 10 translate to ``V6/V viio/V`` or, more plausibly,
      ``V6/V V65/V`` since we can assume notes to keep sounding. This has been condensed into one label here.
    * Several solutions are possible for beat 4.5 of m. 10 depending on what you consider to be a proper or a
      passing chord. According to what you would write in a harmonic reduction other solutions could be
      ``I6 vi``, ``I6 V7 vi``, or ``I6 IV V7 vi``.
    * The resolution of the fourth suspension in m. 11 was put on beat 2.5 reflecting both the harmonic rhythm
      and the placement of the figure ``3``, and interpreting the belated ``E`` in Vl. 2 as rhythmic ornament.

Once more, the chain of ``7-6`` suspensions is expressed in the Fauxbourdon ``IV6 iii6 ii6`` with ``(2)``
suspensions of the root. The principal means for expressing contrapuntal similarity is an analogously similar
syntactical pattern in the annotations. Let's look at a more tricky example now.

A more difficult case
=====================

Let's now finalize ``corelli_op01n01a.mscx`` by going through three different solutions for mm. 7 & 8. The goal is
once more to capture the ``2-3`` dissonance chain. Another question we need to answer in parallel is where we
change the local key to ``vi``.

Solution 1
----------

.. figure:: img/counterpoint_02a_corelli.svg
    :alt: First movement of Corelli op. 1/1, mm. 6-9, annotated
    :scale: 30 %

    First movement of Corelli op. 1/1, mm. 6-9, possible solution

This version uses the earliest possible moment to change the local key to ``vi`` and then translates the figured bass
mechanically. The annotation as ``iv65 iio6 IIIM65 i6 ii%65`` is technically correct and meets the criterion that the
contrapuntal pattern should be reflected in a syntactical pattern; although it does so in a rather opaque manner
(through the root pattern -2 +1 -2 + 1 steps and alternating inversions). However,

* the ``2-3`` suspensions are implicit in this annotation but could have been made explicit through the ``()``
  syntax, which is part of its purpose;
* the first chord of m. 8 can be viewed as part of the cadential pattern in the sense that it could be viewed as
  a cadential six-four chord where the fourth is suspended by a fifth.

Let as look at the second solution which tries to address the second of the two points.

Solution 2
----------

.. figure:: img/counterpoint_02b_corelli.svg
    :alt: First movement of Corelli op. 1/1, mm. 6-9, annotated
    :scale: 30 %

    First movement of Corelli op. 1/1, mm. 6-9, possible solution

In the DCML harmony annotation standard, the cadential six-four is usually written as the suspension chord ``V(64)``,
distinguishing it from the passing ``i64`` or ``I64``. But how would we express a suspension of the fourth which
itself is a suspension? Remember that ``V(64)`` means that ``5`` and ``3`` are not present. What about ``V(+6)``?
Well, doesn't really capture the fact that the fifth is dissonant, does it? So, ``V(65)``? Similar, maybe reach for
a lifehack (in German "trick 17") and use the special symbol ``v`` (the opposite of ``^``) to display the direction of
chord tone replacement, ``V(6v5)``? Yes, that one comes closest but then we have the problem of ``V`` supposing a
major third (``C#``), when the thorough bass actually does not mention it. ``v(6v5)`` or even ``V(6v5-3)`` would fix
that but it is quite tangible that we have manoeuvred us into a corner here. So for the sake of legibility,
let's call this a tonic where the root ``D`` is replaced by the upper *and* the lower neighbour, namely by the
``C`` that is implied by the bass figure. Chord tone replacement from below can generally be displayed through the
mentioned ``^`` sign (e.g. ``i(^2)`` when ``2`` replaces ``3`` rather than ``1``) but this is not necessary for ``(7)``
(nor for any raised number as in ``i(#4#2)`` for replaced ``5`` and ``3``). Hopefully, this tour de force through the
various options is capable of making the slightly unwieldy solution ``i64(72)`` palatable. Compared to ``IIIM65``, it
brings with it the advantage that ``i64`` translates to the same notes as the cadential six-four and, compared to ``V``,
it expresses the resolution of the suspension over the same root, ``i6``, just with a different inversion.

The problem in this solution is, that the sequential pattern is obfuscated because of the interpretation of the last
two chords of m. 7 "as one hears it" in the old key (although the annotator acknowledged the indeterminacy of the
local key by giving the alternatives ``viio6-iio6/vi``). So let's try to fix this, shall we?

Solution 3
----------

.. figure:: img/counterpoint_02c_corelli.svg
    :alt: First movement of Corelli op. 1/1, mm. 6-9, annotated
    :scale: 30 %

    First movement of Corelli op. 1/1, mm. 6-9, possible solution

In this solution, the key change in m. 7 allows for expressing the sequence in a consistent and easy-to-read manner
while keeping the characteristic ``V7 vi`` progression before. Also note the similarity to the annotation of the
``7-6`` chain (which is, of course, the inversion of ``2-3``) at the beginning of this section: In both cases, the
main characteristic as a chain of suspensions has been explicitly expressed by annotating suspension and resolution
over an identical root, and even in the frequent case that the bass progresses in the moment of resolution.

``7-6`` suspensions versus seventh chords
=========================================

One could argue that Solution 1 is better because it shows the continuation of the sequential logic up to the
``ii%65`` chord. The argument points to a fundamental problem of the semantic difference between

* the historically older seventh in the sens of an *patiens* which "wants to" resolve downwards into the sixth over
  the same *agens* (and, thinking in modern terms, over the identical root a third or a fifth below the *agens*), and
* the "emancipated" seventh as a fourth chord tone, which "wants to" resolve downwards as well, but does so a priori
  into the consonant chord tone pertaining to a different root (preferably a fifth below).

.. admonition:: Note
  :class: caution

  Some think that the main difference between the two is the absence or presence of a fifth but the distinction does
  not hold because many ``7-6`` suspensions come as ``75-6`` suspensions.

The two resulting viewpoints are demonstrated most clearly above. Solution 1 shows that a *horizontal* ``2-3``
suspension chain (as well as its inversion ``7-6``) can be implicit in an annotation pattern that focuses on$
*verticalities*, as is most obvious, for example, in all inversions of the ``ii7 V7 I`` progression.
Solution 3, through it's use of ``()``,  by default is the more *horizontally* oriented one, and therefore it can be
more sensitive to and expressive of the voice-leading tendencies of particular tones. Leaving the annotation pattern
through the use of ``ii%65`` can be justified twofold:

* at this moment, the sequential pattern is taken over by a wide-spread cadential pattern;
* the logical continuation ``#viio64(72)`` would obfuscate the chord's pre-dominant function (the legal heir of the
  historically more accurate *antepenultima* function).

.. admonition:: Note
  :class: danger

  These subtle semantic differences are part of the reason why we need human annotators.


.. admonition:: Annotate mm. 233-252 of ``beethoven_n03_1.mscx`` taking contrapuntal patterns into account.
  :class: toggle

  .. figure:: img/counterpoint_03a_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 234-240, annotations
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 234-240, annotations

  At this point of the tutorial, this first section hopefully did not present you with any problems. There is no
  global or local key in the beginning to show we are dealing with an excerpt (in C major).

  .. figure:: img/counterpoint_03b_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 241-245, annotations after review
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 241-245, annotations after review

  In this segment you see labels in three different colours reflecting the result of a review.

  :black: labels left untouched by the reviewer;
  :red: labels removed by the reviewer;
  :green: labels inserted by the reviewer are in green.

  Please pause and ponder for a moment what the reasoning behind each of the two versions might have been and how
  they relate to yours.

  The annotator (in red) had learned their partimento well and defended their interpretation as a stereotypical
  realization of a *basso che scende legato*. The reviewer, on the other hand, wanted to highlight the continuum
  with the following Fauxbourdon (mm. 243-5). Since both are very legitimate views, they settled on integrating
  both perspectives:

  .. figure:: img/counterpoint_03c_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 241-245, annotations reflecting expert consensus
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 241-245, annotations reflecting expert consensus

  Note that an inconsistency in the annotator's version had to be fixed in the process: They had to opt for either
  [``IV(2)``, ``iii(2)``, ``ii(2)``] or [``vi2``, ``V2``, ``IVM2``], not a mix of both.

  And, for matters of completeness, here comes the rest:

  .. figure:: img/counterpoint_03d_beethoven.svg
      :alt: First movement of Beethoven's Piano Sonata no. 3, mm. 246-252, annotated
      :scale: 30 %

      First movement of Beethoven's Piano Sonata no. 3, mm. 246-252, annotated



Analytic conventions
====================

The above-mentioned decision problem arises in many cases where voice-leading phenomena are to be taken into account,
for example the "5-6 movement". In the examples we have seen so far, this has been consistently encoded in the form
``i VI6``, ``I vi6``, ``IV ii6``, ``iv iio6`` etc.
which stand firm as conventional annotation patterns. In cases where annotators find it more reflective of their
interpretation to write ``i i(6)``, ``iv iv(6)`` etc. they may, of course, do that but need to be prepared for
reviewers asking for justification.

In the previous assignment on Beethoven we have seen an example where a historically informed approach based on
contemporary partimento practice lead to a notation that used proper seventh chords (``vi2 ii6 V2 I6 IVM2 viio6``)
rather than highlighting the chain of suspensions (``ii6(42) ii6 I6(42) I6 viio6(42) viio6``). This may
be justified once more with the notoriety of the falling fifths sequence. It forms a renowned recurring musical
pattern and, vice versa, there is an analytical convention to group all its different manifestations under the
analytical pattern of "roots descending by fifths". The overarching sequence of falling seconds is, of course,
always implied, as are the suspensions as soon as seventh chords are involved. And last but not least,
as a weaker justification we can ask ourselves which of the two mentioned chord representations is closer to what
we have in mind when realizing a *basso che scende legato* on a keyboard instrument ourselves.

Another convention that often leads to questions concerns typical opening patterns such as ``i ii%2 #viio7 i`` or
``I ii2 V65 I`` because they can also be interpreted as actually describing a suspension in the bass voice, expressed
as ``i #viio7(2) #viio7 i`` or ``I V65(42) V65 I``. Although the latter two may definitely be legitimate
interpretations in some cases, we generally stick to the aforementioned convention. [Otherwise, why would we be
teaching students all inversions of ``I ii7 V7 I``? ;⚫︎) ]


**Now let's have a look at the remaining features of the DCML standard in conjunction with some special cases.**