Introduction
============

Thank you for your help in building an annotated music corpus. Harmonic
analysis is a notoriously complex task, as of now very difficult to
teach to a computer. Therefore, we need to rely on a handannotated
databasis when analyzing the development of tonal harmony over the last
five centuries with the quantitative methods. With this goal in mind, we
have devised an annotation standard for writing harmonic analyses in a
machine-readable format. This document will help you learn how to use
this standard.

The annotation process consists in adding Roman numerals to a digital
music score. In this context, we will call them 'symbols', 'chord
symbols', 'expressions' or 'annotations'. The chord analyses are added
via the chord symbol function in the open source notation software
`MuseScore
2.3.2 <https://musescore.org/en/download#Older-and-unsupported-versions>`__.

.. note::

   Note that Musescore 3 is available but that we are still working with
   the old version. The link brings you to "Older and unsupported
   versions", please download MuseScore 2.3.2 for your operation system
   there. You can have MuseScore 2 and 3 installed next to each other but
   this requires extra attention because MS3 cannot save files in MS2
   format. At some point in 2019 we will stop using MS2.

Depending on the
source of the notation file that you receive for annotation, it might be
advisable to have a scan of the *Urtext* opened in the background for
tacit correction of the score. At least the bar numbers have to be 100%
correct. Please make sure, that upbeat measures are counted by MuseScore
as measure 0.

For the computer assisted evaluation of your data, a number of things
are important:

-  Chord symbols (i.e. Roman numerals) have to be attached to the
   moments in the score where the respective harmony begins. They are
   understood to be valid until the next symbol is written. That is to
   say, identical symbols are never repeated consecutively.
-  The symbols have to be linked to the upper system of the score, even
   if it contains only rests. Every symbol has to be attached to the
   precise position where the harmony occurs. N.B.: Symbols are stored
   with the original position, even if you move them by hand!
-  If a symbol starts with a note name, Musescore will save it
   differently which annotators have to avoid by putting a dot in front
   of the note name. For example: ``I6``, ``ii7``, ``V65`` etc. can be
   written without a starting dot but ``.bVI`` and ``.Ger6`` (German
   sixth chord) need one, as does the initial indication of the main key
   such as ``.Eb.I.`` (BTW, the one and only actual pitch name needed
   and allowed in every piece, see
   ```{Indication of key.}`` <#indication-of-key>`__).
-  Arabic numbers indicating `inversions <#roman-numerals>`__ or
   `suspensions <#suspensions-and-retardations>`__ always appear in
   descending order (e.g. ``65`` or ``9#74``).
-  The information about a harmony has to be expressed in a fixed order
   (syntax). This `syntax <#the-syntax>`__ can be proofread by using the
   script HarmonyAnnotationChecker.jl
-  Major keys are indicated by uppercase, minor keys by lowercase
   letters.

However, as we are slowly moving towards automated analyses,
**consistency** is the order of the day. In other words, while different
annotators would interpret the same music differently, it is important
that the same annotator interprets the same music identically. That is
to say, once you have made a difficult decision about annotating a
certain chord progression, you have to stick to this decision every time
the progression occurs. If at one point, for the sake of consistency,
you get the idea of `copying your
annotations <#copying-several-annotations>`__ when music repeats, make
sure that you are dealing with an exact repetition and check the
annotations after copying.