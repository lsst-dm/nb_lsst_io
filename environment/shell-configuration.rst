######################
Configuring your shell
######################

The `JupyterLab Terminal`_ runs the ``bash`` shell.
You can configure your ``bash`` environment (including environment variables, aliases, and functions) by editing the :file:`~/.bashrc` file.
In the current version of JupyterLab, the shell in the terminal is not spawned as a login shell.
This means :file:`~/.bash_profile` is not sourced at startup time.
See `this issue`_ for discussion of why this is.

.. note::

   Environment variables that you set in :file:`~/.bashrc` are not available from notebooks.
   You can add such environment variables to you :file:`~/notebooks/.user_setups` file, see :ref:`lsst-kernel-user-setups-envvars`.

.. _`JupyterLab Terminal`: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html
.. _`this issue`: https://github.com/jupyterlab/jupyterlab/issues/3094
