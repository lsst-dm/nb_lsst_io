##########################################
Writing environment-specific documentation
##########################################

The Notebook Aspect is deployed in multiple science platform environments as defined in the `Phalanx deployment repository`_.
A separate version of this documentation is built for each science platform environment and deployed using LSST the Docs's editions feature.
The documentation corresponding to the primary, public-facing science platform is always deployed as the main edition at the root URL (https://nb.lsst.io).
Other editions are available from https://nb.lsst.io/v and the Science Platform homepages of each environment also link directly to these editions.

This page describes supported approaches for writing documentation that is different for each environment.
Each section covers an approach that handles different levels of content customization:

- :ref:`envdocs-substitutions` to customize words and sentences
- :ref:`envdocs-jinja` to customize paragraphs
- :ref:`envdocs-jinja-includes` to customize large portions of a page

Besides this documentation, you can also learn from the existing documentation.
The homepage (``index.rst``) and log-in (``/getting-started/logging-in.rst``) pages demonstrate all the techniques described here.

Information about the RSP environments is maintained in a file named ``rsp-environments.yaml`` in the `documentation repository <https://github.com/lsst-dm/nb_lsst_io>`_.
To learn more about this data, how it is maintained, and how to add additional metadata, see :doc:`rsp-environments-yaml`.

.. _envdocs-substitutions:

Using reStructuredText substitutions
====================================

For inline content (words or sentences) that changes from one environment to another, such as the name of the science platform environment or a link to the science platform, use `reStructuredText substitutions <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#substitutions>`__.
You can find these substitutions defined inside the ``rst_epilog``, inside the ``conf.py`` file at the root of the ``nb_lsst_io`` repository, and particularly within the ``rst_epilog.jinja`` templated file.
Some of the key substitutions include:

.. list-table:: Available substitutions
   :header-rows: 1

   * - Syntax
     - Example
   * - ``|rsp|``
     - |rsp|
   * - ``|rsp-at|``
     - |rsp-at|
   * - ``|rsp-env|``
     - |rsp-env|
   * - ``|rsp-env-link|``
     - |rsp-env-link|
   * - ``|log-in|``
     - |log-in|
   * - ``|open-nb-aspect|``
     - |open-nb-aspect|

The ``rst_epilog.jinja`` file is templated using Jinja.
The context variables are based on the :doc:`rsp-environments.yaml file <rsp-environments-yaml>`.

.. _envdocs-jinja:

Using Jinja templating
======================

If different environments require alternative versions of whole paragraphs, use the ``jinja`` directive, available through sphinx-jinja_, to display different content based on Jinja_ control-flow syntax:

.. code-block:: rst

   .. jinja:: rsp

      {% if primary %}
      This paragraph appears in the documentation for the
      primary science platform environment.

      {% elif phalanx in ("base", "summit") %}
      This paragraph appears in documentation for the base
      and summit.

      {% elif phalanx == "stable" %}
      This paragraph appears only for the LDF "stable"
      environment.

      {% endif %}

The argument to the ``jinja`` directive is always ``rsp``.
This setting makes all of the fields for a specific RSP environment from the :doc:`rsp-environments.yaml file <rsp-environments-yaml>` available in the Jinja environment.
The example above uses the ``primary`` and ``phalanx`` fields (the ``phalanx`` field refers to the name of the environment in Phalanx_).

When using the ``jinja`` directive, as with any Sphinx directive, ensure that content is indented consistently with respect to the scope of the directive, as shown above.

.. _envdocs-jinja-includes:

Using Jinja templating with source file includes (\*.in.rst)
============================================================

The previous approach works well for templating paragraphs, however it is inconvenient to write inside a Jinja directive (within the scope of Jinja syntax, at that).
To customize large portions of text, you can use the include statement in combination with Jinja:

.. code-block:: rst

   .. jinja:: rsp

      {% if primary %}
      .. include:: the-page.primary.in.rst

      {% else %}
      .. include:: the-page.notprimary.in.rst

      {% endif %}

This code sample inserts content from the included source files, either ``the-page.primary.in.rst`` or ``the-page.notprimary.in.rst``.
Those included files are in the familiar reStructuredText syntax (you shouldn't need to use further Jinja syntax within them, though can certainly use :ref:`substititions <envdocs-substitutions>`).

The included files **must** have a ``.in.rst`` suffix so that the Sphinx build won't incorporate those files as separate pages.
Our further convention is to prefix the name with the root name of the page, followed by a description of the environment or context where the content applies.

This approach is used in the ``/getting-started/logging-in.rst`` page to show completely different sections depending on whether the log-in process involves a VPN or not.

.. _envdocs-only:

Avoiding the "only" directive
=============================

Besides the techniques described above, Sphinx also provides an `only <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html?highlight=only#directive-only>`__ directive to control content based on Sphinx build tags.
As part of the tox-based build, the environment name is available as a tag:

.. code-block:: rst

   .. only:: idfprod

      This sentence appears only for the ``idfprod`` build of the docs.

You should avoid this approach, however, and use one of the earlier techniques instead, because the ``only`` directive does not work well with reStructuredText labels and the built-in Sphinx search.
