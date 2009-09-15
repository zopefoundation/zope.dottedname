======================
Dotted Name Resolution
======================

The ``zope.dottedname`` module provides one function, ``resolve`` that
resolves strings containing dotted names into the appropriate python
object.

Dotted names are resolved by importing modules and by getting
attributes from imported modules. Names may be relative, provided the
module they are relative to is supplied.

Here are some examples of importing absolute names::

  >>> from zope.dottedname.resolve import resolve

  >>> resolve('unittest')
  <module 'unittest' from '...'>

  >>> resolve('datetime.datetime')
  <type 'datetime.datetime'>

  >>> resolve('datetime.datetime.now')
  <built-in method now of type object at ...>

  >>> resolve('non existent module')
  Traceback (most recent call last):
  ...
  ImportError: No module named non existent module

  >>> resolve('__doc__')
  Traceback (most recent call last):
  ...
  ImportError: No module named __doc__

  >>> resolve('datetime.foo')
  Traceback (most recent call last):
  ...
  ImportError: No module named foo

  >>> resolve('os.path.split').__name__
  'split'

Here are some examples of importing relative names::

  >>> resolve('.split', 'os.path')
  <function split at ...>

  >>> resolve('..system', 'os.path')
  <built-in function system>

  >>> resolve('...datetime', 'os.path')
  <module 'datetime' ...>

NB: When relative names are imported, a module the name is relative to
**must** be supplied::

  >>> resolve('.split').__name__
  Traceback (most recent call last):
  ...
  ValueError: relative name without base module
