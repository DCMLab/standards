*****************************
DCML Corpus Creation Pipeline
*****************************

#. :ref:`score_repo`

.. _score_repo:

Creating a repository with unannotated MuseScore files
======================================================

.. danger:: After we start the annotation workflow, no MuseScore files should be added. removed, or renamed!

Before starting annotating a corpus, a repo with the standard folder structure needs to be created:

.. code-block:: console

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
  an empty Git repo that will be connected upstream at a later point:

  .. code-block:: console

    mkdir chopin_mazurkas && cd chopin_mazurkas && git init

  Make sure that your Git is configured to use the name ``main`` for the default branch, which can be achieved using
  ``git config --global init.defaultBranch main``.

Clone repo A and transfer files
  We start off with a fresh clone of ``corpora``, head into it and run

  .. code-block:: console

    git filter-repo --subdirectory-filter annotations/Chopin-Mazurkas/ --target ../chopin_mazurkas

  which will copy all files from ``annotations/Chopin-Mazurkas/`` to the freshly initialized repo
  ``chopin_mazurkas`` together with their full commit histories. If there is a README file, rename it to ``README.md``.

Connect local repo B to the remote repo B
  The local ``chopin_mazurkas`` now contains the files at the top level together with the full commit
  history (check out ``git log``). Now we can connect it to the remote and merge the workflow scripts from there:

  .. code-block:: console

    git remote add origin git@github.com:DCMLab/chopin_mazurkas.git
    git pull origin main --allow-unrelated-histories
    git push -u origin main

Clean metadata
  In case there was an older ``metadata.tsv`` it should now be automatically updated and you might have to clean it.
  This may involve naming the first two columns ``rel_paths`` and ``fnames``. For the Mazurka example,
  `this Pull Request <https://github.com/DCMLab/chopin_mazurkas/pull/1>`__ shows the metadata cleaning and update
  of the existing files from an older MuseScore and annotation standard.
