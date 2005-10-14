##############################################################################
#
# Copyright (c) 2005 Zope Corporation and Contributors.
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
"""Type sniffer for page template input

$Id$
"""

import xml.parsers.expat

XML_PREFIXES = [
    "<?xml",                      # ascii, utf-8
    "\xef\xbb\xbf<?xml",          # utf-8 w/ byte order mark
    "\0<\0?\0x\0m\0l",            # utf-16 big endian
    "<\0?\0x\0m\0l\0",            # utf-16 little endian
    "\xfe\xff\0<\0?\0x\0m\0l",    # utf-16 big endian w/ byte order mark
    "\xff\xfe<\0?\0x\0m\0l\0",    # utf-16 little endian w/ byte order mark
    ]

XML_PREFIX_MAX_LENGTH = max(map(len, XML_PREFIXES))

class NamespaceFound(Exception):
    # This exception is throwned by the parser when a namespace is
    # found to stop the parsing.
    pass

def StartNamespaceDeclHandler(prefix, url):
    # Called when an element contains a namespace declaration.
    raise NamespaceFound

def sniff_type(text):
    """Return 'text/xml' if text appears to be XML, otherwise return None.

     o if the document contains the xml process header <?xml ... ?>
     o if the document contains any namespace declarations
    """

    # Check the xml processing header
    for prefix in XML_PREFIXES:
        if text.startswith(prefix):
            return "text/xml"

    # Check if the document contains any namespace declarations
    parser = xml.parsers.expat.ParserCreate(namespace_separator=' ')
    parser.StartNamespaceDeclHandler = StartNamespaceDeclHandler
    try:
        parser.Parse(text)
    except xml.parsers.expat.ExpatError:
        return None
    except NamespaceFound:
        return "text/xml"
    else:
        return None

