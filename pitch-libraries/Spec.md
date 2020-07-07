# Pitch and Interval Interface

Basic design concepts:

- abstraction over different types of intervals and pitches
- based on intervals (pitches are secondary)
- distinction between interval (with octave) and interval class (without octave)
- pitches are wrappers around intervals
  - only one pitch type
  - interval + reference point (by convention e.g. C4)
- common interface
  - operations on corresponding interval and pitch types
  - conversion functions
  - printing / parsing

The goal of this specification is to have a common set of functionality between libraries implemented in different programming languages.
It's more important to implement that functionality in an idiomatic way then to have an identical API.
This includes the technical implementation of types and interfaces as well as naming of types and functions.
An exception is the printing and parsing functionality
since the string representations of pitches and intervals should be compatible between different implementations.

## Common Interface

### Interval

The `Interval` interface represents intervals and supports generic operations on intervals. Each type of interval (MIDI, spelled, etc) has its own type, which may be a subtype of a common `Interval` type, depending on what is idiomatic in the respective language,
but every interval type should implement the following operations
in an idiomatic way.

#### Relation to Interval Classes and MIDI

`ic(i :: Interval) :: IntervalClass`
: Returns the interval class that corresponds to `i` (e.g. `ic(P2+1) => P2`).
If `Interval` is already an interval class type, returns `i`.

`intervalClassType(I :: Type) :: Type`
: Type-level function that returns the type of the interval class that corresponds to the interval Type `I`.
If `I` is already an interval class type, returns `I`.

`toMidi(i :: Interval) :: MidiInterval`
: Returns the approximate midi interval representation of `i`. (up for debate; optional)

#### Special Values

`unison(I :: Type) :: I`
: Returns a unison of type `I` (e.g. `0` for MIDI, `P1` for spelled).
The unison is the `0` element of the module.

`octave(I :: Type, [n=1 :: Int]) :: I`
: Returns the interval of an octave (upwards) for an interval type `I` (e.g. `12` for MIDI, `P8` for spelled).
Returns a unison if `I` is an interval class type.
Can take an optional number of octaves
(if not, the same result can be obtained by `n*octave(I)`)

`chromaticSemitone(I :: Type) :: I`
: Returns a chromatic semitone (upwards) of type `I` (e.g. `1` for MIDI, `A1` for spelled). (up for debate; optional)

`isStep(i :: I) :: Bool`
: Returns `true` iff the interval is considered a step. (optional)

> [name=chfin][color=green]
> The optional methods `isStep` and `chromaticSemition` could be split off from the main interface.
> For example, the Haskell implementation puts them into additional type classes `Diatonic` (containing `isStep`) and `Chromatic` (containing `chromaticSemitone`).

#### Arithmetic Operations

Intervals form a module over integers, i.e. they support addition, negation and multiplication with integers, and have a `0` elements (the unison). In addition, intervals have a direction.

`+(i1 :: Interval, i2 :: Interval) :: Interval`
: Returns the sum of two intervals.

`-(i1 :: Interval, i2 :: Interval) :: Interval`
: Returns the (directed) difference between two intervals.

`-(i :: Interval) :: Interval`
: Negates an interval (changes it's direction).

`*(i :: Interval, n :: Int) :: Interval`; `*(n :: Int, i :: Interval) :: Interval`
: Multiplies `i` by `n`.
If `n` is negative, the direction of `i` is reversed.

`direction(i :: Interval) :: {Up, Down, Neutral}`
: Returns the direction of the interval.
For interval classes, returns the direction of the smaller realization of the interval: e.g., a 5th up and a 4th down are the same interval class, but since the 4th down is the smaller realization, `direction` returns `Down` on this interval.
In ambiguous cases (e.g. the tritone in MIDI, `6`) `Neutral` is returned.
This function may be implemented as a `sign` function, depending on the language.

`abs(i :: Interval) :: Interval`
: Returns the absolute interval of `i`,
i.e. `i` if `i` is upwards or neutral,
and `-i` if `i` is downwards.

### IntervalClass

Interval classes are considered intervals, so they must implement all methods of the `Interval` interface.
In addition, they provide the following methods:

`embed(i :: IntervalClass, [oct=0]) :: Interval`
: Embeds an interval class in the Interval space, i.e. converts it to the corresponding interval type (e.g. `embed(P2) => P2+0`).
Can take an optional octave argument,
which amounts to `embed(i, oct) = oct*octave(Interval) + embed(i)`.

`intervaltype(IC :: Type) :: Type`
: Returns the interval type that corresponds to the interval class type `IC`.

### Pitch

Pitches are just wrappers around Interval Types.
If the languages type system allows, they may be implemented
as a single parametric type that contains an interval and
just changes the semantics of that interval, i.e.
`Pitch<Interval>`.
However, it must be possible to provide specialized methods
on different instantiations,
e.g. different printing methods for `Pitch<MidiInterval>` and `Pitch<SpelledInterval>`.

Representing pitches as wrapping intervals is similar to the use of vectors to describe differences between points (~ intervals) as well as points themselves (~ pitches).
Just like a point is characterized by the vector between it and the origin of the space, pitches can be characterized as the interval form some reference pitch (which is chosen by convention and in principle arbitrary).
This way, arithmetic operations only need to be specified for intervals, and operations on pitches and intervals (such as transposing a pitch or computing the interval between two pitches) can rely on the operations on intervals.

A pitch may be implemented as a generic wrapper with a single field for the wrapped interval:

`Pitch<Interval> = Pitch {i :: Interval}`

#### Conversion

`toPitch(i :: Interval) :: Pitch<Interval> = Pitch(i)`
: Creates a pitch from an interval.
Note that the interpretation of the pitch object relies on the conventional origin of the interval type.

`toInterval(p :: Pitch<Interval>) :: Interval = p.i`
: Returns the interval underlying the pitch.
Note that the semantic relationship between the pitch and the returned interval relies on the conventional origin of the respective interval type.

`pc(p :: Pitch<I>) :: Pitch<IC> = toPitch(ic(toInterval(p)))`
: Converts a pitch into the corresponding pitch class.

`embed(p :: Pitch<IC>, [oct=0]) :: Pitch<n>`
: Embeds a pitch class into the canonical octave (i.e. the octave above the origin).
Optionally, the octave can be modified by an additional argument,
subject to `embed(p, oct) = oct*octave(I) + embed(p)`.

#### Arithmetic Operations

All of these operations are irrespective of the conventional origin.

`+(p :: Pitch<I>, i :: I) :: Pitch<I> = toPitch(toInterval(p) + i)`
: Transposes `p` by `i`.

`+(i :: I, p :: Pitch<I>) :: Pitch<I> = toPitch(i + toInterval(p))`
: Transposes `p` by `i`.

`-(p :: Pitch<I>, i :: I) :: Pitch<I> = p + (-i)`.
: Transpose `p` by `-i`

`-(p1 :: Pitch<I>, p2 :: Pitch<I>) :: I = toInterval(p1) - toInterval(p2)`
: The interval from `p2` to `p1`.

For convenience / better readability:

`from(p1 :: Pitch<I>, p2 :: Pitch<I>) :: I = p1 - p2`
: Interval from `p2` to `p1`.
Like `p1 - p2` but more readable (read `p1 from p2`).

`to(p1 :: Pitch<I>, p2 :: Pitch<I>) :: I = p2 - p1`
: Interval from `p1` to `p2`.
Like `p2 - p1` but more readable (read `p1 to p2`).

## Printing and Parsing

Each pitch and interval type should support some form of printing to and parsing from a textual representation.
While printing will likely use the existing infrastructure for converting objects to strings,
parsing may have to provide separate functions for parsing to different types (an exception being Haskell's `Read` class, which can select the method based on the required return type).

The string formats for specific types are described in the respective sections.

`show(x :: X) :: String`
: Returns a string representation of the pitch or interval `x`.

`read(s :: String) :: X`
: Parses a string into type `X`.
The method may have different names for different `X`,
e.g. `readX(s)` or `X.read(s)`.

## Pitch and Interval Types

### MIDI

A representation of pitches and intervals based on the chromatic system.
Intervals are integers representing a number of semitones
(positive = upwards, negative = downwards),
`0` representing the unison.
An octave has 12 semitiones and the reference pitch is C-1,
so `C4 = C-1 + 12*5 = 60`.

Because of the relation to integers, conversion functions from an to Integers should be provided.
To disambiguate string representations,
the prefixes `i`, `ic`, `p`, and `pc` should be used,
followed by an integer (e.g. `"i-3"` for a minor third down and `"pc7"` for a `G`).

Arithmetic operations are based on integer arithmetic, interval classes return all results modulo 12.
A notable special case is the direction of `ic6`, which is `Neutral`, since the tritone interval class has the same interval size for the upwards and downwards interpretation.
`isStep` returns true for intervals up to two semitones (in either direction).
Note that this include `ic11` and `ic10`.

### Spelled Intervals and Pitches

Spelled Intervals and Pitches are based on the diatonic system
with seven steps per octave and alterations.
In contrast to other interval systems, spelled intervals have a dimensionality of 2.
Possible bases include chromatic semitones and diatonic semitones,
semitones and diatonic steps, or fifths and octaves (with fifths either representing the interval or the interval class).
The internal representation doesn't matter, but the implementation of the interface method obviously depend on the selected basis.

A very natural basis for spelled interval classes is the line of fifths, which allows intervals to be represented as a single integer (this space is 1-dimensional again) and arithmetic operations to be implemented as simple integer arithmetics.
However, other operations such as `direction` and `isStep` might be less straightforward to implement.

The `chromaticSemitone` (augmented unison, A1) is distinguished from the diatonic semitone (minor 2nd, m2).
`isStep` returns `true` for all unisons and seconds (including augmented and larger).
Similarly, the direction of the interval is based on the orientation of the *generic* interval.
Unisons have a neutral direction, though the canonical orientation is upwards (for interpreting augmented and diminished),
and some unisons may have several notations (e.g. -A1 = d1).
While intervals are not totally ordered based on this direction criterion, they are partially ordered with respect to the generic interval, i.e. the number of diatonic steps.
This order also determines the direction of spelled interval classes (i.e. a d5 is downward because -a4 is the smaller realization).

#### Notation

**Spelled intervals** are printed in a format similar to standard interval notation, consisting of
- an optional '-' indicating a downward interval
- one or more letters indicating the quality: 
  'P','M','m','a','d', where 'a' and 'd' can be used several times to indicate multiple augmentations or diminuitions;
- a digit indicating the generic interval within one octave (1-7);
- a '+' sign as a separator;
- the number of additional octaves.

For example, a double augmented ninth downwards is written as `"-aa2+1"`, while a perfect fifth upwards is written as `"P5+0"`.

While the above rules characterize the normalized string representation, parsers may be more flexible,
allowing, for example, negative octaves (`"M2-1"` is parsed as `-m7+0`) or downward unisons (`"-a1"` is parsed as `"d1"`).
The following regex may be used to recognize spelled intervals:
```regex
^(-?)(a+|d+|[MPm])([1-7])(\+|-)(\d+)$
```

**Spelled interval classes** are notated exactly like spelled intervals except for the octave part.
In their normalized form, interval classes are positive, they may be parsed from negative forms too (e.g. `"-M3"` is parsed as `"m6"`).
The following regex recognizes spelled interval classes:
```regex
^(-?)(a+|d+|[MPm])([1-7])$
```

**Spelled pitches** consist of
- the pitch letter (between 'A' and 'G');
- zero or more accidentals, using the unicode letters '♯' and '♭',
  or the ASCII letters '#' 'b' (Unicode is preferred, only one type of accidental per pitch);
- an octave number (an octave ranges from C to B).

For example, Middle C is written as `"C4"`, the D♭♭ below that as `"D♭♭3"` (or alternatively `"Dbb3"`).
A parser should accept both unicode and ascii accidentals and upper- as well as lowercase note letters.
The following regex recognizes spelled pitches 
and may be used case-insensitively:
```regex
^([A-G])(♭+|♯+|b+|#+)?(-?\d+)$
```

**Spelled pitch classes** work like spelled pitches but omit the octave number.
The following regex recognizes spelled pitch classes
and may again be used case-insensitively:
```regex
^([A-G])(♭+|♯+|b+|#+)?$
```

### Frequencies

Not implemented yet.

> [name=chfin][color=green]
> just some ideas...

#### Flat Frequencies

In some situations it might be beneficial to think about the exact frequencies of pitches.
In that case, intervals are frequency ratios and arithmetic operations work logarithmically: interval addition becomes multiplication of frequency ratios, negation becomes inversion, multiplication becomes exponentiation, etc.
Pitch classes take the modulo wrt. to the logarithm.

Note that this space is not a module over integers but a true vector space over real numbers.
This allows the representation of both just and equal temperament intervals (which are irrational).
However, it comes at the expense of not being representable as a finite base plus scalar multiplication with integers.
Practically this is not a problem if arbitrary ratios can be constructed.

Conversion from other pitch representations could be mediated by a formalization of tuning systems.

#### Pythagorean frequencies

Another option for frequency based pitches is to represent intervals as prime-factorized rational numbers.
The space is a module over integers but has infinite dimensions,
one for each prime.
Thus, while the values (and operations) are very similar to the flat frequency space, the shift in perspective changes the interpretation of the space as intervals constructed from integer ratios.

## Example Implementations

The following implementations have been made to follow a design close to this specification (especially wrt. the string representation).
They are currently part of larger libraries or applications, but should probably be factored out to become more reusable.

- [Haskell](https://github.com/DCMLab/haskell-musicology/blob/master/musicology-core/src/Musicology/Types.hs)
  - type classes for the interval interface
  - uses VectorSpace for vector operations
  - common container type `Pitch i`
- Julia: [interface](https://github.com/DCMLab/DigitalMusicology.jl/blob/master/src/Pitches.jl),
  [midi](https://github.com/DCMLab/DigitalMusicology.jl/blob/master/src/pitches/midi.jl),
  [spelled](https://github.com/DCMLab/DigitalMusicology.jl/blob/master/src/pitches/spelled.jl)
  - reuses many `Base` functions (`+`,`-`,`sign` etc.)
  - `Pitch{I}` container similar to Haskell implementation
  - string macros for quick parsing (e.g. `p"Ab4"`)
- ClojureScript: [interface](https://github.com/DCMLab/schema_annotation_app/blob/master/src/intervals/core.cljs), [spelled](https://github.com/DCMLab/schema_annotation_app/blob/master/src/intervals/spelled.cljs)
  - not complete yet (e.g. MIDI missing)
  - currently only ClojureScript, not Clojure
- Python (currently [part of the CorpusInterface](https://github.com/DCMLab/CorpusInterface/blob/master/CorpusInterface/datatypes.py))
  - Point/Vector base classes
  - default arithmetics (+, -, *, /, abs) with type checking
  - MIDI pitch (incl. channel info etc), enharmonic pitch, spellt pitch, log-frequency pitch, harmonic/pythoagorean pitch (and all the corresponding interval classes)
  - possibility to register converters, which automatically detects conversion chains (i.e. registering spelled-->MIDI and MIDI-->log-frequency will add spelled-->log-frequency, but this default behaviour can be suppressed)
  - no dedicated pitch- and interval-_class_ types; this is a boolean property instead, which is check at different points (e.g. for converters)
