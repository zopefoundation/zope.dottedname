Dotted Name Resolution
======================

:mod:`zope.dottedname` provides one function,
:func:`~zope.dottedname.resolve.resolve`, that resolves strings containing
dotted names into the appropriate Python object.

Dotted names are resolved by importing modules and by getting
attributes from imported modules. Names may be relative, provided the
module they are relative to is supplied.

Here are some examples of importing absolute names:

.. doctest::

   >>> from zope.dottedname.resolve import resolve

   >>> resolve('unittest')
   <module 'unittest' from '...'>

   >>> resolve('datetime.datetime')(2015, 2, 2, 18, 59, 27)
   datetime.datetime(2015, 2, 2, 18, 59, 27)

   >>> resolve('os.path.basename')
   <function basename at ...>

   >>> resolve('non existent module')
   Traceback (most recent call last):
   ...
   ModuleNotFoundError: No module named non existent module

   >>> resolve('__doc__')
   Traceback (most recent call last):
   ...
   ModuleNotFoundError: No module named __doc__

   >>> resolve('logging.foo')
   Traceback (most recent call last):
   ...
   ModuleNotFoundError: No module named ...foo

   >>> resolve('os.path.split').__name__
   'split'

Here are some examples of importing relative names:

.. doctest::

   >>> resolve('.split', 'os.path')
   <function split at ...>

   >>> resolve('..system', 'os.path')
   <built-in function system>

   >>> resolve('...datetime', 'os.path')
   <module 'datetime' ...>

NB: When relative names are imported, a module the name is relative to
**must** be supplied:

.. doctest::

   >>> resolve('.split').__name__
   Traceback (most recent call last):
   ...
   ValueError: relative name without base module
