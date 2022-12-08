*************************
Becoming a DCML annotator
*************************

.. contents:: Contents
   :local:

Introduction
============

The Digital and Cognitive Musicology Lab (`DCML <https://www.epfl.ch/labs/dcml/>`__) at École Polytechnique Fédérale de
Lausanne (EPFL, Switzerland) is searching for contributors to its growing corpus of symbolically encoded harmonic analyses.
Remunerated on a per-measure basis, selected applicants will be producing and/or reviewing analyses in the form of typed-text annotations on MuseScore files.

This effort is longstanding and central to the lab’s overarching `Corpus Initiative <https://www.epfl.ch/labs/dcml/projects/corpus-project/>`__,
which studies the development of tonality in instrumental and vocal music of the 17th to the late 20th century.


Working as an annotator
=======================

* DCML annotators take on commissions at their preferred pace and invoice their work upon its completion.
* Before we commit to collaborating with potential annotators, we ask them to go through a
  trial onboarding phase during which they may familiarize themselves with the workflow and annotation syntax.
  Annotation tasks performed during the trial are remunerated at the same rate as regular annotation work.
* If both sides accept to proceed after this trial phase, the newly trained collaborator begins to self-assign annotation
  and review tasks from a list of available work packages, which consist in the identification of harmonic content,
  grouping structure, and cadence types in the selected pieces.
* Annotation labels must adhere to the `DCML Harmony Annotation Standard <https://dcmlab.github.io/standards`__.
  They are submitted for review using the :doc:`../workflow/workflow` which requires good knowledge and handling of
  the version control software `git <https://git-scm.com/>`__.

To get an idea of the whole process, you may refer to the following two publications:

- Conference paper on the annotation workflow: `https://doi.org/10.5281/zenodo.5624416`__ (the essential sections are 3 through 4.4)
- Data report on the Annotated Mozart Sonatas: `http://doi.org/10.5334/tismir.63`__

Tasks
-----

Our workflow currently includes four different kinds of tasks that annotators can select from as they please.
The final outcome of every commission must always always be approved by an annotator and a reviewer, and consists of:

* an expert analysis of the harmonic structure, including musical phrases and cadences;
* encoded in a machine-readable syntax,
* syntactically validated through software,
* and approved by consensus between at least two experts.

Two types of annotation tasks are available:

* ``New annotations``: creating a new set of annotations from scratch;
* ``Annotation upgrade``: revisiting an existing set of annotations, and revising it to conform to the latest version of the
  annotation standard (this often involves adding cadence labels).

Both tasks require that another annotator reviews your work and that, in the case of analytical divergence,
the two of you engage in a constructive debate, adapting the annotations until consensus is reached. Review tasks are
integral to the annotator's role and compensated at two different tariffs, depending on the kind of annotation
tasks reviewed.

Remuneration and invoicing
--------------------------

The tariffs for the aforementioned tasks are as follows:

* new annotations: 0.50 CHF per measure
* upgrading existing annotations: 0.40 CHF per measure
* reviewing new annotations created by someone else: 0.40 CHF per measure
* reviewing annotations upgraded by someone else: 0.20 CHF per measure

We have painstakingly adjusted these tarifs and believe they are fair: while harmonic contents per measure vary, payments tend to even out over several commissions.

The remuneration for each task is logged alongside the title of the respective work package once finalized. Whenever an annotator decides
to invoice one or several commissions, they can generate an automatic report and attach it to the invoice. Payments
usually arrive less than three weeks after sending an invoice.


Coordination & Tools
--------------------

The corpus initiative relies on two tools:

#. OpenProject for self-assigning available tasks, tracking the status of work packages, and generating overviews
   of the logged costs for invoicing.
#. GitHub for storing the data (scores & annotations) and its entire version history (non-annotated -> annotated -> reviewed).
   The underlying version control software is git. If you have never heard of it, your training is going to be a bit
   more involved but with regular practice it can be learned rather quickly.
#. Mattermost for internal communication.


Minimum requirements
--------------------

* a Master’s degree in Music Theory (or equivalent);
* excellent knowledge of tonal harmony, contrapuntal patterns, and schemata;
* a computer running the latest version of `MuseScore <https://musescore.org/>`__;
* willingness to undertake tasks on a regular basis;
* a bank account under your name, which accepts money transfers from Switzerland.

Desirable criteria
------------------

- experience with MuseScore;
- experience with version control software (git).

How to get involved
===================

If you're interested in becoming an annotator and fulfill the minimum requirements above, we invite you to introduce
yourself and express your interest in an email to `dcml.annotators@epfl.ch`__. We will let you know whether we have
openings for new annotators or not. If so, we will invite you to proceed as follows.

Before the trial phase
----------------------

Before we start the actual training, we require candidates to familiarize themselves with the a few resources:

* (if not familiar with git:) any of the countless learning resources of the web
  (`this could be a starting point <https://git-scm.com/doc/ext>`__)
* the documentation of the :doc:`../workflow/workflow`,
* the :doc:`../tutorial/index`

Once you've gone through the resources and decided to start the first trial commission,
we will ask you to consider and sign an agreement which serves as the legal foundation for our collaboration.
You will then be assigned your first remunerated commission of your training phase.

The trial phase
---------------

We will be in close contact, giving you feedback on your work and answering
the technical and annotation-related questions you will probably have. Naturally, you can decide to opt out of the the training phase at any moment.
Once you feel confident enough in the annotation standard, and have gathered enough experience with the workflow,
we will sit together (virtually), discuss how it went, and decide if and how to continue our collaboration.

Becoming part of the project
----------------------------

The DCML syntax has become increasingly expressive during the last years to account for the
wide variety of analytical viewpoints and musical phenomena that are relevant to different styles of music.
(We try to represent Western tonal music to the largest possible extent.) At the same time, years of feedback from annotators and reviewers has helped us refine our annotation guidelines in ways that promote interpretive consistency within the vast space of possible harmonic analyses, thus ensuring
a degree of comparability between harmonic "languages" centuries apart.

If your heart has started pounding at the thought of becoming part of this initiative, please consider joining us. On the other hand, if you feel that this activity is not for you, and are still reading this, we want to thank you for your interest in the first place.
