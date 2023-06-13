Toxicpoller config
==================

The configuration of toxicpoller is done using the a configuration file. The configuration
file can be passed using the  ``-c`` flag to the ``toxicpoller`` command
or settings the environment variable ``TOXICPOLLER_SETTINGS``.

This file is a python file, so do what ever you want with it.

Config values
-------------

.. note::

   Although the config is done using a config file, the default
   configuration file created by ``toxicpoller create`` can use
   environment variables instead.


* ``PORT`` - The port for the server to listen. Defaults to `7777`.
  Environment variable: ``POLLER_PORT``

* ``USE_SSL`` - Defaults to False.
  Environment variable: ``POLLER_USE_SSL``. Possible values are `0` or `1`.

* ``CERTIFILE`` - Path for a certificate file.
  Environment variable: ``POLLER_CERTIFILE``

* ``KEYFILE`` - Path for a key file.
  Environment variable: ``POLLER_KEYFILE``

* ``ACCESS_TOKEN`` - An sha512 encrypted string used to authenticate an
  incomming request.
  Environment variable: ``POLLER_ENCRYPTED_TOKEN``.

.. note::

   You can create a new access token using the ``toxicpoller create_token``
   command. For more information use:

   .. code-block:: sh

       $ toxicpoller create_token --help

* ``ZK_SERVERS`` - A list of zookeeper servers.
  Environment variable: ``ZK_SERVERS``. Servers must be comma separated.

* ``ZK_KWARGS`` - Arguments passed to zookeeper client. Check the
  `aiozk docs <https://aiozk.readthedocs.io/en/latest/api.html#zkclient>`_.
