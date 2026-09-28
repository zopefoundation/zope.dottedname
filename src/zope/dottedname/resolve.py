##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Dotted name support
"""


def resolve(name, module=None):
    """Resolve ``name`` to a Python object via imports / attribute lookups.

    If ``module`` is None, ``name`` must be "absolute" (no leading dots).

    If ``module`` is not None, and ``name`` is "relative" (has leading dots),
    the object will be found by navigating relative to ``module``.

    Returns the object, if found.  If not, propagates the error.
    """
    orig_name = name
    parts = name.split('.')
    if not parts[0]:
        if module is None:
            raise ValueError("relative name without base module")
        # A name made up of nothing but dots (e.g. '.' or '..') splits
        # into one more empty segment than the equivalent name that is
        # followed by an actual attribute name (e.g. '.foo' or '..foo'),
        # because of the implicit empty segment after the trailing dot.
        # Drop that extra segment so both forms count leading dots the
        # same way.
        if not name.strip('.') and parts[-1] == '':
            parts.pop()
        module_parts = module.split('.')
        parts.pop(0)
        while parts and not parts[0]:
            if not module_parts:
                raise ValueError(
                    "'%s' goes above the top-level package '%s'"
                    % (orig_name, module))
            module_parts.pop()
            parts.pop(0)
        parts = module_parts + parts
        if not parts:
            raise ValueError(
                "'%s' leaves nothing to resolve relative to '%s'"
                % (orig_name, module))
        name = parts
    else:
        name = parts

    used = name.pop(0)
    found = __import__(used)
    for n in name:
        used += '.' + n
        try:
            found = getattr(found, n)
        except AttributeError:
            __import__(used)
            found = getattr(found, n)

    return found
