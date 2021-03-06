===========
Local CNAME
===========

.. image:: https://img.shields.io/pypi/v/local-cname.svg
   :target: https://pypi.python.org/pypi/local-cname
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/local-cname.svg
   :target: https://pypi.python.org/pypi/local-cname
   :alt: Development Status

.. image:: https://img.shields.io/pypi/pyversions/local-cname.svg
   :target: https://pypi.python.org/pypi/local-cname
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/l/local-cname.svg
   :target: https://github.com/hjacobs/local-cname/blob/master/LICENSE
   :alt: License

This is a little helper script to emulate a local CNAME DNS by writing to ``/etc/hosts``.
DNS changes (e.g. to rollout new services) can be tested by overwriting DNS names in the local ``/etc/hosts`` file.
The hosts file only supports IP addresses thus making it cumbersome to emulate a DNS ``CNAME`` without a local DNS server/proxy.
The ``local-cname`` is a very small script to automatically lookup DNS names and write IP addresses to the hosts file.
It is self-contained and restores your local ``/etc/hosts`` file on exit (press CTRL+C).

Installation:

.. code-block:: bash

    $ sudo pip install -U local-cnames

Usage:

.. code-block:: bash

    $ cat /etc/cnames
    google.com=duckduckgo.com
    
    $ sudo local-cnames
      # press CTRL+C to cancel and restore your old /etc/hosts

Example:

.. code-block:: bash

    $ cat /etc/cnames
    google.com=duckduckgo.com

    $ sudo local-cnames
    $ ping google.com


