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
"""Filesystem Page Template module

Zope object encapsulating a Page Template from the filesystem.
"""

__metaclass__ = type

__version__ = '$Revision: 1.2 $'[11:-2]

import os, sys
import logging

from zope.pagetemplate.pagetemplate import PageTemplate

def package_home(gdict):
    filename = gdict["__file__"]
    return os.path.dirname(filename)

class PageTemplateFile(PageTemplate):
    "Zope wrapper for filesystem Page Template using TAL, TALES, and METAL"

    _v_last_read = 0

    def __init__(self, filename, _prefix=None):
        if not isinstance(_prefix, str):
            if _prefix is None:
                _prefix = sys._getframe(1).f_globals
            _prefix = package_home(_prefix)

        self.filename = os.path.join(_prefix, filename)

    def _cook_check(self):
        if self._v_last_read and not __debug__:
            return
        __traceback_info__ = self.filename
        try:
            mtime = os.path.getmtime(self.filename)
        except OSError:
            mtime = 0
        if self._v_program is not None and mtime == self._v_last_read:
            return
        self.pt_edit(open(self.filename), None)
        self._cook()
        if self._v_errors:
            logging.error('PageTemplateFile: Error in template: %s',
                '\n'.join(self._v_errors))
            return
        self._v_last_read = mtime

    def document_src(self, REQUEST=None):
        """Return expanded document source."""

        if REQUEST is not None:
            REQUEST.response.setHeader('Content-Type', self.content_type)
        return self.read()

    def pt_source_file(self):
        return self.filename

    def __getstate__(self):
        raise TypeError("non-picklable object")
