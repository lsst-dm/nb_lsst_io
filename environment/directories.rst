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

The :file:`$HOME` directory is also the base directory for the `JupyterLab file browser`_.
Notebooks and other files need to be inside the :file:`$HOME` directory (or a subdirectory) for you to see and open them from the `file browser`_.

Currently there is a 100 GB quota for :file:`$HOME`.
There is also a limit of 102400 files and subdirectories (inodes) within :file:`$HOME`.
You can use :ref:`filesystem-project` for larger datasets.

.. note::

   If you also have an account on `lsst-dev <https://developer.lsst.io/services/lsst-dev.html>`_,
   you can access your Notebook Aspect home directory via :file:`$HOME/jhome/` from lsst-dev.

Preinstalled subdirectories
---------------------------

Within the :file:`$HOME` directory a number of directories are currently pre-created for new users.

The ~/notebooks directory
^^^^^^^^^^^^^^^^^^^^^^^^^

The :file:`~/notebooks` directory is intended as the top of a subtree within which you can organize your personal notebooks.
Within this directory, two items are pre-created:

- A clone of the `lsst-sqre/notebook-demo`_ repository is created from GitHub at :file:`~/notebooks/notebook-demo`. The ``prod`` branch of this repository is regularly updated from GitHub in this clone.  See the :doc:`../getting-started/notebook-demo` page to learn more.
- You can use the :ref:`~/notebooks/.user_setups <lsst-kernel-user-setups>` file to configure the environment your notebooks run in.

The ~/DATA directory
^^^^^^^^^^^^^^^^^^^^

The :file:`~/DATA` directory is pre-created, empty, as a place for tutorial notebooks to load input datasets.
If you delete it, some notebooks will attempt to re-create it, while others may fail.

The ~/WORK directory
^^^^^^^^^^^^^^^^^^^^

The :file:`~/WORK` directory is pre-created, empty, as a place for some tutorial notebooks to write outputs (e.g., "rerun" directories).
If you delete it, these notebooks may fail.

The ~/dask directory
^^^^^^^^^^^^^^^^^^^^

The :file:`~/dask` directory is pre-created and holds an automatically updated `Dask <https://dask.org/>`_ configuration file, :file:`~/dask/dask_worker.yml`.
This file is recreated on each login, populated with a template that builds dask nodes of the appropriate size and with the appropriate disk mounts.

The ~/idleculler directory
^^^^^^^^^^^^^^^^^^^^^^^^^^

The :file:`~/idleculler` directory is used for logfile output from the process that watches for idle sessions.
This file, :file:`culler.output`, may be deleted when it begins to take up a lot of space; it will be automatically recreated.

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
.. _`lsst-sqre/notebook-demo`: https://github.com/lsst-sqre/notebook-demo
