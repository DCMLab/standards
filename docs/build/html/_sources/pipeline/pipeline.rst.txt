*****************************
DCML Corpus Creation Pipeline
*****************************

.. contents:: Contents
   :local:

.. _get_scores:

Collect and prepare the digital edition in the latest MuseScore format
======================================================================

Prior research
--------------

* Check which pieces make up the collection
* how they are grouped
* what naming or numbering conventions exist
* which editions there are
* if different versions of the pieces exist.
* Come up with a list (and hierarchy) of names. Here, you can already think of a good naming/numbering convention for the corpus.
* It might be good to create the list of the overarching group of works even if your corpus will contain only parts of it, for the sake of a better overview.
* Example: Going from the `list of Monteverdi's Madrigal books <http://www3.cpdl.org/wiki/index.php/Claudio_Monteverdi>`__
  to an `initial README file <https://github.com/DCMLab/corpora/blob/master/annotations/Monteverdi-Madrigals/readme.md>`__.

Look up and check existing scores
---------------------------------


* All scores available need to be checked and compared:
    * reference edition
    * completeness
    * quality & errors
    * license (later publication!)
    * file format and expected conversion losses
* Where to check
    * First: musescore.com because the scores are in the target format
    * musicalion.com (not free to publish: need to ask first)
    * choral music: CPDL
    * http://kern.ccarh.org/ lossless humdrum 2 musescore conversion needed

Typeset non-existent files
--------------------------

* pick reference edition and send commission to transcriber
* depending on the music, prices may vary between 5 and 20 CHF per page

File curation
-------------

The scores need to be corrected on the basis of a reference edition/manuscript.
We have a collaborative document with detailed
`Score correction guidelines <https://docs.google.com/document/d/1Q2svEUSsE7OCetik8An__gsEwQCYNfFJlHFMF9dRce4/edit#heading=h.8hrcm7m3udll>`__.
It also stipulates which information from the reference edition/manuscript needs to be encoded in what way.
Please send a request to be added to the document.

* Convert to MuseScore format
    * XML, CAP: can be done with MuseScore's batch converter plugin or with ``ms3 convert``
    * CAPX: Conversion to CAP or XML with DCML's Capella license
    * MUSX: Conversion to XML with private Finale copy
    * SIB: Conversion to XML with Sibelius on DCML's iMac
    * LY: no good conversion available
    * KRN: hum2xml can be used but it would be preferable to have our own converter to MuseScore
    * results need to be checked; especially markup such as slurs, arpeggios, trills etc. often get screwed
* Renaming
    * Decide on naming convention and create a map (without extensions) from old to new filenames
    * Sometimes, files need to be split at that point because they contain several movements
        * For this, you introduce section breaks separating the movements
        * After every section break, you have to re-insert the time and key signature or add it into the split file
        * Start with the last movement, select it and do `File -> Save Selection`
        * Repeat for all movements
    * Rename the files
    * Possibly add a small script that automatically renames the source files
* Use parser/checking tool and/or manual checks for consistency
    * certain bars need to be excluded from the bar count:
        * anacrusis
        * pickup measures throughout the piece
        * second voltas (i.e. second repeats)
    * irregular measure lengths need to complete each other
        * e.g. when a repeated section starts with a pickup measure, the last measure of the repeated section needs to be shorter
        * anacrusis is substracted from the last bar
    * if in the reference edition the bar count restarts in the middle of the piece (e.g. in some variation movements), you can
        * either: split the movement into individual files (not preferable if you want to keep the movement as one coherent unit)
        * or: have two versions, one working version with continuous (unambiguous) measure numbers that depart from the reference edition, and one that is provided separately, that has the original (ambiguous) measure numbering but is not used for computational purposes. The reset of the counter should not be done via "add to measure count" using a negative number, but rather via section breaks.


Create metadata
---------------

All metadata fields are automatically extracted (by our workflow script that use ``ms3 extract -D``) and represented
in the ``metadata.tsv`` file. To conveniently populate the metadata fields in the MSCX files, you can also create
the corresponding columns in the existing ``metadata.tsv`` files and use ``ms3 metadata`` to update the
Musescore files.

Populate the following default fields (if applicable):

* ``composer``
* ``movementNumer``
* ``movementTitle``
* ``source`` (URL of the adapted digital edition)
* ``workNumer``
* ``workTitle``

Add to that the following custom fields (if applicable):

* ``composed_start``, ``composed_end`` (identical values if one exact year is known)
* ``typesetter``
* ``score_integrity`` (person who made the score match the reference edition/manuscript)
* ``annotators`` (name, if several annotations or iterations, specify in parenthesis who did what)
* ``reviewers``
* ``harmony_version`` (version of the DCML harmony annotation standard used)
* ``imslp`` (URL of the work's Wiki page)
* ``musicbrainz`` (work URI)
* ``viaf`` (work URI)
* ``wikidata`` (e.g. `<http://www.wikidata.org/entity/Q2194957>`__)

.. _score_repo:

Creating a repository with unannotated MuseScore files
======================================================

.. danger:: After we start the annotation workflow, no MuseScore files should be added. removed, or renamed! The edition
   needs to be complete and the file names final.


Before starting annotating a corpus, a repo with the standard folder structure needs to be created: ::

  .
  ├── MS3
  └── pdf

The directory ``MS3`` contains the unannotated MuseScore files and ``PDF`` the print edition or manuscript which they
encode. In order to activate the annotation workflow (i.e. the automatic scripts triggered on the GitHub servers
by certain events related to annotation and review), the folder ``.github/workflows`` needs to be copied from
the `template repository <https://github.com/DCMLab/annotation_workflow_template>`__. It also contains our
standard ``.gitignore`` file which prevents temporary files from being tracked and uploaded.

Variant 1: Using the template repository
----------------------------------------

You can create the new repo directly from the `template repository <https://github.com/DCMLab/annotation_workflow_template>`__
by heading there and clicking on 'Use this template'. In this variant, every push to the ``main`` branch results
in metadata, measures and notes being extracted from all changed ``.mscx`` files. Note that renaming and deleting
files will lead to undesired effects that will have to be checked and corrected manually.

Variant 2: Starting from scratch
--------------------------------

Or you simply create the new repo with the above-mentioned folder structure and add the workflow scripts when
the scores are prepared. In this case, you will have to use the `Python library ms3 <https://pypi.org/project/ms3>`__
to extract metadata, notes, and measures manually.

Variant 3: Splitting an existing repository
-------------------------------------------

This is for the special case that the MuseScore files in question are already sitting in a subfolder of an existing
repository which is to be transferred into the new repo including the files' Git histories. This variant is a bit
more involved and requires prior installation of the `git filter-repo <https://github.com/newren/git-filter-repo>`__
command which is recommended by the Git developers for replacing ``git filter-branch``.

Setting
  As an example, we will create a new repository ``chopin_mazurkas`` (Repo B) which will include all files situated in the
  existing repository ``corpora`` (Repo A) in the subfolder ``annotations/Chopin-Mazurkas``, with the workflow scripts
  added on top.

Create the new repo B
  On GitHub, we use the `template repository <https://github.com/DCMLab/annotation_workflow_template>`__ to create
  the target repo ``chopin_mazurkas`` with the workflow files and the standard ``.gitignore``. Locally, we initialize
  an empty Git repo that will be connected upstream at a later point: ::

    mkdir chopin_mazurkas && cd chopin_mazurkas && git init

  Make sure that your Git is configured to use the name ``main`` for the default branch, which can be achieved using
  ``git config --global init.defaultBranch main``.

Clone repo A and transfer files
  We start off with a fresh clone of ``corpora``, head into it and run: ::

    git filter-repo --subdirectory-filter annotations/Chopin-Mazurkas/ --target ../chopin_mazurkas

  which will copy all files from ``annotations/Chopin-Mazurkas/`` to the freshly initialized repo
  ``chopin_mazurkas`` together with their full commit histories. If there is a README file, rename it to ``README.md``.

Connect local repo B to the remote repo B
  The local ``chopin_mazurkas`` now contains the files at the top level together with the full commit
  history (check out ``git log``). Now we can connect it to the remote and merge the workflow scripts from there: ::

    git remote add origin git@github.com:DCMLab/chopin_mazurkas.git
    git pull origin main --allow-unrelated-histories
    git push -u origin main

Clean metadata
  In case there was an older ``metadata.tsv`` it should now be automatically updated and you might have to clean it.
  This may involve naming the first two columns ``rel_paths`` and ``fnames``. For the Mazurka example,
  `this Pull Request <https://github.com/DCMLab/chopin_mazurkas/pull/1>`__ shows the metadata cleaning and update
  of the existing files from an older MuseScore and annotation standard.

Configuring and adding the new repo
===================================

* Set the standard repo settings on GitHub:

  .. figure:: img/pr_settings.png
       :alt: Repository settings on GitHub
       :scale: 50%

* Under ``Branches``, create a branch protection rule for the main branch:

  .. figure:: img/branch_protection.png
       :alt: Protecting the main branch on GitHub
       :scale: 50%

* Under ``Collaborators and teams`` give write access to the ``annotators`` team.
* Add the new repo to the corresponding meta-repositories (at least to ``all_subcorpora``, see below).
* Add the new repo to the annotation workflow (drop-down menus, OpenProject, WebHooks etc.)


.. _metarepos:

Adding the repo to one or several meta-repos
--------------------------------------------

The individual subcorpora can be embedded as submodules in meta-repositories. These meta-repos are listed in the private
`meta_repositories <https://github.com/DCMLab/meta_repositories>`__ repo. Currently, the most important ones are:

1. `dcml_corpora <https://github.com/DCMLab/dcml_corpora>`__ for published corpora
2. `all_subcorpora <https://github.com/DCMLab/all_subcorpora>`__ (private) for all published and unpublished corpora.

To add the new repo, head into the meta-repo and do ::

  git submodule add -b main https://github.com/DCMLab/chopin_mazurkas/

Just to be sure, update all submodules: ``git submodule update --remote`` and push the whole thing.


Creating work packages on OpenProject
-------------------------------------

