************************
DCML annotation workflow
************************

.. contents:: Contents
   :local:

.. note:: It is of utmost importance that annotators have a basic understanding of version control and branching
   via Git before they get familiar with the DCML annotation workflow. The :ref:`Quick reference <git-intro>` below
   contains the bare minimum of what annotators need to know, but if you're completely new to Git, please make sure
   to read, watch, or do a couple of tutorials online.

Short summary
=============


#. Annotator:

   * creates a new branch (splitting off of ``main``!) named after the file to be annotated
   * pushes annotations and corrects errors that were :ref:`automatically detected on GitHub <syntax_errors>`,
   * creates Pull Request (PR)

#. Reviewer:

   * reviews the annotations and commits every change separately into the open PR
   * approves the changes on GitHub, enabling the annotator to agree and merge

#. Annotator:

   * Pulls the changes and goes through reviewer's commits in the PR
   * in case of disagreement, enters into discussion with reviewer until consensus is reached
   * merges PR as soon as both parties agree on a set of labels.

More details can be found below.

.. _annotating:

Annotating
==========


Head to your local clone of the repository in which you want to annotate a piece and update the main branch.
  ::

    git checkout main
    git pull

Create a new branch that has exactly the same name as the file you are going to annotate.
  In this example, we want to annotate the first movement of Corelli's first trio sonata which is called
  ``op01n01a.mscx``, so we do::

    git checkout -b op01n01a

Annotate the piece.
  Open ``op01n01a.mscx`` with the latest version of MuseScore and insert your labels while saving the file
  from time to time. Don't forget to create the following metadata fields by going through the menu
  ``File -> Score Properties...``:

  * ``annotators`` (plural form!): your name
  * ``harmony_version``: version of the annotation standard you are using (currently 2.3.0)

  .. figure:: img/musescore_metadata.png
      :alt: Entering metadata in MuseScore
      :scale: 80%

      Entering metadata in MuseScore

Commit your changes locally and describe the commit in the commit message.
  ::

    git add -A
    git commit -m "annotated mm. 1-15"

  .. hint:: Since you'll use these commands quite a lot, you might want to create aliases, i.e., shortcut commands,
     for example ``ga`` and ``gc``. A web search for "create alias [your operation system]" will tell you how.

  Other examples for meaningful commit messages could be ``"annotated the entire movement"`` or ``"fixed syntax error
  in m. 17"``. Please include measure numbers whenever applicable.

.. _syntax_errors:

Push your commits to GitHub and check if syntactical errors are detected.
  ::

    git push

  .. note:: At the first time you will be asked to connect your new local branch to GitHub using the command
     ``git push --set-upstream origin op01n01a`` or whatever the name of the new branch is.

  Everytime you push your commits to GitHub, the scores you've modified will be checked automatically and you can see
  immediately if there are any syntactic errors or where the notes in the score do not match the label.
  Simply head to the GitHub repository and click on the ``Actions`` tab.
  There you will see your last commit with a small coloured symbol:

  :yellow: Check in progress (wait a couple of seconds)
  :green: Everything OK
  :red: Syntactical error(s) detected

    .. figure:: img/github_actions_tab.png
      :alt: The last commit listed in the ``Actions`` tab with the red icon symbolizing that the syntax check failed.
      :scale: 80%

      The last commit listed in the ``Actions`` tab with the red icon symbolizing that the syntax check failed.


When tests have failed, please go back to your local MuseScore file and commit the changes necessary to make them pass
next time you push. Remember to include explanatory commit messages and measure numbers.
Still under the ``Actions`` tab, click on the failed syntax check and then on ``perform_check``

  .. figure:: img/github_check_perform_check.png
      :alt: Click on "perform_check"
      :scale: 80%

      Click on "ms3_review"

  Put the word "warning" into the black search bar and go through all warnings.

  .. figure:: img/github_syntactical_errors.png
      :alt: Log of ms3 review showing incorrect labels
      :scale: 99%

      Output log of the `ms3 review` command; use the search bar to go through every `_WARNING`.

  Where applicable, every warning comes with a measure count ``MC`` and/or a measure number ``MN``. MC corresponds
  to the bar number that MuseScore displays in the
  status bar on the bottom left (not always identical to the measure number (MN) in the score). The warning's message
  is hopefully expressive enough for you to know what to do. If not or you're unsure, you may look it up in thea
  label's offset from the barline, ``mc_onset``, measured in fractions of a whole note, and the incorrect label. From here on,
  simply correct the labels, commit and push again, and the check should pass this time.

Once all your labels are syntactically correct, create a Pull Request.
  There are (at least) three different ways for creating a Pull Request (i.e. a request for merging your annotations
  from the new branch into ``main``):

  1. Head to the main page of the GitHub repository where you should see a banner allowing you to quickly create
     a pull request:

     .. figure:: img/github_pr.png
        :alt: GitHub offering to creat a new pull request

        GitHub offering to create a new pull request with the recently pushed annotations

  2. Otherwise, select the new branch from the dropdown menu

     .. figure:: img/github_select_branch.png
        :alt: Selecting a branch on GitHub

        Selecting a branch on GitHub

     and click on ``Contribute -> Open pull request``

     .. figure:: img/github_open_pr_from_branch.png
        :alt: Opening a PR directly from the branch.

        Opening a PR directly from the branch.

  3. Or, head to the ``Pull requests`` tab, click on "New pull request" and select your branch accordingly, like this:

     .. figure:: img/github_create_pr.png
        :alt: Giving the new pull request a meaningful title

        Giving the new pull request a meaningful title

Give the pull request a meaningful name and feel free to add anything worth knowing below. Once you confirm with
the green button "Create pull request", you're done. In case more pieces were commissioned to you, you can continue
annotating, but make sure to create the new branch for the next piece after checking out and updating ``main`` first!

.. _modulation_plans:

Modulation plans
----------------

Since November 2021, the DCML workflow includes a new feature, namely the automated creation of modulation plans.
Once a Pull Request (PR) is created, modulation plans are generated and updated for all altered MuseScore files. They
come in the form of HTML files and are stored in the folder ``tonicizations``. After you create a PR or push into an
existing one, the ms3-bot will commit these files, so in order to view them, you need to wait for the bot's commit
and then pull it into your local clone.

For example, in `this PR <https://github.com/DCMLab/schubert_dances/pull/516>`__,
the annotator pushed a new set of annotations, requested a review and then the bot added
the HTML file in the commit "Added comparison files for review". In order to view the file, the annotator will
do a ``git pull``, find it in the folder ``tonicizations`` and open it in a browser:

.. raw:: html
   :file: interactive/D718walzer01.html

:Gantt chart: *Automatically generated modulation plan in HTML format, displayed through a browser.*

The modulation plans display the tonal hierarchy represented by your annotations and allow you to check if your labels
correspond to your understanding of the piece's structure. The keys that the piece modulates to are shown in blue,
temporary tonicizations (slash notation) are shown in red, and adjacency of the tonicized numerals in green. More
detailed information on the keys is shown when hovering over the figure. If you find inconsistencies, simply
correct them in your MuseScore file and commit them into the open PR, the modulation plan will be updated and overwritten,
so you can pull it and check it once more.

Upgrading annotations
=====================

Upgrading an existing set of annotations created under an older version of the DCML annotation standard roughly
follows the same workflow as the :ref:`creation of new labels <annotating>` above. The main difference is that during
the upgrade, you commit your changes individually, justifying each of them in a commit message starting with the
respective measure number.

Create a new branch and adapt the metadata.
  As an example, let's upgrade the labels of ``op01n06a.mscx`` from version 2.1.1 to 2.3.0. In this screencast,
  the score is already open and you see how the metadata is updated and committed to a new branch called ``op01n06a``.

  .. note:: that the commands ``ga`` and ``gc`` are aliases, i.e. shortcut commands, which you would replace by
     ``git add -A`` and ``git commit -m`` respectively (unless you have created your own aliases).

  .. figure:: img/upgrade_metadata.gif
     :alt: Updating the metadata reflecting the version upgrade.

     Updating the metadata reflecting the version upgrade. The screencast starts at ``cd corelli``.

  As you can see, the metadata field ``annotators`` is updated in a way that the old version is added to the previous
  annotators and that the upgrader adds themselves to the annotators, indicating the new versions. Since the version
  upgrade includes a review of the existing labels, they also add their initials to the ``reviewers`` field.

Review and update the labels and commit your changes individually.
  The following screencast demonstrates the upgrade process of ``op01n06a.mscx``. In principle, after every change
  the file is saved and the change is committed with the measure number and an explanation.

  .. note:: that the commands ``ga`` and ``gc`` are aliases, i.e. shortcut commands, which you would replace by
     ``git add -A`` and ``git commit -m`` respectively (unless you have created your own aliases).

  .. _individual_commits:

  .. figure:: img/upgrade_commits.gif
     :alt: Giving the new pull request a meaningful title

     Creating individual commits for every change or group of changes. The screencast produces the syntax error
     ``V6/III(2)`` (instead of ``V6(2)/III``) that is automatically detected upon push to GitHub (see screenshot below).

  As you can see, similar changes can be grouped as one commit, as for m. 2. Phrase annotations such as the added
  curly bracket in m. 1 do not need to be committed individually.

Push your commits and create a Pull Request
  From here on, the procedure is the same as for new annotations, only that the PR will be called something like
  ``Upgraded op06n01a to 2.3.0``. Just like for new annotations, your version will be syntactically checked. For
  example, the mistake in the above screencast will be displayed like this:

  .. figure:: img/github_syntax_error.png
     :alt: Automatically detected syntax error from above, as displayed on GitHub.

     Automatically detected syntax error from above, as displayed on GitHub.

  Shortly after opening the PR, the ms3-bot will create two additional files that will help you and the reviewer
  understand your changes: An additional MuseScore file showing all changes you have made, and a :ref:`modulation plan <modulation_plans>`
  (in the folder ``tonicizations``) reflecting your updated set of labels. To see these files, you will need to
  update your local clone so that it includes the bot's commit: ::

    git checkout op01n06a
    git pull

Reviewing a set of annotations
==============================

Reviewing a set of new annotations and a set of annotations upgraded to a new version works essentially the same way,
but with one important difference. To review new annotations, you first need to merge the PR into ``main`` and create
a new one after you finished your review. For upgraded annotations, this is not necessary and you can push your commits
into the open PR right away. The reason for this is the automatic creation of the ``_reviewed`` files,
as explained in the following.

In order for the annotator or upgrader to comprehend the changes you made during your review, not only do you need
to commit and explain your changes individually (indicating the measure number of the respective change). Also,
an additional copy of the MuseScore file in question will be automatically created where your changes are highlighted
with different colours. The creation of such a ``_reviewed`` file depends on the presence of an automatically
extracted TSV file which includes a table with the labels as they were before you made your changes. For new
annotations, this file needs to be generated by merging the PR with the new annotations into ``main``. In the case
of a PR with upgraded labels, the TSV file with the previous labels should already be present, indicated by the fact
that a ``_reviewed`` file should already have been pushed into this PR by the ms3-bot (e.g., in the following
screenshot, the commit ``Added comparison files for review``).

.. _new_annotations:

Reviewing a new set of annotations
----------------------------------

.. admonition:: Update May 2022
   :class: note

   The procedure described in the following (i.e. the reviewer to merge the PR into ``main``, merge the updated ``main``
   back into the annotation branch and create a new PR) is slightly redundant and soon to be deprecated. Additionally,
   it is currently not working because merging a PR now requires at least 1 reviewer's approval on GitHub. Before the
   automatic scripts will be updated to solve this problem, the best workaround requires the reviewer to install and
   run a program in order to generate and commit a TSV file, which normally the ``ms3-bot`` would have done.
   If the steps below don't make any sense to you, please contact us so we can set everything up together for the time being.

   1. `Python 3 <https://www.python.org/downloads/>`__ needs to be installed on your system. If asked, have the
      commands ``python`` and ``pip`` added to your PATH.
   2. Install the program (a parser for MuseScore 3 files) via pip: ``pip install -U ms3``.
   3. Navigate to the GitHub repo in question (using ``cd``) and checkout the Pull Request to be reviewed.
   4. Issue the command ``ms3 extract -X -f MS3/{filename}`` replacing ``{filename}`` with the file you are about to review.
   5. Take note of the log messages. The last one should say that the file ``harmonies/{filename}.tsv`` has been written,
      which you can verify via ``git status``.
   6. Commit the file using a message such as ``extracted annotations``.
   7. Now you are ready to perform the review, committing one change at a time.
   8. Leave the annotator/upgrader a comment with an ``@``-mention to make sure they are informed.


First, open the Pull Request containing the new labels and check if all syntactic errors have been corrected.
  As can be seen in the following image, in the PR, all commits made by the annotator and by the ms3-bot are listed,
  two in this example.

  .. figure:: img/github_pr_commits.png
     :alt: A pull request were some syntactic errors have not been corrected yet.

     A pull request were some syntactic errors have not been corrected yet.

  It is important to note that the last commit made by the annotator (``fully annotated op01n01a``) has a red cross instead of a green check. Although
  the last commit by the ms3-bot has a green check, the error persists (bot's commits are not checked for syntactical
  correctness). In this case, please leave a comment below, asking the annotator to correct the labels and to let you
  know once they are done.

.. admonition:: Warning
   :class: danger

   It is important to never merge syntactically incorrect labels into ``main`` because such errors would
   propagate to other branches, causing failed syntax checks for your fellow annotators.

Merge the PR
  Once there are no syntactical errors left, take note of the annotator's comments, if any, to be able to react to them,
  and click on 'Merge pull request'. This will trigger the script that
  extracts the new labels and pushes the corresponding TSV file to the ``harmonies`` folder. Go to the main branch
  and wait about 30 seconds, refreshing the page sporadically to see whether the ms3-bot has made the commit called
  ``Automatically added TSV files from parse with ms3``. Then you're ready to continue.

Merge the updated ``main`` branch into the updated annotation branch.
  The newly created TSV files needs to be present in the annotation branch where you perform the review. Therefore,
  assuming you are reviewing ``op01n01a.mscx``: ::

    git checkout main
    git pull
    git checkout op01n01a
    git pull
    git merge main

.. _how_to_review:

Now you are ready to start your review.
  * At first you start by adding your initials to the metadata field ``reviewers`` (plural!), comma-separated in case
    the field is already populated. Doing that, you may also want to check whether the annotator spelled the fields
    ``annotators`` and ``harmony_version`` correctly.
  * **Update November 2021** At any point of the review, check the associated :ref:`modulation plan <modulation_plans>`
    by finding the corresponding HTML file in the folder ``tonicizations`` and opening it in your browser. It helps
    to check if the tonal structure expressed by the labels corresponds to the one you and the annotator have in mind.
  * Reviewing a new set of annotations means reading through the labels to see whether you agree with
    each of them on the basis of the :doc:`annotation tutorial <../tutorial/index>`, paying special attention to
    consistency within the piece and consistency across similar annotated pieces.
  * For every label where you feel the need to remove, reinsert, or replace it, you do the change directly in the
    MuseScore file, save it, and commit the alteration giving as a commit message the measure number(s) and your
    justification. In the case of obvious mistakes, it is enough to indicate the replacement, as in
    ``"4: #viio/V => viio/V"``. You may indicate commits were your change is a suggestion that you would be happy
    to discuss by a trailing question mark, e.g. ``"15.2: how about including V65 as an alternative label?"``.
    You may also address the comments and questions that the annotator had left with their original PR in commit
    messages, or you could address them in comments, as explained below.
    The procedure is technically identical with the :ref:`example screencast above <individual_commits>`.
  * Once you are happy with the labels in their entirety, you are ready to push your changes, see whether the
    syntax check passes, and launch a new Pull Request entitled ``Reviewed [file name]`` (you may do this even
    before the syntax check finishes, since you can always add commits to a PR). While or after opening the PR,
    please request a review from the annotator through this interface on the right side:

    .. figure:: img/github_review_suggestions.png
       :alt: GitHub usually suggests the annotator for a review, otherwise use the menu to select the user handle.

       GitHub usually suggests the annotator for a review, otherwise use the menu to select the user handle.
  * Naturally, you may include comments or points worth discussing in the description of your PR. You can also
    add comments on the bottom of the page, or attach a comment to a certain commit/change to have the changed
    labels displayed together with your comment. To do that, in the open PR, you click on the commit in question,
    and, in the particular line in the source code, click the plus symbol, as can be seen in the
    :ref:`screenshot below <pr_comment>`. Be sure to always include a measure number, so that your respondent can
    find the spot in the MuseScore file.
  * From here on, monitor your GitHub notifications for reactions to your PR from the annotator. Use the comment
    function to discuss individual solutions until you find a consensual one for each controversial label. This
    process usually includes you and the annotator committing further changes to the MuseScore file with
    expressive commit messages (always including the measure number). In case you are working with the automatically
    generated ``_reviewed`` file to display all changes made in the PR, be aware that you never commit changes to this
    file, since they will be overwritten automatically.
  * In the (rare) case where you would be unable to form a consensus, please include in the discussion a third person
    of whom you think they could bring in weighty arguments. Another way would be to bring the discussion to a
    Mattermost channel if you think the question requires a fundamental decision based on a larger consensus.
  * Once the new annotations correspond to a consensus between you and the annotator, the person who made the last
    decision in the process merges the PR. As a last step, go to the main branch, wait for the automatic
    ``Automatically added TSV files from parse with ms3`` commit, and check if the corresponding table row in the
    README got updated correctly (otherwise, the metadata fields in the MuseScore file were not correctly populated).
    The piece has now been finalized and is ready for eventual publication. Thank you!


Reviewing a set of upgraded annotations
---------------------------------------

Making use of the ``_reviewed`` file.
  In the case that existing labels were upgraded, the corresponding TSV file was already present in the ``harmonies``
  folder, meaning that after every push into the open PR, ms3-bot updates the ``_reviewed`` file to reflect `all`
  changes made within the PR.
  This means that for starting the review, you can checkout and pull the corresponding branch and view the file to
  see all changes made by the upgrader. Once you commit your changes on top,
  the file will be updated to reflect the changes between the deprecated labels
  (those that the upgrader updated) and the final version after your review. If you were to instead generate a file
  reflecting only the differences before and after `your` review, you would have to follow the steps in the
  :ref:`previous section <new_annotations>`, i.e. merge the PR and open a new one.

Review the labels
  The procedure is essentially the same as the one for :ref:`reviewing new annotations <how_to_review>` above. The difference is that you focus
  more on the labels changed by the upgrader, exercising particular care for potential inconsistencies that might
  have arisen; for example by applying a change to one place but not to an analogous one; or by having missed a
  subtle aspect in the previous, replaced label, that actually made for an ideal solution; etc.


Reacting to a review & reaching expert consensus
================================================

Once your file(s) got reviewed, the reviewer creates a pull request (PR) and requests your review. You should
receive an e-mail notification, if not, please check your GitHub settings. Now your task is to go through all changes
and see whether you agree with all of them. Here is how:

How to review a review
----------------------

Open the PR from your notification e-mail or go to GitHub and open the ``Pull requests`` tab where you should see it.
The PR lets you inspect all changes and start discussions. Most importantly, after opening it, you will see all
commits made by the reviewer:

.. figure:: img/pr_commits.png
    :alt: List of commits made by the reviewer
    :scale: 95%

    List of commits made by the reviewer

Clicking on one of them will show you the corresponding changes in the MuseScore file. But it might be hard for
you to assess the changes without looking at the actual music. Therefore:

The last commit, called "Added comparison files for review", was made automatically by ``ms3-bot``,
creating an additional MuseScore file with the suffix ``_reviewed``. Therefore, the first thing you want to do to
review the review, is locally checkout and pull the branch corresponding to the PR
(it should be the same you created for annotating). As an example, if in the PR it says

.. figure:: img/github_pr_description.png
    :alt: johentsch wants to merge 2 commits into main from op01n01a
    :scale: 95%

    johentsch wants to merge 2 commits into main from op01n01a

it means you do::

  git checkout op01n01a
  git pull

Now you should have the comparison MuseScore file  ``_reviewed``
in your local clone and can open it in MuseScore. It shows unchanged labels in black,
labels removed by the reviewer in red, and labels added by the reviewer in green.
The sole purpose of this file is to help you with the review of the review and will be deleted
at some later point (it is not listed in the metadata either). In case this comparison file (and the corresponding
commit ``Added comparison files for review``) is missing, the reviewer might have made a procedural mistake and
you should ask for it to be created before you review the changes.

How to finalize the review of the review
----------------------------------------

Now you can go through the list of commits one by one and check how they play out in the comparison file. For every
change that you agree with, there is nothing you need to do. In cases where you don't agree, you write a comment
on GitHub (see next subsection) and discuss with the reviewer until you find a solution that satisfies both analytical
views. In addition, you may want to suggest a new label by integrating it in the *original* file (not the
``_reviewed`` file) and committing the change with a meaningful commit message that includes the measure number
(e.g. ``"14.4: included my original solution V43(4) as an alternative solution"``).
Once you push the changes, they will be included into the PR and the comparison file will be updated accordingly.
As soon as the original file contains a set of annotations that you and the reviewer agree to be the best possible
solution, the person who made the last
decision in the process merges the PR. As a last step, go to the main branch, wait for the automatic
``Automatically added TSV files from parse with ms3`` commit, and check if the corresponding table row in the
README got updated correctly (otherwise, the metadata fields in the MuseScore file were not correctly populated).
The piece has now been finalized and is ready for eventual publication. Thank you!

How to start a discussion
-------------------------

To start a discussion, click on the commit you disagree with. On the left you see in red your previous version and
on the right, in green, the changes made by the reviewer. Hovering over the code lines, you will see a blue plus
that lets you add your comment. It is important that you add the measure number so that the reviewer can find
the spot and react to your comment.

.. _pr_comment:

.. figure:: img/pr_comment.png
    :alt: Starting a discussion by commenting the reviewer's commit
    :scale: 95%

    Starting a discussion by commenting the reviewer's commit

The comments and resulting discussions will be visible in the PR's "Conversation" tab (under the list of commits).
Don't forget to press the Subscribe button on the right to get informed about reactions to your comments.


.. _warnings:

What to do about the warnings?
==============================

There can be a range of reasons why you may see a ``WARNING`` in the output log of the automated tests.

#. One or several labels do not conform to the current version DCML harmony annotation syntax.
#. The parentheses of organ point or phrase annotations do not add up to complete pairs.
#. One or several labels express chord tones that match badly or not at all with the notes in the given segment(s).
#. There is an encoding error or inconsistency in the MuseScore file (e.g. one that leads to wrong measure numbers)
   which needs to be fixed. Since oddities are omnipresent in music, we sometimes want to suppress a warning and
   leave a comment saying as humans that the exception from the norm is justified.
#. Sometimes you don't get a warning but instead a (somewhat cryptic) error, which might actually a bug, i.e. mistake
   in the code. If you think it is, please `create an issue <https://github.com/DCMLab/dcml_corpus_workflow/issues>`__
   and point us to the error, e.g. by pasting the output or a link to it, and the score in question so we can look into it.



Syntax errors
-------------


#8 DCML_HARMONY_KEY_NOT_SPECIFIED_ERROR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#12 DCML_HARMONY_INCOMPLETE_LOCALKEY_COLUMN_ERROR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#13 DCML_HARMONY_INCOMPLETE_PEDAL_COLUMN_ERROR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#15 DCML_HARMONY_SYNTAX_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#16 DCML_PHRASE_INCONGRUENCY_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#17 DCML_EXPANSION_FAILED_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




Semantic mismatches
-------------------

#6 DCML_HARMONY_SUPERFLUOUS_TONE_REPLACEMENT_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#18 DCML_SEVENTH_CORD_WITH_ALTERED_SEVENTH_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#19 DCML_NON_CHORD_TONES_ABOVE_THRESHOLD_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Irregularities and score encoding errors
----------------------------------------

.. _warning_1:

#1 MCS_NOT_EXCLUDED_FROM_BARCOUNT_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#2 INCORRECT_VOLTA_MN_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#3 INCOMPLETE_MC_WRONGLY_COMPLETED_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#4 VOLTAS_WITH_DIFFERING_LENGTHS_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#5 MISSING_END_REPEAT_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#9 COMPETING_MEASURE_INFO_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#14 LOGGER_NOT_IN_USE_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#20 UNUSED_FINE_MARKER_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#21 PLAY_UNTIL_IS_MISSING_LABEL_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#22 JUMP_TO_IS_MISSING_LABEL_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#23 MISSING_TIME_SIGNATURE_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No time signature present throughout the piece. Needs adding one.

#24 BEGINNING_WITHOUT_TIME_SIGNATURE_WARNING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This warning shows when more than just the first bar has no time signature (if it's only one measure
it is considered to be an incipit). Please check if a time signature is missing or add the warning
to :ref:`ignored_warnings`.

#25 INVALID_REPEAT_STRUCTURE = 25
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _ignored_warnings:

IGNORED_WARNINGS
----------------