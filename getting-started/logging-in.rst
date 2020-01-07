##########
Logging in
##########

You need NCSA Kerberos credentials to log into the LSST Science Platform Notebook Aspect.
Members of LSST receive an NCSA Kerberos account as part of your `onboarding <https://developer.lsst.io/team/onboarding.html>`__.
If you haven’t onboarded into LSST yet, talk to your T/CAM or sponsor.

If this is your first time logging in, you'll need to take a moment to set up a VPN:

- :ref:`vpn-setup`

Once you have a working VPN, you can log into the LSST Science Platform Notebook Aspect itself:

- :ref:`vpn-login`
- :ref:`nb-login`
- :ref:`machine-setup`

.. _vpn-setup:

Install and configure the NCSA VPN (Cisco AnyConnect and NCSA DUO)
==================================================================

To use the notebook aspect from non-approved networks, you need to use the NCSA VPN.
This requires you to:

- Install the `Cisco AnyConnect client`_ on your computer.
- Install and enroll in `NCSA DUO`_ on your iPhone or Android device.

Follow the documentation `Connecting to the VPN System`_ (external link) for details on using Cisco AnyConnect VPN client and `NCSA DUO`_ for two-factor authentication.

.. _vpn-login:

Step 1: Log into the NCSA VPN
=============================

If you aren't on an approved network, first activate the NCSA VPN.
Follow the steps a `Connecting to the VPN System`_ (external link) for details on how to do thiis.

If you've forgotten your password, you can reset it by visiting https://identity.ncsa.illinois.edu/reset.

.. _nb-login:

Step 2: Log in
==============

Open `lsst-lsp-stable.ncsa.illinois.edu/nb <https://lsst-lsp-stable.ncsa.illinois.edu/nb>`__ in your web browser.
Click the **Sign in with CILogon** button.
This will take you to a page where you can choose an identity provider.
You must choose NCSA as the provider the first time you log in (type NCSA in the search box to find it).
Once you have chosen NCSA as the identity provider, click the **Log On** button and you will be taken to a page where you can enter your NCSA Kerberos credentials.

You can add identity providers using the identity management page at https://identity.lsst.org/manage.
Scroll to the bottom and click the **Add Identity** button.
You will be asked to authenticate to the external identity provider after which you can use those credentials to log into the LSP.

If you've forgotten your password, you can reset it at https://identity.ncsa.illinois.edu/reset.

Once authentication is complete, you’ll be redirected to the Notebook Aspect’s Spawner page.

.. _machine-setup:

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

-  Learn more about the `JupyterLab interface <https://jupyterlab.readthedocs.io/en/latest/>`_ (external Project Jupyter documentation).
-  :doc:`Explore demo notebooks <notebook-demo>` featuring LSST data analysis.

.. _LSST Science Pipelines: https://pipelines.lsst.io
.. _NCSA DUO: https://wiki.ncsa.illinois.edu/display/cybersec/Duo+at+NCSA
.. _Connecting to the VPN System: https://wiki.ncsa.illinois.edu/display/cybersec/Virtual+Private+Network+%28VPN%29+Service#VirtualPrivateNetwork(VPN)Service-ConnectingtotheVPNSystem
.. _`Cisco AnyConnect client`: https://wiki.ncsa.illinois.edu/display/cybersec/Virtual+Private+Network+%28VPN%29+Service#VirtualPrivateNetwork(VPN)Service-CiscoAnyConnectVPNClientDownloads
