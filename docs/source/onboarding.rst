*************************
Becoming a DCML annotator
*************************

.. contents:: Contents
   :local:

Introduction
============

The Digital and Cognitive Musicology Lab (`DCML <https://www.epfl.ch/labs/dcml/>`__) at École Polytechnique Fédérale de
Lausanne (EPFL, Switzerland) is searching for contributors to its growing corpus of symbolically encoded harmonic analyses.
Remunerated on a per-measure basis, selected applicants will be producing and/or reviewing analyses in the form of typed
text annotations on MuseScore files.

This effort is longstanding and central to the lab’s overarching `Corpus Initiative <https://www.epfl.ch/labs/dcml/projects/corpus-project/>`__,
which studies the development of tonality in instrumental and vocal music of the 17th to the late 20th century.


Working as an annotator
=======================

* DCML annotators take on commissions at their desired pace and invoice their completed work when it best suits them.
* Before we commit to collaborating with a new annotator, we ask them to go through a
  trial and onboarding phase during which they can familiarize themselves with the workflow and the annotation syntax.
  The annotation tasks performed during the trial are remunerated the same way as after the trial.
* If, at the end, both sides decide to keep collaborating, the newly-trained annotator gets to self-assign tasks from a
  list of available work packages, which consist in identifying harmonic content, grouping structure, and cadence types
  of the selected pieces.
* Annotation labels must adhere to the `DCML Harmony Annotation Standard <https://dcmlab.github.io/standards`__.
  They are submitted for review using the :doc:`../workflow/workflow` which requires good knowledge and handling of
  the version control software `git <https://git-scm.com/>`__.

In order to get an idea of the whole process you may refer to the following two publications:

- Conference paper on the annotation workflow: `https://doi.org/10.5281/zenodo.5624416`__ (the essential sections are 3 through 4.4)
- Data report on the Annotated Mozart Sonatas: `http://doi.org/10.5334/tismir.63`__

Tasks
-----

Our workflow currently includes four different kinds of tasks that annotators can select from as they please.
The end result of every commission (which always involves an annotator and a reviewer) is

* an expert analysis of the harmonic structure including musical phrases and cadences,
* encoded in a machine-readable syntax,
* validated through software,
* and verified through the consensus between at least two experts.

The two available annotation tasks are:

* ``New annotations``: creating a new set of annotations from scratch;
* ``Annotation upgrade``: revisited an existing set of annotations and making it conform to the current version of the
  annotation standard (which often involves adding cadence labels).

Both tasks require that another annotator reviews your work and that, in the case of analytical divergence,
the two of you exchange arguments and adapt the annotations until consensus is reached. Taking on review tasks is
an integral part of annotating for the DCML and comes with two different tariffs, depending on which kind of annotation
tasks is being reviewed.

Remuneration and invoicing
--------------------------

The tariffs for the above-mentioned tasks are as follows:

* new annotations: 0.50 CHF per measure
* upgrading existing annotations: 0.40 CHF per measure
* reviewing new annotations created by someone else: 0.40 CHF per measure
* reviewing annotations upgraded by someone else: 0.20 CHF per measure

While the harmonic content per measure varies drastically, the tariffs tend to even out over several commissions.

The remuneration for each task is logged with the respective work package once finalized. At the time an annotator wants
to invoice one or several commissions, they can generate an automatic report and attach it to their invoice. Payments
usually arrive less than three weeks after sending an invoice.


Coordination & Tools
--------------------

The corpus initiative relies on two tools:

#. OpenProject for self-assigning available tasks, tracking the status of work packages, and generating overviews
   of the logged costs for invoicing.
#. GitHub for storing the data (scores & annotations) with its entire version history (unannotated -> annotated -> reviewed).
   The underlying version control software is git. If you have never heard of it, your training is going to be a bit
   more involved but with some continuity it can be learned rather quickly.
#. Mattermost for internal communication.


Minimum requirements
--------------------

* a Master’s degree in Music Theory (or equivalent);
* excellent knowledge of tonal harmony, contrapuntal patterns, and schemata;
* a computer running the latest version of `MuseScore <https://musescore.org/>`__;
* willingness to take on tasks on a regular basis;
* a bank account under your name that accepts money transfers from Switzerland.

Desirable criteria
------------------

- experience with MuseScore;
- experience with version control software (git).

How to get involved
===================

If you're interested in becoming an annotator and fulfill the minimum requirements above, we invite you to introduce
yourself and express your interest in an email to `dcml.annotators@epfl.ch`__. We will let you know if we have
capacities for onboarding new annotators or not. If yes, we will invite you to proceed as follows.

Before the trial phase
----------------------

Before we start the actual training, we require candidates to familiarize themselves with the following resources:

* (if not familiar with git:) any of the countless learning resources of the web
  (`this could be a starting point <https://git-scm.com/doc/ext>`__)
* the documentation of the :doc:`../workflow/workflow`,
* the :doc:`../tutorial/index`

Once you've gone through the resources and decided you want to start the first trial commission,
we will ask you to consider and sign an agreement which serves as the legal foundation for our collaboration
and you will be assigned your first remunerated commission for your training phase.

The trial phase
---------------

We will be in close contact giving you feedback on your work and answering to your
technical and annotation-related questions. Naturally, you can decide to opt out of the the training phase at any moment.
Once you feel firm enough with the annotation standard and have gathered enough experience with the workflow,
we will (virtually) sit together, discuss how it went, and decide if and how to continue our collaboration.

Becoming part of the project
----------------------------

The DCML syntax has grown more and more expressive during the last years to account for the
wide variety of analytical viewpoints that can be appropriate for particular styles of music
(we try to cover Western tonal music to the largest possible extent). At the same time, continuous discussions with and
between annotators and reviewers have helped refining the annotation guidelines that are supposed to constrain the
vast space of analytical possibilities just enough to facilitate decision-making during the analysis and to allow for
some degree of comparability between all DCML labels. If your heart has started pounding at the thought of becoming
part of this initiative, please consider joining us.

In case this activity is not for you and you are still reading this,
we want to thank you for considering the option in the first place.