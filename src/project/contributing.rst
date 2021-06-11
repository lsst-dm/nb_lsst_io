########################
Contributing to the docs
########################

This documentation is open source.
Rubin Observatory welcomes contributions that make this documentation more useful and accurate.

Keep in mind that everyone participating in this project is expected to follow the Rubin Observatory LSST Data Management `Team Culture and Conduct Standards <https://developer.lsst.io/team/code-of-conduct.html>`__.

.. _contributing-issue:

Raising an issue
================

If you spot an issue with the documentation, the best thing to do is `raise a GitHub issue in the nb_lsst_io repo <https://github.com/lsst-dm/nb_lsst_io/issues/new>`__.
Include any relevant URLs with your issue description.

If you need help with the Notebook Aspect, in general, reach out on one of our :doc:`support channels first </getting-started/getting-help>`.

.. _contributing-pr:

Creating a pull request
=======================

You can contribute directly to the `nb_lsst_io <https://github.com/lsst-dm/nb_lsst_io>`__ repo by creating a pull request.
If you’re intending to make a substantial change, it’s a good idea to create a GitHub issue first with your proposal.
Rubin Observatory can’t accept contributions that don’t fit with our strategy and roadmap.

These sections can help you create a successful pull request:

-  :ref:`building-the-docs`
-  :ref:`doc-style-guide`

.. _building-the-docs:

Editing the docs locally
========================

Setting up the development environment
--------------------------------------

These are the basic steps to clone and build the docs:

.. code-block:: bash

   git clone https://github.com/lsst-dm/nb_lsst_io
   cd nb_lsst_io

Next, create a Python virtual environment (with venv_, for example).

Once you’ve done that, initialize the development environment:

.. code-block:: bash

   make init

This command installs tox_ and pre-commit_ hooks.
Tox enables you to build customized documentation sites for each RSP environemnt from a single source repository.
A consequence of using tox is that you don't install and run Sphinx directly, instead, tox handles build dependencies through its own Python virtual environments.
If you ever need to refresh those virtual environments (perhaps because you've updated your branch and the up-stream dependencies changed, you can re-initialize the environment by running ``make init`` in your shell again.

Running a documentation build
-----------------------------

Build documentation for all RSP environments by running tox:

.. code-block:: bash

   tox

By default, the tox command generates documentation site builds for each RSP environment in the ``_builds/html`` directory.
For example, ``_builds/html/idfprod/index.html`` is the homepage for the production IDF deployment and ``_builds/html/summit/index.html`` is the homepage for the summit deployment.

To build documentation for a limited number of environments, supply environment names to tox's ``-e`` option:

.. code-block:: bash

   tox -e sphinx-idfprod,sphinx-summit

To see a list of all available environments:

.. code-block:: bash

   tox -a

Although GitHub Actions performs link checks automatically for you, you can manually check links:

.. code-block:: bash

   tox -e linkcheck-idfprof

To force a complete rebuild of the documentation, you can clean-up the existing builds:

.. code-block:: bash

   make clean

Git commit hooks
----------------

To ensure that code quality is consistent, this project uses pre-commit_ hooks to lint the source repository before every commit.
These hooks are also in GitHub Actions, however, for the best development experience you will want to run these hooks during development.
By running ``make init``, these hooks are installed in your local repository clone.

If the hooks "fail," you will need to correct and re-add (``git add``) your changes before running ``git commit`` again.
Some hooks auto-correct the source, in which case you only need to re-add the changes.

.. _doc-style-guide:

Documentation style guide
=========================

This documentation is written in reStructuredText.
The `DM reStructuredText style guide <https://developer.lsst.io/restructuredtext/style.html>`__ can help you create effective reStructuredText.

Style and voice
---------------

This is user documentation, which is different from academic writing.
Here are some tips:

- Make sure that all of your writing is in the service of users.

- Write with the active voice and in the present tense as much as possible.

- Address the user directly (“you can…”).
  Never use “we” since that’s ambiguous.
  If “we” means “Rubin Observatory,” then name “Rubin Observatory.”
  If “we” means the user, then say “you.”
  Even in tutorials, don’t use “we” to refer to an imaginary writer assisting the user.

- Write simply, with short sentences and short paragraphs.
  Chunk information with headers.

- Write confidently and precisely, yet also casually.
  Contractions are good.

For further discussion about specific style issues, refer to the `Google Developer Documentation Style Guide <https://developers.google.com/style/>`_.

File names
----------

Always use hyphens to separate words in file names.
Don’t use underscores or spaces.

Prose formatting in plain text
------------------------------

DM's user documentation is written with soft wrapping, meaning that lines are as long as they need to be in the plain text file and the text editor is expected to handle wrapping.
Never hard wrap to an arbitrary line length.
Soft wrapping makes editing more approachable for more people (particularly those using the GitHub editor) and makes pull request line comments more useful.

More specifically, use `semantic line formatting <http://rhodesmill.org/brandon/2012/one-sentence-per-line/>`__.
Generally this means that each sentence should be its own line in the text file.

Titles and headings
-------------------

Use sentence case for headings (don’t use title case).
Capitalize proper nouns as usual.

Try not to use more than two levels of heading hierarchy.
Using more than two levels of hierarchy might suggest an information architecture issue.

Also keep in mind DM’s `reStructuredText heading styles <https://developer.lsst.io/restructuredtext/style.html#sections>`__.

Links
-----

Never use "here" as link text.
Instead, make the relevant noun or phrase the link.

Environment-specific documentation
----------------------------------

If the content is specific to an RSP environments, or is different across RSP environments, use the project's tools to write environment-specific content.
See :doc:`environment-specific-documentation`.
