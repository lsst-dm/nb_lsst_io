######################
Filesystem directories
######################

This page describes the filesystem directories available in the Notebook Aspect.

.. list-table::
   :header-rows: 1

   * - Directory
     - Private
     - Persistent
     - Writeable
   * - :ref:`filesystem-home`
     - ✅
     - ✅
     - ✅
   * - :ref:`filesystem-notebooks`
     - ✅
     - ✅
     - ✅
   * - :ref:`filesystem-datasets`
     -
     - ✅
     -
   * - :ref:`filesystem-project`
     -
     - ✅
     - ✅
   * - :ref:`filesystem-scratch`
     -
     -
     - ✅

.. _filesystem-home:

$HOME
=====

Your home directory is just that.
It’s backed by essentially the same storage as your home directory on `lsst-dev`_ in the LSST Data Facility.
In fact, your :file:`$HOME` directory in the Notebook Aspect *is* the :file:`$HOME/jhome/` directory on `lsst-dev <https://developer.lsst.io/services/lsst-dev.html>`_. 

Currently there is a 100 GB quota for :file:`$HOME`.
There is also a limit of 102400 files and subdirectories (inodes) within :file:`$HOME`.
You can use :ref:`filesystem-project` for larger datasets.

.. _filesystem-notebooks:

~/notebooks
===========

The :file:`~/notebooks` directory inside your :file:`$HOME` directory is the base directory for the `JupyterLab file browser`_.
Notebooks and other files need to be inside the :file:`~/notebooks` directory for you to open them from the `file browser`_.

The :file:`~/notebooks` directory is created for you.

.. _filesystem-datasets:

/datasets
=========

This is a **read-only** directory containing curated Butler data repositories.
Each dataset has a README file describing its contents and intended applications.
See `Common Dataset Organization and Policy`_ in the DM Developer Guide for more information about these datasets.

.. _filesystem-project:

/project
========

This directory is for shared, uncurated, persistent data.
There is no disaster recovery, nor is there an enforced quota or purge policy.

.. _filesystem-scratch:

/scratch
========

This directory is for **completely transient** data.
There is no disaster recovery or quota, but there is a purge cycle.

.. _`lsst-dev`: https://developer.lsst.io/services/lsst-dev.html
.. _`data use and protection policies`: https://developer.lsst.io/services/data_protection.html
.. _`Common Dataset Organization and Policy`: https://developer.lsst.io/services/datasets.html
.. _`JupyterLab file browser`:
.. _`file browser`: https://jupyterlab.readthedocs.io/en/latest/user/files.html
