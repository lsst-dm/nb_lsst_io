################################################
Using the LSST Science Pipelines in the terminal
################################################

The Notebook Aspect includes the `LSST Science Pipelines`_, making it a convenient way to work with LSST’s software.
The version of the LSST Science Pipelines that’s preinstalled corresponds to the :ref:`image you selected at log in <logging-in-image>`.

This page describes how to use the LSST Science Pipelines from the `JupyterLab terminal`_.

.. seealso::

   :doc:`science-pipelines-in-notebooks`.

Setting up the LSST Science Pipelines
=====================================

1. Open a `terminal`_.
   Click the **+** button in the `file browser`_ (or type :kbd:`command`\ -\ :kbd:`shift`\ -\ :kbd:`L`) and then click the **Terminal** icon.

2. Load the LSST environment:

   .. code-block:: bash

      source /opt/lsst/software/stack/loadLSST.bash

3. Set up LSST Science Pipelines packages:
   
   .. code-block:: bash
   
      setup lsst_distrib

Now you can run the Pipelines’s command-line tasks.
For example:

.. code-block:: bash

   processCcd.py -h

See `Setting up installed LSST Science Pipelines`_ in the LSST Science Pipelines documentation for more information about EUPS and the :command:`setup` command.

.. _`LSST Science Pipelines`: https://pipelines.lsst.io
.. _JupyterLab terminal:
.. _terminal: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html
.. _`file browser`: https://jupyterlab.readthedocs.io/en/latest/user/files.html
.. _`Setting up installed LSST Science Pipelines`: https://pipelines.lsst.io/install/setup.html
