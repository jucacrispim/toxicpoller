Secrets API
===========

The uses the `tpp <https://docs.poraodojuca.dev/toxiccore/tpp.html>`_
and has the following actions:

Add or update
--------------

The action ``add-or-update-secret`` creates a new or upates the value of a secret.

The following body params are mandatory:

-  ``owner`` - An ObjectId identificating the owner of the secret
- ``key`` - A key to identify the secret
- ``value`` - The value of the secret. Will be encrypted before stored in database.


Get secrets
-----------

The action ``get-secrets`` returns a list with all secrets owned by a
(some) user(s).

The following body params are mandatory:

- ``owners`` - A list of ObjectIds of secret owners


Remove secret
-------------

The action ``remove-secret`` removes a secret from the database.

The following body params are mandatory:

-  ``owner`` - An ObjectId to identificate the owner of the secret
- ``key`` - The key of the secret

Remove all
----------

The action ``remove-all`` removes all secrets of a owner.

The following body params are mandatory:

-  ``owner`` - An ObjectId to identificate the owner of the secrets
