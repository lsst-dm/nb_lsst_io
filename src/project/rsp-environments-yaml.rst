#######################################################################
rsp-environments.yaml: metadata about the science platform environments
#######################################################################

Source data about the RSP environments that can be used to :doc:`write environment-specific documentation <environment-specific-documentation>` is maintained in a file called ``rsp-environments.yaml`` at the root of this documentation repository.
This page describes that file, and how to maintain it.

File layout and schema
======================

The ``rsp-environments.yaml`` file consists of a mapping of RSP environments.
These keys closely correspond to RSP environments in the `Phalanx deployment repository`_, though they are made to conform to python variable name syntax since they are used as `tags for the Sphinx builds <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html?highlight=tags#including-content-based-on-tags>`__ (see the ``tox.ini`` file).
The value for each environment is a mapping that describes metadata about the environment.

.. jsonschema:: ../../rsp-environments.schema.json

Linting and data maintenance
============================

The ``rsplint.py`` script lints the contents of ``rsp-environments.yaml`` using the `Phalanx deployment repository`_ as a source of truth.
In turn, ``rsplint.py`` is run as a Git hook through the pre-commit_ framework so that ``rsp-environments.yaml`` is validated regularly during documentation builds:

- whenever you run ``pre-commit run --all-files`` on the command line
- whenever you commit a change to ``rsp-environments.yaml``
- during any build in GitHub Actions

If ``rsplint.py``, through pre-commit_, detects a mismatch between values in ``rsp-environments.yaml`` and the `Phalanx deployment repository`_, you will need to update ``rsp-environments.yaml``.

Adding or removing an environment
=================================

If you are adding a new RSP environment to the documentation build, or removing an existing environment there are a number of files to consider:

- Update ``rsp-environments.yaml``
- Update ``tox.ini``
- Update GitHub Actions, particularly ``.github/workflows/ci.yaml``
- Update any ``jinja`` directives in the source content
