****************************************
Work package management with OpenProject
****************************************

To facilitate assigning work packages, reviews, and accounting, we are using a self-hosted
`OpenProject instance <https://op-musicology.epfl.ch>`__.

.. contents:: Contents
   :local:

Workflow
========

In a nutshell
-------------

Independent on which task you are performing, you simply need to remember to change the status **before and after** working
on a piece. This way it is possible to self-assign without duplicating any work. Each package corresponds to one piece
that needs to be annotated (package type ``New annotations``) or upgraded (package type ``Annotation upgrade``).
Each package traverses the following statuses, in this order:

* ``Not available``: to be disregarded for now
* ``Available``: to be (self-)assigned; the ``Assignee`` field should be empty and once filled the status needs to be changed to
* ``In progress``: currently being undertaken by the person marked in the ``Assignee`` field
* ``Needs review``: the annotator/upgrader has finished and the person (self-)assigned in the ``Reviewer`` field should
  begin their review
* ``Under review``: review & subsequent discussions currently in progress (refer to the PR).
* ``Done``: ``Reviewer`` as approved the PR which consequently has been merged by the ``Assignee``.


In more detail
--------------

Decide what you want to work on.
  As a general principle, please give preference to finalizing tasks before
  addressing new work packages (WPs). Starting from May 2022, both ``Assignee`` and ``Reviewer`` may only invoice
  work packages that have reached the status ``Done``, meaning that the associated Pull Request (PR) has been reviewed
  and merged.

  * First, make sure you have addressed all comments and new commits in the PRs in which you
    are involved (always make sure you are subscribed on GitHub in order to receive notifications).
  * When all PRs have been addressed, please use OpenProject's filter functionality to see if

    - you are the ``Assignee`` for packages with status ``Available``
    - you are the ``Reviewer`` for packages with status ``Needs review``

    Usually, if this is the case, it is because of an agreement you have made with DCML. The default is that people
    self-assign.
  * If your desk is clean and you want to take on a new task, use the
    ``Work packages -> To Do`` view.
    Please give preference to the packages with status ``Needs review`` in order to finalize them quickly, to make
    them invoiceable, and to get them out of our way.

Self-assign.
  * If you are addressing a package with status ``Needs review``, the ``Reviewer`` field needs to be empty so
    you can enter your name and set the status to ``Under review``. Otherwise, the review has been assigned to
    someone else. For details, :ref:`see below <taking_on_a_review>`.
  * If you are addressing a package with status ``Available``, the ``Assignee`` field needs to be empty so
    you can enter your name and set the status to ``In progress`` **and the ``Start date`` to "Today"**.
    Otherwise, the task has been assigned to someone else. For details, :ref:`see below <taking_on_a_task>`.

Perform the task according to the usual :doc:`GitHub workflow <../git/git>`.
  * If you are the WP's ``Assignee`` you end your task by creating a Pull Request that you link to the WP by including
    the WP's URL in the PR's description (:ref:`see screencast below <taking_on_a_task>`).
  * If you are the WP's ``Reviewer`` your task ideally ends with you having committed to the PR to the point where you
    approve it (:ref:`see screencast below <taking_on_a_review>`).

Change the WP's status and :ref:`log the costs <logging_costs>`.
  * If you are the WP's ``Assignee``, you change the status to ``Needs review``. If it takes too long (say two weeks)
    for anyone to take on the review, please ping your fellow annotators.
  * If you are the WP's ``Reviewer``, there is nothing for you to change in the work package. If, after your approval,
    the ``Assignee`` takes unreasonably long to merge the PR and set the status to ``Done`` (thus allowing you to
    invoice your work) you may ping them politely.

Finalize the WP.
  Once the ``Reviewer`` has approved the PR and the ``Assignee`` has reviewed and agreed with their changes, it is
  the ``Assignee`` you merges the PR and enables the package for invoicing by performing two equally important steps:

  * The WP's status is changed to ``Done`` so it can show up in the :ref:`cost reports <creating_cost_report>`.
  * The WP's ``Finish date`` needs to be set to "Today" so as to allow for filtering out previously invoiced
    cost items.


User Interface
==============

.. figure:: img/op_overview.png
     :alt: Overview over OpenProject's user interface

1. Make sure to access the project ``Harmony Annotations`` (you need to be added by an admin).
2. Go to ``Work packages``.
3. To see or alter information of a work package, click on its ID or use the blue menu that appears when hovering
   over the right end of the row.
4. Use the filters to see only particular work packages.
5. Use the menu ``... -> Save as...`` to save a filtered view.
6. Find saved views in the ``Work packages`` sub-menu

Taking on an assignment
=======================

1. In the work package sub-menu, use the ``Assigned to me`` default view to check if any of the packages assigned to you
   require your action. Finish any open tasks before taking on new ones.
2. Use the view ``To Do`` to display work packages that have status ``Available`` or ``Needs review``.
3. Assign yourself, change the status, and the ``Start date``.
4. Perform the task and include the URL of the work package in the description of your Pull Request (see below).
5. Change the status, log the costs.
6. Follow the progress of the Pull Request and the work package and, if needed, ping fellow annotators to undertake the review.
7. Once the PR has been reviewed and a consensual solution found, the ``Assignee`` merge the PR, sets the status to
   ``Done`` and the ``Finish date`` to today. Only at this point can assignee and reviewer
   :ref:`invoice the task <creating_cost_report>`.

.. _taking_on_a_task:

Taking on ``New annotations`` or an ``Annotation upgrade``
----------------------------------------------------------

.. figure:: img/op_assignment.png
     :alt: Details page of a work package
     :scale: 50%

Open the details of the corresponding work package.

1. Change the status from ``Available`` to ``In progress``.
2. Add your name to the field "Assignee" (which should be empty).
3. Set the "Start date" to ``Today``.

**Once you have completed the job:**

.. figure:: img/op_github.png
     :alt: The GitHub pane of a work package
     :scale: 50%

1. You want the Pull Request to show up in the "GitHub" pane of the work packages so that the reviewer can easily find it.
2. For that you simply open the work package and copy its URL into the description of your PR (see screencast).  Compared
   to using the short string that OP suggests to you (e.g. ``OP#40`` for the WP with ID 40) the URL has the advantage
   that when you merge the PR later, you get to the WP more quickly to set the status to ``Done``.
3. Then take note of the number of measures and :ref:`log the costs <logging_costs>`.
4. Once your PR has been approved and you agree with the reviewer's changes, you are responsible for merging the PR,
   changing the WP's status to ``Done`` and, importantly, setting the ``Finish date`` to "Today".

.. figure:: img/linking_pr.gif
   :alt: Linking a Pull Request to a Work Package.
   :scale: 90%

   Linking a Pull Request to a Work Package. It doesn't matter that in this case the PR is already merged and the
   package marked as ``Done``.

.. _taking_on_a_review:

Taking on a review
------------------

.. figure:: img/op_review.png
     :alt: How to assign a work package as a reviewer
     :scale: 50%

Open the details of the corresponding work package.

1. Change the status from ``Needs review`` to ``Under review``.
2. If you hadn't been assigned already, add your name to the field "Reviewer".
3. Find the Pull Request in the GitHub pane.
4. Once the review is finished, approve the PR (unless you need to request changes) and
   :ref:`log the costs <logging_costs>`.
5. From here on, be attentive to any comments and discussion points raised by the ``Assignee`` and make sure to
   find consensus as efficiently as possible. It is a matter of teamwork to get the PR to a mergeable state and
   thus the work package to status ``Done``, invoiceable for both.

.. figure:: img/reviewing_pr.gif
   :alt: How to approve a PR
   :scale: 90%

   How to approve a PR (the screencast skips the actual review process which usually includes commits, comments, and
   metadata update).



.. _logging_costs:

Logging unit costs
==================

OpenProject computes the amount to be invoiced for each work package based on the number of measures.

1. Open the Work Package in question and find the number in the field "Measures". In case the status is ``Done``,
   please verify that the ``Finish date`` has been set upon merging the PR.
2. Open the context menu (``...`` or ``More``) and select ``Log unit costs``.
3. In the mask that opens,

   * under ``Cost type`` select the kind of service you provided (and thus the associated tariff).
   * enter the number of measures in the field ``Units``

4. Click "Save".

.. figure:: img/logging_costs.gif
   :alt: How to log unit costs
   :scale: 90%

   How to log unit costs. Here, the WPs in questions did not have a ``Finish date`` yet. For convenience, the respective
   column is added to the view but the date can also be entered in the WP's Overview.


Writing invoices
================

As you know already, you can invoice your finalized tasks at any given moment. Tasks are finalized when a Work Package's
``Assignee`` and ``Reviewer`` reach expert consensus on a set of annotations. Therefore, you can invoice tasks only
after the respective WP has reached the status ``Done``.

Starting from May 2022, all invoices should be based exclusively on cost reports generated by OpenProject.
Therefore it is important that you don't forget to :ref:`log your costs <logging_costs>` after performing a task
and that ``Assignee`` set the WP's ``Finish`` date to "Today" when setting the status to ``Done``.

.. _creating_cost_report:

Creating a cost report
----------------------

.. figure:: img/cost_report.gif
   :alt: How to generate a cost report.
   :scale: 90%

   How to generate a cost report.

#. Head to the "Time and Costs" menu and select the "Ready for invoicing" view.
#. Add the filter ``Finish date >= [day after your last invoice]``. If this is your first invoice, you can skip this
   step.
#. Click "Apply" and verify if the displayed unit costs indeed cover the finalized WPs you have undertaken. If a WP
   is not shown, at least one of these three things must be true:

   * You have not :ref:`logged your costs <logging_costs>`.
   * The WP has not reached the status ``Done`` yet.
   * The WP is missing its ``Finished date`` (or the date does not match your filter).

#. Click on "Export XLS" to export the Excel file to be attached to your invoice.
#. Use the different sheets contained in the Excel file to sum up measures and costs to come up with the items
   for the invoice (see below).

Writing an invoice
------------------

For the actual invoice you can use `our template <https://drive.switch.ch/index.php/s/lfNUOJ987AvFuvg>`__
or your own as long as it contains

* your address
* the current date
* an arbitrary invoice number
* one item per repository per type of service (e.g. one for "Creating new annotations" and one for "Reviewing new annotations")
* for each item, the accumulated number of bars and aggregated costs (e.g. "Creating new annotations | scarlatti_sonatas (321 bars) | 160.50 CHF")
* the total sum
* your bank details
* your signature

To compute the individual per-repository numbers easily, you can simply open the exported XLS (Excel) file:
It contains one sheet per cost type and from here it is simple to group measures and costs per repository using ``=SUM()``.

.. figure:: img/invoice_items.png
   :alt: How to compute grouped items for the invoice.
   :scale: 90%

   How to compute grouped items for the invoice. In this case, all WPs belong to the same corpus, so the item would be
   ``Creating new annotations | jc_bach_sonatas (825 bars) | 412.50 CHF``. If the sheet contains WPs from several repos,
   use ``=SUM()`` to group measures and costs.

