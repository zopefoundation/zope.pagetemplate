===========
 ZPT Usage
===========

This document focuses on usage of the Page Templates API.

For information about writing Page Templates documents and using TAL
and TALES, refer to the `reference documentation
<https://pagetemplates.readthedocs.io/en/latest/>`_ or the
`Chameleon documentation
<https://chameleon.readthedocs.io/en/latest/reference.html>`_ if you
are using z3c.ptcompat.

.. testsetup::

    __file__ = 'docs/using.rst'

Simple Usage
============

Using Page Templates is very easy and straight forward. Let's look at
a quick example. Suppose we have a file called ``hello_world.pt`` with
these contents:

.. literalinclude:: hello_world.pt

.. doctest::

    >>> from zope.pagetemplate.pagetemplatefile import PageTemplateFile
    >>> my_pt = PageTemplateFile('hello_world.pt')
    >>> print(my_pt().strip())
    <html><body>Hello World</body></html>

Subclassing PageTemplates
=========================

Lets say we want to alter page templates such that keyword arguments
appear as top level items in the namespace. We can subclass
:class:`~.PageTemplate` and alter the default behavior of
:meth:`~.pt_getContext()` to add them in:

.. testcode::

    from zope.pagetemplate.pagetemplate import PageTemplate

    class mypt(PageTemplate):
        def pt_getContext(self, args=(), options={}, **kw):
           rval = PageTemplate.pt_getContext(self, args=args)
           options.update(rval)
           return options

    class foo(object):
        def getContents(self): return 'hi'

So now we can bind objects in a more arbitrary fashion, like the
following:

.. testcode::

  template = """
  <html>
  <body>
  <b tal:replace="das_object/getContents">Good Stuff Here</b>
  </body>
  </html>
  """

  pt = mypt()
  pt.write(template)
  print(pt(das_object=foo()).strip())

.. testoutput::

  <html>
  <body>
  hi
  </body>
  </html>
