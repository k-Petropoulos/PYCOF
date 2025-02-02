###
FAQ
###

*****************************************************
I have an error when using a function, what can I do?
*****************************************************

If you encounter an unexpected error (coming from the source code), we recommend to first check if you are using the latest version of PYCOF

.. code::

    pip3 show pycof

If the version is not the latest one, please upgrade it.

.. code::

    pip3 install --upgrade pycof

If you still encounter the same error with the most recent version, please raise an `issue`_.


----

*****************************************************************************
What if I change an argument in the SQL query and run with :obj:`cache=True`?
*****************************************************************************

See `SQL FAQ 1 <../sql/sql.html#what-if-i-change-an-argument-in-the-sql-query-and-run-with-cache-true>`_.


----

*************************************
How to use different credential sets?
*************************************

See `SQL FAQ 2 <../sql/sql.html#how-to-use-different-credential-sets>`_.



****************************************
How to execute a query from an SQL file?
****************************************

See `SQL FAQ 3 <../sql/sql.html#how-to-execute-a-query-from-an-sql-file>`_.



*********************************************
How can I load a .json file as a dictionnary?
*********************************************

The function :py:meth:`~pycof.f_read` allows to read different formats.
By default it will load as and :obj:`pandas.DataFrame` but you can provide :obj:`engine='json'` to load as :obj:`dict`.

.. code:: python

    import pycof as pc

    pc.f_read('/path/to/file.json', engine='json')










.. _git: https://github.com/florianfelice/PYCOF/
.. _issue: https://github.com/florianfelice/PYCOF/issues

.. _statinf: https://www.florianfelice.com/statinf
