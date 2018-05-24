######################
The Python environment
######################

The Notebook Aspect includes Python 3.6.
This page describes the Python packages that are preinstalled, and how to install additional packages that enable your work.

Preinstalled Python packages
============================

-  astropy
-  astroquery
-  bokeh
-  cloudpickle
-  datashader (master)
-  healpy
-  holoviews (master)
-  ipywidgets
-  ipykernel
-  nbdime
-  nbval
-  numpy
-  rise
-  scipy
-  matplotlib
-  pandas
-  parambokeh (master)
-  pipenv
-  pyarrow
-  pypandoc
-  virtualenv
-  virtualenvwrapper

Installing Python packages
==========================

You can install additional Python packages with :command:`pip`:

1. `Open a terminal`_.

2. Install the package with :command:`pip`:
   
   .. code-block:: bash
   
      pip install --user {{package name}}
      
   .. note::
   
      The ``--user`` flag is necessary because you don’t have root access.

Packages that you install with ``pip install --user ...`` are available from **both** the LSST and regular Python 3 kernels.

.. caution::

   The Python packages that you install can, on occasion, be incompatible with the preinstalled packages from the Notebook Aspect’s image when you log in.
   For example, you might have installed a package, but the Notebook Aspect includes a newer version that is required for compatibility.

   The best way to resolve this is by deleting the version of the package you installed.
   You can find your installed packages in the :file:`~/.local/lib/python3.6/site-packages` directory.

   Sometimes the Notebook Aspect will not start at all because of a package incompatibility.
   To resolve this, select the **Clear local** option on the Spawner options page when you :doc:`log in </getting-started/logging-in>`.
   This moves the entire :file:`~/.local` directory aside, enabling you to successfully log in.

.. _`Open a terminal`: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html
