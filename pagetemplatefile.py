##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
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
"""Filesystem Page Template module

Zope object encapsulating a Page Template from the filesystem.

$Id$
"""

__all__ = ("PageTemplateFile",)

import os
import sys
import re
import logging

from zope.pagetemplate.pagetemplate import PageTemplate

from typesniffer import sniff_type
from typesniffer import XML_PREFIX_MAX_LENGTH

DEFAULT_ENCODING = "utf-8"

meta_pattern = re.compile(
    r'\s*<meta\s+http-equiv=["\']?Content-Type["\']?'
    r'\s+content=["\']?([^;]+);\s*charset=([^"\']+)["\']?\s*>\s*',
    re.IGNORECASE)

def package_home(gdict):
    filename = gdict["__file__"]
    return os.path.dirname(filename)

class PageTemplateFile(PageTemplate):
    "Zope wrapper for filesystem Page Template using TAL, TALES, and METAL"

    _v_last_read = 0

    def __init__(self, filename, _prefix=None):
        path = self.get_path_from_prefix(_prefix)
        self.filename = os.path.join(path, filename)
        if not os.path.isfile(self.filename):
            raise ValueError("No such file", self.filename)

    def get_path_from_prefix(self, _prefix):
        if isinstance(_prefix, str):
            path = _prefix
        else:
            if _prefix is None:
                _prefix = sys._getframe(2).f_globals
            path = package_home(_prefix)
        return path

    def _prepare_html(self, text):
        match = meta_pattern.search(text)
        if match is not None:
            type, encoding = match.groups()
            # TODO: Shouldn't <meta>/<?xml?> stripping
            # be in PageTemplate.__call__()?
            text = meta_pattern.sub("", text)
        else:
            type = None
            encoding = DEFAULT_ENCODING
        return unicode(text, encoding), type

    def _read_file(self):
        __traceback_info__ = self.filename
        f = open(self.filename, "rb")
        try:
            text = f.read(XML_PREFIX_MAX_LENGTH)
        except:
            f.close()
            raise
        type_ = sniff_type(text)
        if type_ == "text/xml":
            text += f.read()
        else:
            # For HTML, we really want the file read in text mode:
            f.close()
            f = open(self.filename)
            text = f.read()
            text, type_ = self._prepare_html(text)
        f.close()
        return text, type_

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
        text, type = self._read_file()
        self.pt_edit(text, type)
        self._cook()
        if self._v_errors:
            logging.error('PageTemplateFile: Error in template: %s',
                '\n'.join(self._v_errors))
            return
        self._v_last_read = mtime

    def pt_source_file(self):
        return self.filename

    def __getstate__(self):
        raise TypeError("non-picklable object")
