********************
Questions & Examples
********************

Although the guidelines for applying the DCML harmony standard to scores aim at
reducing contingency (i.e. the presence of several solutions) in order to
achieve high inter-annotator agreement, the standard needs to remain open enough
so that style-specific and case-to-case solutions are possible if required.

In other words: In many cases, the same harmonic passage can be annotated in
different ways. Which one the annotator chooses, depends on their interpretation
of the passage. Since different interpretations have different semantics
(meanings), we provide a collection of difficult and ambiguous cases. In every
case, we discuss the most obvious solutions and try to give convincing reasons
why we opted for a particular one. This resource is mainly targeted at
annotators for reference.

This section will be constantly extended with solved cases from our
`issue tracker <https://github.com/DCMLab/standards/issues>`_. If you come
across such a difficult case you are more than welcome to open an issue there
together with a screenshot which includes measure number, clefs, time and key
signatures, so that it can be discussed by the community and eventually added
to this collection here.

Modulation and Secondary Keys
=============================

The DCML harmony standard distinguishes between modulation (e.g. to scale degree
V: ``V.V7 I``) and temporary tonicization to a secondary key (``V7/V I/V``). For
distinction, the common-place distinctions based on the autonomy (prevalence,
cadences) of the new key come into play. In uncertain cases, take as a guidance
the key disposition represented by your modulations, which could be visualised
in a Gantt chart like so:


.. raw:: html
   :file: interactive/K309-3_gantt.html

:Gantt chart: W.A. Mozart: *Piano Sonata No. 7 in C major*, K. 309, III. Rondeau, Allegretto grazioso.
    Disposition of keys modulated to (blue) and secondary keys (red).

In other words, annotate in a way, that the keys that your annotations modulate
to would lead to a Gantt chart where the yellow bars represent the disposition
of keys as you conceive it.

Modulation
----------

Positioning a modulation
^^^^^^^^^^^^^^^^^^^^^^^^

In the guidelines it says that, generally

    "[...] the change of local key should be annotated as early as consistently possible."

However, there are situations where we can refrain from this principle. In the
following example, it looks cleaner to let the key of IV (F major) include beat
1 of m. 32, rather than letting the cadence end on a ``I.IV}``.

Secondary Keys
--------------

'Ternary' / 'Triple' dominants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the following example, notating secondary dominants of ``/VII`` in m. 154f.
is, of course, fine:

.. figure:: img/mendelssohn_op12_I_149-158.png
    :alt: Ternary key in a Mendelssohn quartet
    :target: ../_images/mendelssohn_op12_I_149-158.png

    Felix Mendelssohn-Bartholdy: *String Quartet op. 12*, I. Adagio, non troppo, mm. 149-158

However, in order to express a continued tonicization of G minor (``iii``),
annotators might want to opt for the 'ternary key' notation, in the sense that
the standard allows for secondary keys within secondary keys. In order to
express this, we would write ``viio7/V/iii V65/V/iii``.

In addition, the example contains a mistake in m. 156 where ``iii`` should be
replaced by ``i6/iii``.

Phrase Structure
================

Phrase annotations should be considered as a separate, light-weight annotation
standard which can be combined with harmony labels or used separately.

Hierarchical phrase structure?
------------------------------

At the moment, we don't use hierarchical phrase segmentations. In other words,
annotators choose exactly one hierarchical level to be expressed in the
continuous segmentation using ``{`` and ``}``. Ideally, this level is chosen such
every cadence coincides with a phrase ending (but not forcibly vice-versa).

Figured Bass
============

In music where the composer has written a figured bass, it needs to be included
in the score and in the analysis. For example:

.. figure:: img/corelli_op01n07c_1-2_figured_bass.png
    :alt: Figured bass in Corelli
    :target: ../_images/corelli_op01n07c_1-2_figured_bass.png

    Arcangelo Corelli: *Sonata da chiesa op. 1/7*, III. Allegro, mm. 1-2
