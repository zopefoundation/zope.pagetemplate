=======================================
 ZPT (Zope Page-Template) Architecture
=======================================

There are a number of major components that make up the page-template
architecture:

- The TAL *compiler* and *interpreter*.  This is responsible for
  compiling source files and for executing compiled templates.  See
  the zope.tal_ package for more information.

- An *expression engine* is responsible for compiling expressions and
  for creating expression execution contexts.  It is common for
  applications to override expression engines to provide custom
  expression support or to change the way expressions are implemented.

  The :mod:`zope.pagetemplate.engine` module uses this to implement trusted
  and untrusted evaluation; a different engine is used for each, with
  different implementations of the same type of expressions.

  The z3c.ptcompat_ package extends these engines to use the
  Chameleon_ templating system for increased speed.

  Expression contexts support execution of expressions and provide
  APIs for setting up variable scopes and setting variables.  The
  expression contexts are passed to the TAL interpreter at execution
  time.

  The most commonly used expression implementation is that found in
  zope.tales_.

- Page templates tie everything together. They assemble an expression
  engine with the TAL interpreter and orchestrate management of source
  and compiled template data.  See :mod:`zope.pagetemplate.interfaces`.

.. _z3c.ptcompat: https://pypi.python.org/pypi/z3c.ptcompat
.. _zope.tal: https://pypi.python.org/pypi/zope.tal
.. _zope.tales: https://pypi.python.org/pypi/zope.tales
.. _Chameleon: https://chameleon.readthedocs.io/en/latest/
