##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Simple variation of MultiMapping used to support layers of variable
declarations in TAL."""


class SafeMapping:
    def __init__(self, *dicts):
        self._mappings = list(dicts)
        self._mappings.reverse()

    def __getitem__(self, key):
        for d in self._mappings:
            if key in d:
                return d[key]
        raise KeyError, key

    def __contains__(self, key):
        for d in self._mappings:
            if key in d:
                return 1
        return 0

    has_key = __contains__

    def get(self, key, default=None):
        for d in self._mappings:
            if key in d:
                return d[key]
        return default

    def _push(self, dict):
        self._mappings.insert(0, dict)

    def _pop(self, count=1):
        del self._mappings[:count]
