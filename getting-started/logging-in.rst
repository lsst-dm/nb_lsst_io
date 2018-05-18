##########
Logging in
##########

You need NCSA Kerberos credentials to log into the LSST Science Platform Notebook Aspect.
Members of LSST receive an NCSA Kerberos account as part of your onboarding.
If haven’t onboarded into LSST yet, talk to your T/CAM or supervisor (see `DM Onboarding <https://developer.lsst.io/team/onboarding.html>`__).

Step 1: Use the NCSA VPN with Cisco AnyConnect
==============================================

As a development deployment, the Notebook Aspect is not yet directly accessible from the internet.
For now, you’ll use NCSA’s VPN, through Cisco AnyConnect, to log into the Notebook Aspect.

.. tip::

   If you are on an approved network, like NOAO, you can skip the VPN and log in directly.

To use the NCSA VPN, open `vpn.ncsa.illinois.edu <https://vpn.ncsa.illinois.edu>`__ in your web browser.
Select ``ncsa-vpn-default`` from the **GROUP** menu and enter your NCSA Kerberos username and password.
The page installs and starts the Cisco AnyConnect application for you.

.. tip::

   In the future, you can open the AnyConnect application and enter ``vpn.ncsa.illinois.edu`` to get connected.
   There's no need to go back to the `vpn.ncsa.illinois.edu <https://vpn.ncsa.illinois.edu>`__ website.

Step 2: Log in
==============

Open `lsst-lspdev.ncsa.illinois.edu/nb <https://lsst-lspdev.ncsa.illinois.edu/nb>`__ in your web browser.
Click the **Sign in with CILogon** button, then enter your NCSA Kerberos credentials on the NCSA CILogon page.

Once authentication is complete, you’ll be redirected to the Notebook Aspect’s Spawner page.

Step 3: Select a machine image and size
=======================================

The **Spawner options** page lets you select the machine image and size that you’ll work in.

.. _logging-in-image:

Image
-----

The machine images are based on `LSST Science Pipelines`_ Docker images, which are built on the CentOS 7 Linux operating system.

You can choose which version of the LSST Science Pipelines to run:

-  Daily releases (YYYY-MM-DD)
-  Weekly releases (YYYY-WW)
-  Supported releases

For scientific analyses, we recommend a supported or weekly release.
If you are developing with the `LSST Science Pipelines`_, opting for the latest daily release might make sense.

Only the most recent releases are shown by default.
You can select older releases from the image tag drop-down menu.

Size
----

You can also choose your machine size from the Spawner options page. Try to use the smallest machine possible so that resources are available to other users.

For small-scale analyses, the **Tiny** and **Small** images will be just fine.

For running image processing tasks with the `LSST Science Pipelines`_, choose the **Medium** or **Large** images to ensure that datasets fit in RAM.

Next, click **Spawn** and you’ll be launched into the Notebook Aspect.

Next steps
==========

-  `Learn more about the JupyterLab interface <https://jupyterlab.readthedocs.io/en/latest/>`_ (Project Jupyter documentation)
-  Explore demo notebooks featuring LSST data analysis.

.. FIXME add link.

.. _LSST Science Pipelines: https://pipelines.lsst.io
