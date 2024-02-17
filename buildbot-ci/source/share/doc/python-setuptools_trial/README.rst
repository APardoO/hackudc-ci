
setuptools_trial
================

About
-----

This is a plugin for setuptools that integrates Twisted trial.  Once
installed, "python ./setup.py trial" will run the package's unit tests
using Twisted trial.  The package can also optionally be configured so
that "python ./setup.py test" will use Twisted trial instead of pyunit
a.k.a. unittest.


Installation
------------

With ``pip``:

.. code-block:: bash

   pip install setuptools_trial

or with ``easy_install``:

.. code-block:: bash

   easy_install setuptools_trial

Alternative manual installation:

.. code-block:: bash

    tar -zxvf setuptools_trial-X.Y.Z.tar.gz
    cd setuptools_trial-X.Y.Z
    python setup.py install

Where ``X.Y.Z`` is a version number.

Alternative to make a specific package use setuptools_trial without
installing setuptools_trial into the system:

Put ``setup_requires=['setuptools_trial']`` in the call to ``setup()`` in
the package's ``setup.py`` file.


Usage
-----

Once setuptools_trial is installed (either into the system or just for
the current package), then ``python ./setup.py trial`` will run trial on
the package.

You can then make ``python ./setup.py test`` use trial instead of pyunit
(unittest) by adding the following stanza to your project's ``setup.cfg``:

.. code-block:: text

    [aliases]
    test = trial

See also the output of ``python ./setup.py trial --help`` for usage
options.


References
----------

To learn more about Python modules packaging visit
https://www.pypa.io/en/latest/.

Thanks to Yannick Gingras for providing the prototype for this
``README.rst``.
