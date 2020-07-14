# Things to discuss

All concrete examples that are discussed and where a decision is made should be added to a `FAQ` collection where the different options and decisions are listed for reference.

The discussed issues should be close in the course of the discussions or attributed to someone. If useful, create milestones.

## [Segmentations (organ points, phrases etc.)](https://github.com/DCMLab/standards/labels/segmentations)

### [Forbidden repetitions of identical labels and exceptions](https://github.com/DCMLab/standards/issues/3)

* Let `\\` stand alone (without repeating identical harmony)
* (instead) generally allow for repeating identical harmonies as a means of creating "Sinneinheiten" ("meaningful" chord segments)

### [Phrase interlocking, different kinds of phrase endings, cadence annotations](https://github.com/DCMLab/standards/issues/12)

* So far, there are no guidelines as to in what a phrase ending exists. What is our stance?
* Introduce `\` for phrase interlocking?
* Do we want to allow for cadence annotations? How would they relate to the phrase ending symbols? Alternative: Have cadences always as separate set of annotations.

### [The question of the organ points](https://github.com/DCMLab/standards/issues/6)

* Approval of the current 'regulation'
* Discuss concrete examples and add them to the FAQ


## [Changes](https://github.com/DCMLab/standards/labels/%27changes%27%20feature)

### [Suspensions & Retardations: Which note is being withheld?](https://github.com/DCMLab/standards/issues/4)

* New symbol for indicating that `2`, `4`, and `6` exceptionally replace the upper, not the lower neighbour?
* What about a `7` which exceptionally replaces the lower, not the upper neighbour?

### [Suspension vs passing notes](https://github.com/DCMLab/standards/issues/9)

* Is this distinction possible? Is it necessary?

### [Chord suspensions/extensions/alterations](https://github.com/DCMLab/standards/issues/10)

* Additionally to added tones (e.g. `+9`), allow for missing tones (e.g. `-5`)

### [Level of detail concerning suspensions](https://github.com/DCMLab/standards/issues/5)

* Discuss concrete examples and add them to the FAQ

## [Error Detection](https://github.com/DCMLab/standards/labels/error%20detection)

### [Downward compatibility of changes in the annotation standard / guidelines](https://github.com/DCMLab/standards/issues/8)

* Checking labels' syntax (regEx) is context-independent, checking their semantics (during post-annotation feature extraction) is not. Close issue?
* Since we convert labels into chord tones, there are new possibilities of checking against the actual notes in the score. Should that be included in the checks?

## [Analytical Edge Cases](https://github.com/DCMLab/standards/labels/analytical%20edge%20cases)

### [Chord analysis when the melody is in the bass](https://github.com/DCMLab/standards/issues/11)

* Discuss concrete examples and add them to the FAQ

