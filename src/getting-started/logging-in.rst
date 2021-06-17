##########
Logging in
##########

This page explains how to log into the |rsp-at| and launch a JupyterLab server.

.. jinja:: rsp

   {% if vpn %}
   Before you get started, first make sure you have an account and have the VPN software installed (if necessary, given your network location).
   See :doc:`account` for details.
   {% else %}
   Before you get started, make sure you have an account.
   See :doc:`account` for details.
   {% endif %}

.. jinja:: rsp

   {% if phalanx in ("stable", "int") %}
   .. include:: logging-in.ldfvpnsteps.in.rst
   {% elif phalanx in ("idfint", "idfprod") %}
   .. include:: logging-in.idflogin.in.rst
   {% endif %}

.. _machine-setup:

Step 2: Select a machine image and size
=======================================

The **Server Options** page lets you select the machine image and size that you’ll work in.

.. _logging-in-image:

Image
-----

The machine images are based on `LSST Science Pipelines`_ Docker images, which are built on the CentOS 7 Linux operating system.

You can choose which version of the LSST Science Pipelines to run:

- Recommended
- Release (``rX.Y``)
- Weekly releases (``YYYY_WW``)
- Daily releases (``YYYY_MM_DD``)

The **Recommended** image is often the best choice because it has update-to-date versions of both the LSST Science Pipelines and supporting Jupyter and Python software, and is backed by additional testing.

For a scientific analysis work where reproducibility between Notebook Aspect sessions is important, you may wish to select a specific major or weekly release, and stick with that release for each log in.
To continue using a specific release, you may need to select it from the **historical image** drop down.

For developing with the `LSST Science Pipelines`_, we recommend using the latest daily release to ensure your work is compatible with current versions of Science Pipelines packages.
See :doc:`/science-pipelines/development-tutorial` for more information.

Options: size
-------------

You can also choose your machine size from the **Server Options** page.
Since the |rsp-at| is a shared resource, try to use the smallest machine possible so that resources are available to other users.

For most light-weight tasks, such as editing notebooks or analyzing small datasets, small-scale analyses, the **Small** images will be just fine.

For running data processing tasks with the `LSST Science Pipelines`_, choose the **Medium** or **Large** images to ensure that datasets fit in RAM.

Options: Enable debug logs
--------------------------

Only select this option if requested by Rubin Observatory staff.

Options: Clear the .local directory
-----------------------------------

Only select this option if you are having difficulties starting the Notebook Aspect because Python packages or other software that you installed yourself are now incompatible with the :ref:`image <logging-in-image>` that you want to launch.

Start the notebook aspect
-------------------------

Click **Start** and to launch into the Notebook Aspect.

Next steps
==========

-  Learn more about the `JupyterLab interface <https://jupyterlab.readthedocs.io/en/latest/>`_ (external Project Jupyter documentation).
-  :doc:`Explore demo notebooks <notebook-demo>` featuring LSST data analysis.
