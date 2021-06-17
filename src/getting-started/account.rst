##################
Getting an account
##################

.. jinja:: rsp

   {% if phalanx == "idfprod" %}
   You need an account to use the |rsp-at|.
   Accounts are available to DP0.1 delegates.
   To learn more about DP0.1 and how to become a delegate and receive a Rubin Science Platform account, visit the `DP0.1 Guide`_.
   {% else %}
   .. important::

      This |rsp-at| is for internal Rubin Observatory engineering and testing.
      If you are a DP0.1 delegate, switch to the main Notebook Aspect documentation at https://nb.lsst.io/.

   {% endif %}

   {% if phalanx in ("idfdev", "idfint") %}
   To access this Notebook Aspect, you need to be a member of a specific GitHub team:

   {% for t in github_teams %}
   - `{{ t }} <https://github.com/orgs/{{ t.split("/")[0] }}/teams/{{ t.split("/")[1] }}/members>`__
   {% endfor %}

   If you aren't a member of an appropriate GitHub team, send a message to |slack-rsp-team| on Slack.

   {% elif phalanx in ("stable", "int", "nts") %}
   You need NCSA Kerberos credentials to log into the |rsp-at|.
   Members of Rubin Observatory receive an NCSA Kerberos account as part of your `onboarding <https://developer.lsst.io/team/onboarding.html>`__.
   If you haven’t onboarded yet, talk to your T/CAM or sponsor.

   {% elif phalanx == "tucsonteststand" %}
   To learn how to get an account, please contact the team at |slack-com-square| on Slack.

   {% elif phalanx in ("base", "summit") %}
   To learn how to get an account, please contact the team at |slack-com-square| on Slack.

   {% endif %}

   {% if vpn %}

   .. _vpn-setup:

   Installing and configuring the VPN
   ==================================

   Unless you are connecting to the |rsp-at| from a pre-authorized, internal, network, you need to use a VPN.

   {% if phalanx in ("stable", "int", "nts") %}
   To set up the NCSA VPN, you to:

   - Install the `Cisco AnyConnect client`_ on your computer.
   - Install and enroll in `NCSA DUO`_ on your iPhone or Android device.

   Follow the documentation `Connecting to the VPN System`_ (external link) for details on using Cisco AnyConnect VPN client and `NCSA DUO`_ for two-factor authentication.

   {% elif phalanx in ("base", "summit") %}
   For information about VPN for base and summit networks, please contact the team at |slack-chile-it| on Slack.

   {% elif phalanx == "tucsonteststand" %}
   For information about the NOIRLab VPN, please contact the team at |slack-rubin-it| on Slack.
   {% endif %}
   {% endif %}

Once you account is set up, :doc:`your next step is to Log in <logging-in>`.
