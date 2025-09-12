=========
 Changes
=========

6.0 (2025-09-12)
================

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


5.2 (2025-08-06)
================

- Add preliminary support for Python 3.14.

- Add support for Python 3.13.

- Drop support for Python 3.7, 3.8.


5.1 (2024-02-08)
================

- Add support for Python 3.12.


5.0 (2023-02-07)
================

- Add support for ``zope.untrustedpython`` on Python 3. With it, Python
  expressions are now protected. It is activated using the ``untrusted`` extra.

- Add support for Python 3.11.

- Drop support for Python 2.7, 3.5, 3.6.


4.6.0 (2021-11-04)
==================

- Avoid traceback reference cycle in ``PageTemplate._cook``.

- Add support for Python 3.9 and 3.10.


4.5.0 (2020-02-10)
==================

- Add support for Python 3.8.

- Drop support for Python 3.4.


4.4.1 (2018-10-16)
==================

- Fix DeprecationWarnings for ``ComponentLookupError`` by
  importing them from ``zope.interface.interfaces``. See `issue 17
  <https://github.com/zopefoundation/zope.pagetemplate/issues/17>`_.

4.4 (2018-10-05)
================

- Add support for Python 3.7.

- Host documentation at https://zopepagetemplate.readthedocs.io/

4.3.0 (2017-09-04)
==================

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6, 3.2 and 3.3.

- Certain internal test support objects in the ``tests`` package were
  removed or modified.

- The ``TraversableModuleImporter`` properly turns ``ImportError``
  into ``TraversalError``. Previously it was catching ``KeyError``,
  which cannot be raised.

- Reach 100% code coverage and maintain it through automated testing.

4.2.1 (2015-06-06)
==================

- Add support for Python 3.2.

4.2.0 (2015-06-02)
==================

- Allow short-circuit traversal for non-proxied dict subclasses.  See:
  https://github.com/zopefoundation/zope.pagetemplate/pull/3 .

- Add support for PyPy / PyPy3.

4.1.0 (2014-12-27)
==================

- Add support for Python 3.4.

- Add support for testing on Travis.

4.0.4 (2013-03-15)
==================

- Ensure that ``ZopePythonExpr`` and ``PythonExpr`` are separate classes even
  when ``zope.untrustedpython`` is not available.  Fixes a ZCML conflict error
  in ``zope.app.pagetemplate``.

4.0.3 (2013-02-28)
==================

- Only allow ``zope.untrustedpython`` to be a dependency in Python 2.

- Fix buildout to work properly.

4.0.2 (2013-02-22)
==================

- Migrate from ``zope.security.untrustedpython`` to ``zope.untrustedpython``.

- Make ``zope.untrustedpython`` an extra dependency.  Without it, python
  expressions are not protected, even though path expressions are still
  security wrapped.

- Add support for Python 3.3.

4.0.1 (2012-01-23)
==================

- LP#732972:  PageTemplateTracebackSupplement no longer passes
  ``check_macro_expansion=False`` to old templates which do not
  accept this argument.

4.0.0 (2012-12-13)
==================

- Replace deprecated ``zope.interface.classProvides`` usage with equivalent
  ``zope.interface.provider`` decorator.

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.

- PageTemplate.pt_render() has a new argument, ``check_macro_expansion``,
  defaulting to True.

- PageTemplateTracebackSupplement passes ``check_macro_expansion=False``, to
  avoid LP#732972.

3.6.3 (2011-09-21)
==================

- Fix test assertions to be compatible with ``zope.tal`` 3.6.

3.6.2 (2011-09-21)
==================

- Change interface for engine and program such that the return type of
  the ``cook`` method is a tuple ``(program, macros)``. This follows
  the interface for the TAL parser's ``getCode`` method.

  Fixes a legacy compatibility issue where code would expect an
  ``_v_macros`` volatile attribute which was missing.

3.6.1 (2011-08-23)
==================

- Fix issue with missing default value for ``strictinsert``.

3.6.0 (2011-08-20)
==================

- Replace StringIO stream class with a faster list-based implementation.

- Abstract out the template engine and program interfaces and allow
  implementation replacement via a utility registration.

- Remove ancient copyright from test files (LP: #607228)

3.5.2 (2010-07-08)
==================

- Fix ``PTRuntimeError`` exception messages to be consistent across Python
  versions, and compatibile with the output under Python 2.4.  (More
  readable than the previous output under Python 2.6 as well.)

3.5.1 (2010-04-30)
==================

- Remove use of ``zope.testing.doctestunit`` in favor of stdlib's doctest.

- Add dependency on "zope.security [untrustedpython]" because the ``engine``
  module uses it.

3.5.0 (2009-05-25)
==================

- Add test coverage reporting support.

- Move 'engine' module and related test scaffolding here from
  ``zope.app.pagetemplate`` package.

3.4.2 (2009-03-17)
==================

- Remove old zpkg-related DEPENDENCIES.cfg file.

- Change package's mailing list address to zope-dev at zope.org, as
  zope3-dev at zope.org is now retired.

- Change `cheeseshop` to `pypi` in the packages' homepage url.

3.4.1 (2009-01-27)
==================

- Fix test due to recent changes in zope.tal.


3.4.0 (2007-10-02)
==================

- Initial release independent of the Zope 3 tree.


3.2.0 (2006-01-05)
==================

- Corresponds to the version of the zope.pagetemplate package shipped
  as part of the Zope 3.2.0 release.

- ZPTPage macro expansion:  changed label text to match the corresponding
  label in Zope 2 and activated the name spaces for macro expansion
  in 'read'.  See http://www.zope.org/Collectors/Zope3-dev/199

- Coding style cleanups.


3.1.0 (2005-10-03)
==================

- Corresponds to the version of the zope.pagetemplate package shipped
  as part of the Zope 3.1.0 release.

- Fixed apidoc and Cookie, which were using wrong descriptor class
  (changed to 'property').  See http://www.zope.org/Collectors/Zope3-dev/387

- Documentation / style / testing cleanups.


3.0.0 (2004-11-07)
==================

- Corresponds to the version of the zope.pagetemplate package shipped
  as part of the Zope X3.0.0 release.
