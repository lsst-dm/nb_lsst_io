#######################
Science Platform Tokens
#######################

The Notebook Aspect of the Rubin Observatory Science Platform provides access tokens for interacting with other services provided by the Science Platform.
An example is the TAP service provided by the API Aspect.
When interacting with authenticated services for within the Notebook Aspect you typically doesn't need to interact with the access tokens since the various clients are able to pick up the token from your user environment.
This access token can also be used outside the Notebook Aspect to access services from a local machine (for example, to access the TAP service from `TOPCAT`_).

This page will give you an introduction to the access token, where to find it, how to inspect it, and how to use it in an environment outside the Notebook Aspect.
Note that the access token has a finite lifetime and is refreshed on each login to the Notebook Aspect.

The access token
================

The access token is mounted in a known location in your home space.
To view it, you can simply look a the special file called ``~/.access_token``.
From within a `terminal`_ execute the following command.

.. code-block:: bash

   cat ~/.access_token

.. _`terminal`: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html

The environment includes a notebook, at ``~/notebooks/notebook-demo/token-info.ipynb``, that allows you to inspect a token.
Executing the two cells in the notebook will provide information about token creation time and lifetime among other things.
You will note from the above notebook that the token is also provided as the value of the environment variable ``ACCESS_TOKEN``, but the file version should be considered primary.

Using a token outside the Science Platform
==========================================

Following is a recipe for an example workflow that uses the access token taken from a JupyterLab session to access the Science Platform TAP service from a local computer using TOPCAT.
You can apply similar steps to other use cases.

1. `Open a terminal`_.

2. As in the last section, use the ``cat`` command to print out your access token.
   It should be quite a long string.

   .. code-block:: bash

      $ cat ~/.access_token
      eyJ0eXAiOiJKV1QiLCJhbGci...

3. Copy the entire token string to your clipboard.

4. On your local machine open up `TOPCAT`_.
   This will require having `Java`_ installed.

5. Once you have ``TOPCAT`` open, you will see a menu item called "VO".
   From that dropdown, select the entry that says "Table Access Protocol (TAP) Query".

  .. image:: VO_menu.png
     :alt: The VO menue

6. This will bring up a window with a list of available TAP services.
   We want to use a service with a known endpoint.
   Enter https://lsst-lsp-stable.ncsa.illinois.edu/api/tap in the box at the bottom of the page labeled "TAP URL".

   .. image:: tap_window.png
      :alt: The TAP service configuration window.

7. Clicking "Use Service" will bring up a username/password dialog.
   Paste the entire access token into the **User** field.
   Leave the password field blank.

   .. image:: username_password.png
      :alt: Username and password dialog.

8. If authentication is successful, the window will change to the TAP service window and information about the various tables in the service will appear in the left portion of the upper panes.
   If you select a table, you will see information about the columns in the table to the right of the table listing.

   For this example, I used the ``wise_00.allwise_p3as_mep`` table which provides photometry among other things.
   Make a query by entering the ADQL in the box at the bottom and click the "Run Query" button.

   The example query selects three magnitudes from a circular region on the sky.

   .. code-block:: SQL

      SELECT w1mpro_ep, w2mpro_ep, w3mpro_ep FROM wise_00.allwise_p3as_mep WHERE CONTAINS(POINT('ICRS', ra, decl), CIRCLE('ICRS', 192.85, 27.13, .2)) = 1

   .. image:: query_window.png
      :alt: Query window

9. Once the query returns, you can make plots like this color-color diagram.
   I made two more `synthetic columns`_ from the magnitude columns to plot.

   .. image:: color_color.png
      :alt: A color color plot from wise data.

.. _`Open a terminal`: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html

.. _`TOPCAT`: http://www.star.bris.ac.uk/~mbt/topcat/

.. _`Java`: https://www.java.com/en/

.. _`synthetic columns`: http://www.star.bris.ac.uk/~mbt/topcat/sun253/sun253.html#SyntheticColumnQueryWindow
