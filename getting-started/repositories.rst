##################################
LSST-related notebook repositories
##################################

Many groups in LSST and the wider community are sharing Jupyter notebooks on GitHub.
These notebooks are excellent resources for learning about LSST data processing and can be inspiration for your own work.

Getting notebooks from GitHub
=============================

You can clone any Git repository from GitHub to work with its notebooks.
Be sure to clone into the :file:`~/notebooks/` directory (or a subdirectory of it) so that you can browse the repository with `JupyterLab’s file browser`_:

1. Open the `JupyterLab terminal`_.
2. ``cd ~/notebooks``
3. ``git clone https://github.com/{{org}}/{{repo}}``
4. Open notebooks from `JupyterLab’s file browser`_.

Notebook repositories
=====================

Take a look at these GitHub repositories to find interesting notebooks:

.. list-table::
   :widths: 30 60
   :header-rows: 1

   * - Repository
     - Description
   * - `lsst-sqre/notebook-demo`_
     - Preinstalled demo notebooks. See :doc:`notebook-demo`.
   * - `lsst-com/notebooks`_
     - A collection point for LSST Commissioning-related Jupyter notebooks.
   * - `LSSTScienceCollaborations/DMStackClub`_
     - Learning the LSST DM Stack, by writing Jupyter notebook tutorials.
   * - `lsst-dm/tutorial-lsst2017`_
     - This is the tutorial notebook from LSST Data Management’s onsite tutorials. Check out the ``answers`` branch to run the notebook all the way through — or try to code it yourself from ``master``.

.. _`lsst-sqre/notebook-demo`: https://github.com/lsst-sqre/notebook-demo
.. _`lsst-com/notebooks`: https://github.com/lsst-com/notebooks
.. _`LSSTScienceCollaborations/DMStackClub`: https://github.com/LSSTScienceCollaborations/DMStackClub
.. _`lsst-dm/tutorial-lsst2017`: https://github.com/lsst-dm/tutorial-lsst2017

Suggest a repository
====================

If you would like to share your own open-source repository of notebooks, feel free to `submit an issue`_ or pull request to this documentation.

.. _`JupyterLab terminal`: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html
.. _`JupyterLab’s file browser`: https://jupyterlab.readthedocs.io/en/latest/user/files.html
.. _`submit an issue`: https://github.com/lsst-dm/nb_lsst_io/issues/new
