# DCMLab/standards
Repository containing standards developed at the DCML

This repository contains the standard for harmonic annotations developed at the [Digital and Cognitive Musicology Lab](https://dcml.epfl.ch/) at [École Polytechnique Fédérale de Lausanne](https://www.epfl.ch/).

## Harmonic annotation standard

The DCML standard for harmonic annotations consists in a set of [annotation guidelines](https://github.com/DCMLab/standards/blob/master/guidelines/english.md) and a [regular expression](https://github.com/DCMLab/standards/blob/master/harmony.py). The guidelines are the reference for annotators applying the standard for the task of encoding harmonic analysis, and explain how the open-source software [MuseScore](https://musescore.org/) can be used to enter chord labels into scores so that they can be
* automatically extracted using the tools developed at the DCML, and
* split into the various encoded features using the regular expression.

### Use Cases

Version 2.0.0 has been used for all annotations commissioned by the DCML since the second half of 2018.

### Log

#### v2.0.0

* The new version does not allow `9` as `figbass` feature anymore. This means that a label such as `V9` will throw an error. Instead, this chord needs to be written either as `V7(9)` or `V7(+9)`, depending on the context.
* An additional group called `chord` has been added to the regular expression which captures the groups `numeral, figbass, changes, relativeroot` in order to separate it from the additional information about keys, pedal points and phrasing.
* This is the first published version of the annotation guidelines.

#### v1.0.0
Initial version of the regular expression to annotate harmonies, taken from https://github.com/DCMLab/ABC and used in

1. Moss FC, Neuwirth M, Harasim D, Rohrmeier M (2019) Statistical characteristics of tonal harmony: A corpus study of Beethoven’s string quartets. PLoS ONE 14(6): e0217242. [https://doi.org/10.1371/journal.pone.0217242](https://doi.org/10.1371/journal.pone.0217242)
1. Neuwirth M, Harasim D, Moss FC and Rohrmeier M (2018) The Annotated Beethoven Corpus (ABC): A Dataset of Harmonic Analyses of All Beethoven String Quartets. Front. Digit. Humanit. 5:16. doi: [https://doi.org/10.3389/fdigh.2018.00016](https://doi.org/10.3389/fdigh.2018.00016)
