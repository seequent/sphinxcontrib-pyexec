PyExec
======

A sphinx extension for running python code and displaying both the input and
output `sphinx documentation <http://www.sphinx-doc.org/>`_.

In the ReStructuredText file, use the `exec` environment.::

    .. exec::
        print 2 + 2

To output python code & the results in your documentation.

.. exec::
    print 2 + 2


Note that you need to include the :code:`print` statement for the output to be
shown. To see it in action, checkout the `Properties
documentation <http://propertiespy.readthedocs.io/>`_.

Setup
=====

PyExec is on `pip <https://pypi.python.org/pypi/sphinxcontrib-pyexec>`_::

    pip install sphinxcontrib-pyexec

or install from `source <https://github.com/3ptscience/sphinxcontrib-pyexec>`_::

    git clone https://github.com/3ptscience/sphinxcontrib-pyexec/

In the conf.py for your documentation, make sure you import pyexec::

    import pyexec

and add :code:`pyexec` to your extensions.

.. code:: python

    extensions = ['pyexec']

Developers
----------

View the source code on `github <https://github.com/3ptscience/sphinxcontrib-pyexec>`_

Based on
--------

- https://github.com/sphinx-doc/sphinx/blob/master/sphinx/directives/code.py
- http://stackoverflow.com/a/18143318/6086999





