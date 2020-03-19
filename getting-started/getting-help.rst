############
Getting help
############

Documentation
=============

The Notebook Aspect is built on JupyterLab.
`Project Jupyter’s JupyterLab documentation <https://jupyterlab.readthedocs.io/en/latest/>`__ is the best way to learn about JupyterLab’s user interface and features.
The documentation you’re reading now focuses on LSST-specific aspects of the JupyterLab application.

For more information about the LSST Science Pipelines software included in the Notebook Aspect, see the `LSST Science Pipelines documentation <https://pipelines.lsst.io>`__.

LSST Community forum
====================

Use the `LSST Science Platform category <https://community.lsst.org/c/support/lsp>`__ on the LSST Community forum to get help from LSST staff and fellow users. 
You can even request new features, like preinstalled software, Python packages, and JupyterLab extensions.

Also, we’d love to learn about your work on the Notebook Aspect.
Feel free to share ideas and links to your own notebooks on GitHub.

Slack
=====

We encourage you to use the `LSST Community forum <https://community.lsst.org/c/support/lsp>`__ as much as possible, but on occasion you might need to work directly with an LSST engineer to debug an issue in real-time.
You can use the `#dm-lsp <https://lsstc.slack.com/channels/dm-lsp>`__ Slack channel for that.

Diagnostics
===========

If you are reporting an issue over Slack, one of the first questions you
will be asked is "what node are you running on?"  Determine that (inside
a Jupyterlab notebook, or if you prefer, from a python process in the
Terminal) with the following:
::

    from jupyterlabutils.notebook.utils import get_node
    get_node()

