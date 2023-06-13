:tocdepth: 1

Toxicpoller: Fetches changes on remote repositories
===================================================

Toxicpoller is a server that fetches changes in the remote repositories
and informs the master.

Install
-------

To install it use pip:

.. code-block:: sh

   $ pip install toxicpoller



Setup & config
--------------

Before running the program you must create an environment for toxicpoller.
To do so use:

.. code-block:: sh

   $ toxicpoller create ~/poller-env

This is going to create a ``~/poller-env`` directory with a ``toxicpoller.conf``
file in it. This file is used to configure toxicpoller.

Check the configuration instructions for details

.. toctree::
   :maxdepth: 1

   config


Run the server
--------------

When the configuration is done you can run the server with:

.. code-block:: sh

   $ toxicpoller start ~/poller-env


For all options for the toxicpoller command execute

.. code-block:: sh

   $ toxicpoller --help


Poller server API
==================

Check the api documentation for details

.. toctree::
   :maxdepth: 1

   poller_api.rst


CHANGELOG
---------

.. toctree::
   :maxdepth: 1

   CHANGELOG
